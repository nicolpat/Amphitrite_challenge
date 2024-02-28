Amphitrite challenge 
=====================

This repository contains scripts designed for displaying altimetry data measured 
in the western part of the Atlantic between the 1st and 10th of February 2023 by 
Sentinel A and B satellites. The visualisation chosen aims to emphasise how ocean 
dynamics can be inferred from the variability in the measurements. Further 
information regarding the methods employed and conclusions drawn can be found in 
the figure captions (L3_product*.png).

Data were downloaded manually from https://data.marine.copernicus.eu/product/SEALEVEL_GLO_PHY_L3_NRT_008_044/description
The Python libraries required to run the scripts can be found in the requirements.txt file.

To run the program via the terminal (pip, venv and python3 must be installed on your machine)
-----------------------------------
1) Download the repository from GitHub https://github.com/nicolpat/Amphitrite_challenge
2) Open the terminal and go to the main directory.
3) Set up the virtual environnement.
4) Run main.py

The command lines are the following: 
> cd path_to/AMPHITRITE_Interview_Challenge/
> source venv/bin/activate
> pip install -r requirements.txt
> python3 main.py


To be improved
--------------
- Automatically download data from Copernicus, using python API

		Or

- Directly read data from Copernicus


