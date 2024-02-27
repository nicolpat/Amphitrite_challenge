import xarray as xr

from toolbox.readdata import get_absolute_dynamical_topography
from toolbox.showdata import (create_figure,
                              add_track,
                              display_figure,
                              add_variability_absolute_dynamical_topography,
                              add_absolute_dynamical_topography)
from toolbox.processdata import calculate_statistics_along_track


# INITIAL PARAMETERS ______________________________
# Set geographical limits of the study zone
MIN_LONGITUDE = - 80
MAX_LONGITUDE = - 50
MIN_LATITUDE = 25
MAX_LATITUDE = 40
BOX_FRAME = [MIN_LONGITUDE, MAX_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE]

# Set time limit of the study period
DATE_START = 1 #
DATE_END = 2 #

# Set parameters for the visualisation
TITLE = ''
DISPLAY_FIGURE = True

# PROGRAM _______________________________
# Download data

# Open data file
data_sentinel_A = xr.open_mfdataset('copernicus-data/sentinel_3A/*.nc',combine='by_coords')
data_sentinel_B = xr.open_mfdataset('copernicus-data/sentinel_3B/*.nc',combine='by_coords')

# Get ocean property
adt_sentinel_A = get_absolute_dynamical_topography(data_sentinel_A)
adt_sentinel_B = get_absolute_dynamical_topography(data_sentinel_B)

# Calculate statistics along the track of the satellite
# -> This function averages the ADT along the satellite track to estimate a
# mean value every 17 data points (sampled every second). This period roughly
# corresponds to the time needed for a satellite to travel across 1° latitude
T = 17 # time-frame (sec)
statistics_sentinel_A = calculate_statistics_along_track(adt_sentinel_A,period=T)
statistics_sentinel_B = calculate_statistics_along_track(adt_sentinel_B,period=T)

# Display ocean property
#Figure 1
title = f'Variability in Absolute Dynamical Topography (ADT)'
legend = 'Sentinel A','Sentinel B'
colorbar_unit = 'Standard deviation [m]'


create_figure(box_frame=BOX_FRAME)
add_variability_absolute_dynamical_topography(statistics_sentinel_B, marker='o',color = None)
add_variability_absolute_dynamical_topography(statistics_sentinel_A, marker='s',color = None)
display_figure(title = title,
               display = DISPLAY_FIGURE,
               legend = legend,
               colorbar_unit=colorbar_unit,
               savefig = True)

#Figure 2
title = f'Absolute Dynamical Topography (ADT) averaged along the track of the satellites'
legend = 'Sentinel A','Sentinel B'
colorbar_unit = 'ADT [m]'

create_figure(box_frame=BOX_FRAME)
add_absolute_dynamical_topography(statistics_sentinel_B, marker='o',color = None)
add_absolute_dynamical_topography(statistics_sentinel_A, marker='s',color = None)
display_figure(title = title,
               display = DISPLAY_FIGURE,
               legend = legend,
               colorbar_unit = colorbar_unit,
               savefig=True)



