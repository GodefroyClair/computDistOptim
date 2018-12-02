import pandas as pd
from geopy import distance


def dist(compCords, prospCords):
    prospectsArray = []
    prospArr = []

    for i, row in prospCords.iterrows():
        lat1 = row['prospLat']
        lon2 = row['prospLong']
        coords = [lat1, lon2]
        distanceArr2 = []

        for x, row2 in compCords.iterrows():
            lat2 = row2['compLat']
            lon2 = row2['compLong']
            coords2 = [lat2, lon2]
            dist = distance.great_circle(coords, coords2).miles
            if dist > 300:
                dist = 0.

            distanceArr2.append(dist)
        prospArr.append(distanceArr2)
    prospectsArray.extend(prospArr)

    return pd.DataFrame(prospectsArray)
