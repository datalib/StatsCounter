StatsCounter: A statistics-enabled Python container
---------------------------------------------------

::

         _        _                             _
     ___| |_ __ _| |_ ___  ___ ___  _   _ _ __ | |_ ___ _ __
    / __| __/ _` | __/ __|/ __/ _ \| | | | '_ \| __/ _ \ '__|
    \__ \ || (_| | |_\__ \ (_| (_) | |_| | | | | ||  __/ |
    |___/\__\__,_|\__|___/\___\___/ \__,_|_| |_|\__\___|_|


StatsCounter is a GNU Licensed, statistics powered version
of Python's standard library ``Counter`` class. It attaches
several helpful methods that can be used to make your
data-driven uses a breeze.

Usage
-----

As a histogram
~~~~~~~~~~~~~~

.. code-block:: python

    >>> import statscounter as stats
    >>> letter_freq = stats.StatsCounter(a=1, b=2, c=3, d=4, e=4, f=6)
    >>> letter_freq.mean()      # average frequency
    3.3333333333333335
    >>> letter_freq.mode()      # most frequent element
    4
    >>> letter_freq.median()    # the median number (avg if even # of items)
    3.5
    >>> letter_freq.variance()  # sample variance
    3.066666666666667
    >>> letter_freq.stdev()     # sample standard deviation
    1.7511900715418263
    >>> letter_freq.pvariance() # population variance
    2.555555555555556
    >>> letter_freq.pstdev()    # population std. dev.
    1.5986105077709065
    >>> letter_freq.max()       # the maximum value
    6
    >>> letter_freq.argmax()    # the argument yielding the maximum value
    "f"

As a utility
~~~~~~~~~~~~

.. code-block:: python

    >>> import statscounter as stats
    >>> stats.mean([1, 2, 3, 4, 4, 6])      # average frequency
    3.3333333333333335
    >>> stats.mode([1, 2, 3, 4, 4, 6])      # most frequent element
    4
    >>> stats.median([1, 2, 3, 4, 4, 6])    # the median number (avg if even # of items)
    3.5
    >>> stats.variance([1, 2, 3, 4, 4, 6])  # sample variance
    3.066666666666667
    >>> stats.stdev([1, 2, 3, 4, 4, 6])     # sample standard deviation
    1.7511900715418263
    >>> stats.pvariance([1, 2, 3, 4, 4, 6]) # population variance
    2.555555555555556
    >>> stats.pstdev([1, 2, 3, 4, 4, 6])    # population std. dev.
    1.5986105077709065
