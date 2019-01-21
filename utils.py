import numpy as np

def wind_direction(degrees):
    directions = np.array('N NE E SE S SW W NW N'.split())
    bins = np.arange(22.5, 385, 45)
    return directions[np.digitize(degrees, bins)]
