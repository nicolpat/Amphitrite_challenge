# Import modules
import copernicusmarine
from pprint import pprint


dataset_id = ('nrt_global_s3b_phy_l3_1hz_20230201_20230222.nc')

output_directory = "copernicus-data"

get_files = copernicusmarine.get(
    dataset_id=dataset_id,
    output_directory=output_directory,
    )
