
class Absolute_dynamical_topography:
    def __init__(self, time, longitude, latitude, adt):
        self.time = time
        self.longitude = longitude
        self.latitude = latitude
        self.adt = adt

    def calculate_across_track_velocity(self):
        pass

def get_absolute_dynamical_topography(data):
    time = data['time'].values
    longitude = data['longitude'].values
    latitude = data['latitude'].values
    mean_dynamical_topography = data['mdt'].values
    sea_level_anomaly = data['sla_unfiltered'].values

    absolute_dynamical_topography = Absolute_dynamical_topography(
        time,longitude,latitude,mean_dynamical_topography+sea_level_anomaly)

    return absolute_dynamical_topography
