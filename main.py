''' This file contains the main program to visualise the spatial
variability observed along the track of two satellites. The initial
parameters can be tuned to '''

import xarray as xr

from toolbox.readdata import get_absolute_dynamical_topography
from toolbox.processdata import (calculate_statistics_along_track,
                                convert_date_copernicus)
from toolbox.showdata import (create_figure,
                              display_figure,
                              add_variability_absolute_dynamical_topography)

# INITIAL PARAMETERS ______________________________
# Set geographical limits of the study zone
MIN_LONGITUDE = - 80
MAX_LONGITUDE = - 50
MIN_LATITUDE = 25
MAX_LATITUDE = 40
BOX_FRAME = [MIN_LONGITUDE, MAX_LONGITUDE, MIN_LATITUDE, MAX_LATITUDE]

# Set parameters for the visualisation
DISPLAY_FIGURE = True
SAVE_FIGURE = True

# PROGRAM _______________________________
# Open data file
data_sentinel_A = xr.open_mfdataset('copernicus-data/sentinel_3A/*.nc', combine='by_coords')
data_sentinel_B = xr.open_mfdataset('copernicus-data/sentinel_3B/*.nc', combine='by_coords')

# Get absolute dynamical topography
adt_sentinel_A = get_absolute_dynamical_topography(data_sentinel_A)
adt_sentinel_B = get_absolute_dynamical_topography(data_sentinel_B)

# Calculate statistics along the track of the satellite
# -> This function averages the ADT along the satellite track to estimate a
# mean value every 17 data points (sampled every second). This period roughly
# corresponds to the time needed for a satellite to travel across 1° latitude
box = 17  # box length (points)
statistics_sentinel_A = calculate_statistics_along_track(adt_sentinel_A, box=box)
statistics_sentinel_B = calculate_statistics_along_track(adt_sentinel_B, box=box)

print(adt_sentinel_A.time)

# Display the along-track variability in absolute dynamical topography
title = f'Along-track variability in Absolute Dynamical Topography (ADT)'
legend = 'Sentinel A', 'Sentinel B'
colorbar_unit = 'Standard deviation [m]'
datestart = convert_date_copernicus(adt_sentinel_A.time[0])
dateend = convert_date_copernicus(adt_sentinel_A.time[-1])
caption = \
    (f"Spatial variability in absolute dynamical Topography observed along the track "
         f"of the satellites between the {datestart} and the {dateend}, "
         f"within the Gulf Stream region. The ADT was averaged along the satellite track to "
         f"estimate a standard deviation every {box} data points. This period roughly corresponds "
         f"to the time needed for a satellite to collect data across 1° latitude. This method provides "
         f"a simple a way to detect dynamical regions from ungridded altimetric data. For instance, "
         f"the highest variability is found in the north-western part of the domain, revealing the "
         f"presence of the Gulf Stream (red dots). More generally, this method shows a potential to "
         f" detect mesoscale phenomena (ex: eddy core located at 50°W - 34°N ?).")

create_figure(box_frame=BOX_FRAME)
add_variability_absolute_dynamical_topography(statistics_sentinel_B, marker='o', markersize = 30, color=None)
add_variability_absolute_dynamical_topography(statistics_sentinel_A, marker='s', markersize = 30, color=None)
display_figure(title=title,
               legend=legend,
               colorbar_unit=colorbar_unit,
               caption = caption,
               display=DISPLAY_FIGURE,
               savefig=SAVE_FIGURE)
