import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a csv file from a given path and return a pandas DataFrame"""
    data = pd.read_csv(path)
    if data is None:
        raise Exception("Data is not loaded")
    if len(data) == 0:
        raise Exception("Data is empty")
    print("Loading dataset of dimensions ", data.shape)
    return data
