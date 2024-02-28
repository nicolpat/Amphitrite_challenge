# Import modules
import copernicusmarine
from pprint import pprint

# !!!! download data between 10th of Feb and 20th of Feb 2024 !!!

def download_data_sentinel_A():
    # DatasetIDs of interest (3-hourly waves and daily currents)
    dataset_ids = ["cmems_obs-sl_glo_phy-ssh_nrt_s3a-l3-duacs_PT1S"]

    # Dates from June 20 to June 23
    date_range = "*/2023/02/*_2023021*.nc"

    # Define output storage parameters
    output_directory = "./copernicus-data/sentinel_3A/"

    # Call the get function for each dataset to save files for the date range
    for dataset_id in dataset_ids:
        get_files = copernicusmarine.get(
            dataset_id=dataset_id,
            output_directory=output_directory,
            filter=date_range,
            no_directories = True,
        )

    pprint(f"List of downloaded files for {dataset_id} is: \n{get_files}")

def download_data_sentinel_B():
    # DatasetIDs of interest (3-hourly waves and daily currents)
    dataset_ids = ["cmems_obs-sl_glo_phy-ssh_nrt_s3b-l3-duacs_PT1S"]

    # Dates from June 20 to June 23
    date_range = "*/2023/02/*_2023021*.nc"

    # Define output storage parameters
    output_directory = "./copernicus-data/sentinel_3B/"

    # Call the get function for each dataset to save files for the date range
    for dataset_id in dataset_ids:
        get_files = copernicusmarine.get(
            dataset_id=dataset_id,
            output_directory=output_directory,
            filter=date_range,
            no_directories=True)

    pprint(f"List of downloaded files for {dataset_id} is: \n{get_files}")


