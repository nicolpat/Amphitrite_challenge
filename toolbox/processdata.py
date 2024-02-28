import numpy as np
from datetime import datetime

class Along_track_statistics:
    def __init__(self, longitude, latitude, mean_adt, std_adt):
        self.longitude = longitude
        self.latitude = latitude
        self.adt = mean_adt
        self.std_adt = std_adt


def calculate_statistics_along_track(data, box=17):
    ''' Average the ADT every period to estimate
    the spatial variability of the measurements along
    the track of the satellite. '''

    N = len(data.time) // box       # Number of boxes along-track
    index_nearest = box // 2        # index of the data point associated to the spatial-average
                                    # This value is used to associate a longitude and a latitude
                                    # to our spatial averages

    # Create variables
    mean_adt = []
    std_adt = []
    longitude = []
    latitude = []

    n = 0
    # running mean
    for i in np.arange(0, N, 1):
        mean_adt.append(np.mean(data.adt[n:n + box - 1]))
        std_adt.append(np.std(data.adt[n:n + box - 1]))
        longitude.append(data.longitude[n + index_nearest])
        latitude.append(data.latitude[n + index_nearest])
        n = n + box # shift to the next period

    along_track_statistics = Along_track_statistics(
        np.array(longitude), np.array(latitude),
        np.array(mean_adt), np.array(std_adt))

    return along_track_statistics

def convert_date_copernicus(date,format ='%d of %B %Y'):
    date_str = str(date)
    date_str = date_str[0:-3] #remove last 3 digits
    date_conventional = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    date_newformat = date_conventional.strftime(format)

    return date_newformat
