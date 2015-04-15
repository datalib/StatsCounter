StatsCounter
------------

A statistics-powered Python container.


Usage
-----

.. code-block:: python

    >>> import statscounter as sc
    >>> letter_freq = sc.StatsCounter(a=1, b=2, c=3, d=4, e=4, f=6)
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
