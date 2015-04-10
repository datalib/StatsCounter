"""Moved private statistical methods away from StatsCounter definition"""

from __future__ import division

import collections
import math

from fractions import Fraction
from decimal import Decimal

# === Private utilities ===

def _sum(data, start=0):
    """_sum(data [, start]) -> value
    Return a high-precision sum of the given numeric data. If optional
    argument ``start`` is given, it is added to the total. If ``data`` is
    empty, ``start`` (defaulting to 0) is returned.
    Examples
    --------
    >>> _sum([3, 2.25, 4.5, -0.5, 1.0], 0.75)
    11.0
    Some sources of round-off error will be avoided:
    >>> _sum([1e50, 1, -1e50] * 1000)  # Built-in sum returns zero.
    1000.0
    Fractions and Decimals are also supported:
    >>> from fractions import Fraction as F
    >>> _sum([F(2, 3), F(7, 5), F(1, 4), F(5, 6)])
    Fraction(63, 20)
    >>> from decimal import Decimal as D
    >>> data = [D("0.1375"), D("0.2108"), D("0.3061"), D("0.0419")]
    >>> _sum(data)
    Decimal('0.6963')
    Mixed types are currently treated as an error, except that int is
    allowed.
    """
    # We fail as soon as we reach a value that is not an int or the type of
    # the first value which is not an int. E.g. _sum([int, int, float, int])
    # is okay, but sum([int, int, float, Fraction]) is not.
    allowed_types = {int, type(start)}
    n, d = _exact_ratio(start)
    partials = {d: n}  # map {denominator: sum of numerators}
    # Micro-optimizations.
    exact_ratio = _exact_ratio
    partials_get = partials.get
    # Add numerators for each denominator.
    for x in data:
        _check_type(type(x), allowed_types)
        n, d = exact_ratio(x)
        partials[d] = partials_get(d, 0) + n
    # Find the expected result type. If allowed_types has only one item, it
    # will be int; if it has two, use the one which isn't int.
    assert len(allowed_types) in (1, 2)
    if len(allowed_types) == 1:
        assert allowed_types.pop() is int
        T = int
    else:
        T = (allowed_types - {int}).pop()
    if None in partials:
        assert issubclass(T, (float, Decimal))
        assert not math.isinf(partials[None])
        return T(partials[None])
    total = Fraction()
    for d, n in sorted(partials.items()):
        total += Fraction(n, d)
    if issubclass(T, int):
        assert total.denominator == 1
        return T(total.numerator)
    if issubclass(T, Decimal):
        return T(total.numerator)/total.denominator
    return T(total)


def _check_type(T, allowed):
    if T not in allowed:
        if len(allowed) == 1:
            allowed.add(T)
        else:
            types = ', '.join([t.__name__ for t in allowed] + [T.__name__])
            raise TypeError("unsupported mixed types: %s" % types)


def _exact_ratio(x):
    """Convert Real number x exactly to (numerator, denominator) pair.
    >>> _exact_ratio(0.25)
    (1, 4)
    x is expected to be an int, Fraction, Decimal or float.
    """
    try:
        try:
            # int, Fraction
            return (x.numerator, x.denominator)
        except AttributeError:
            # float
            try:
                return x.as_integer_ratio()
            except AttributeError:
                # Decimal
                try:
                    return _decimal_to_ratio(x)
                except AttributeError:
                    msg = "can't convert type '{}' to numerator/denominator"
                    raise TypeError(msg.format(type(x).__name__))
    except (OverflowError, ValueError):
        # INF or NAN
        if __debug__:
            # Decimal signalling NANs cannot be converted to float :-(
            if isinstance(x, Decimal):
                assert not x.is_finite()
            else:
                assert not math.isinf(x)
        return (x, None)


# FIXME This is faster than Fraction.from_decimal, but still too slow.
def _decimal_to_ratio(d):
    """Convert Decimal d to exact integer ratio (numerator, denominator).
    >>> from decimal import Decimal
    >>> _decimal_to_ratio(Decimal("2.6"))
    (26, 10)
    """
    sign, digits, exp = d.as_tuple()
    if exp in ('F', 'n', 'N'):  # INF, NAN, sNAN
        assert not d.is_finite()
        raise ValueError
    num = 0
    for digit in digits:
        num = num*10 + digit
    if exp < 0:
        den = 10**-exp
    else:
        num *= 10**exp
        den = 1
    if sign:
        num = -num
    return (num, den)


def _counts(data):
    # Generate a table of sorted (value, frequency) pairs.
    table = collections.Counter(iter(data)).most_common()
    if not table:
        return table
    # Extract the values with the highest frequency.
    maxfreq = table[0][1]
    for i in range(1, len(table)):
        if table[i][1] != maxfreq:
            table = table[:i]
            break
    return table
