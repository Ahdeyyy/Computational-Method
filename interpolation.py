def linear_spline_interpolation(x_values,y_values):
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length.")
    def interpolate (x):
        if x < min(x_values) or x > max(x_values):
            raise ValueError("x is out of range of the provided x_values.") 
        i = 0
        while x > x_values[i]:
            i += 1

        # Perform linear interpolation
        x0, x1 = x_values[i-1], x_values[i]
        y0, y1 = y_values[i-1], y_values[i]

        # Equation of the straight line (linear interpolation formula)
        y = y0 + ( ((y1 - y0) * (x - x0)) / (x1 - x0))

        return y
    return interpolate
