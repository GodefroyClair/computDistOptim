import pandas as pd
from geopy import distance


def dist(compCords, prospCords):
    def distanceCalc(compCoord):
        # print("compCoord: ", compCoord)
        # return the list of result instead of using append() method
        propsDist = prospCords.apply(
            lambda row: distance.great_circle(
                compCoord, [
                    row['prospLat'], row['prospLong']]).miles, axis=1)
        # clean data in a pandas Series
        # print("propsDist: \n", propsDist)
        return propsDist.apply(lambda d: 0. if d > 300 else d)

    # Here too return the list through the output
    compDist = compCords.apply(lambda row: distanceCalc(
        [row['compLat'], row['compLong']]), axis=1)

    return pd.DataFrame(compDist)
