import numpy as np
class Along_track_statistics:
    def __init__(self, longitude, latitude, mean_adt, std_adt):
        self.longitude = longitude
        self.latitude = latitude
        self.adt = mean_adt
        self.std_adt = std_adt


def calculate_statistics_along_track(data, dp = 19):
    ''' Average the ADT every 19 points to estimate
    a variability on the measurements. We assume a speed of
    6km/s for a satellite '''

    N = len(data.time) // dp
    n = 0
    index_nearest = dp // 2

    mean_adt = []
    std_adt = []
    longitude = []
    latitude = []

    for i in np.arange(0, N, 1):
        mean_adt.append(np.mean(data.adt[n:n + dp - 1]))
        std_adt.append(np.std(data.adt[n:n + dp - 1]))
        longitude.append(data.longitude[n + index_nearest])
        latitude.append(data.latitude[n + index_nearest])
        n = n + dp

    along_track_statistics = Along_track_statistics(
        np.array(longitude), np.array(latitude),
        np.array(mean_adt), np.array(std_adt))

    return along_track_statistics

def clean_adt():
    pass