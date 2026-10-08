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
