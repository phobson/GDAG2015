import numpy as np
def sigFigs(value, N):
    if not np.isfinite(value):
        raise ValueError("`value` must be a finite number")

    if N < 1:
        raise ValueError("you need at least 1 sig fig")

    order = np.floor(np.log10(np.abs(value)))
    decimal_places = int(N - 1 - order)
    if decimal_places <= 0:
        output = '{0:,.0f}'.format(round(value, decimal_places))

    else:
        fmt = '{0:,.%df}' % decimal_places
        output = fmt.format(value)

    return output
