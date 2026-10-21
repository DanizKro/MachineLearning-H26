# %% #-------------------------
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
import sklearn
# %% #-------------------------
# Set the directory in which to store data
NB_DIR = Path.cwd()       # Set NB_DIR to be the current working directory
DATA = NB_DIR/'data'      # The data dir is the subdirectory 'data' under NB_DIR

DATA.mkdir(exist_ok=True) # Create the data directory

# %% #-------------------------
import urllib.request

# Define the file path
FILE = DATA / 'World-Stock-Prices-Dataset.csv'

# %% #-------------------------
stockdata = pd.read_csv(FILE)

# %%#-------------------------
stockdata.head()

# %% 
#Prosseserer markedsdata CSVen og lagere nye basert på Brand_Name (eller Ticker) i processed-mappen
# Definer sti til processed-mappen (data/processed)
PROCESSED_DATA = DATA / "processed"

# Opprett 'processed'-mappen dersom den ikke finnes fra før
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

# Grupper datasettet etter 'Brand_Name' (eller 'Ticker') og lagre hver gruppe til en CSV-fil
for brand, group in stockdata.groupby("Brand_Name"):
    # Rens mappenavnet/filnavnet for ulovlige tegn som '/' og ekstra mellomrom
    safe_brand_name = brand.replace('/', '_').replace(' ', '_').strip()
    
    # Generer trygg sti i DATA-mappen
    filepath = PROCESSED_DATA / f"{safe_brand_name}_stock.csv"
    
    group.to_csv(filepath, index=False)
    print(f"Lagret: {filepath}")

# %%
