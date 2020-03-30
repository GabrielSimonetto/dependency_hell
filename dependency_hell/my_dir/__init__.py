from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[2]
DATAPATH = PROJECT_ROOT.joinpath('data')
DATAFILE = DATAPATH.joinpath('mock_data.csv')
