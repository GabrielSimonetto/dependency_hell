from dependency_hell.my_dir import DATAFILE

def gibe_data():
    with DATAFILE.open() as f:
        return f.read()
