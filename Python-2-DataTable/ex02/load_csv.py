import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a csv file from a given path and return a pandas DataFrame"""
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions ", data.shape)
        return data
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except ValueError:
        print(f"Error loading file: {path}")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
