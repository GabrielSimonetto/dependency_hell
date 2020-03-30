from pathlib import Path
from data import gibe_data

PROJECT_ROOT = Path(__file__).parents[2]
DATAPATH = PROJECT_ROOT.joinpath('data')
DATAFILE = DATAPATH.joinpath('mock_data.csv')
