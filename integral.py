import numpy as np

def rect_low(from_x, to_x):
    precision = 0.1
    to_x_actual = to_x - precision # stop at second to last point
    n_x = (to_x_actual - from_x) / precision + 1
    # TODO avoid hard-coding the math function here
    area_total = 0.
    for x in np.linspace(from_x, to_x_actual, n_x): # TODO vectorize with np !
        y = x**2
        area_local = precision * y
        area_total += area_local

    return area_total

def rect_high(from_x, to_x):
    precision = 0.1
    from_x_actual = from_x + precision
    n_x = (to_x - from_x_actual) / precision + 1
    # TODO avoid hard-coding the math function here
    area_total = 0.
    for x in np.linspace(from_x_actual, to_x, n_x): # TODO vectorize with np !
        y = x**2
        area_local = precision * y
        area_total += area_local

    return area_total

def rect_avg(from_x, to_x):
    low = rect_low(from_x, to_x)
    high = rect_high(from_x, to_x)
    return (low + high) / 2

def rect_trap(from_x, to_x):
    return -1 # TODO