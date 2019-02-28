def right(at_point):
    delta = 0.1
    # TODO hard-coding the math function here - simple squaring function
    f_x_plus_delta = (at_point + delta)**2
    f_x = (at_point)**2
    der = (f_x_plus_delta - f_x) / delta
    return der

def central(at_point):
    delta = 0.1
    # TODO hard-coding the math function here - simple squaring function
    f_x_plus_delta = (at_point + delta)**2
    f_x_minus_delta = (at_point - delta)**2
    der = (f_x_plus_delta - f_x_minus_delta) / (2 * delta)
    return der