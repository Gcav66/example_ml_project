import os
import pandas as pd

import logging
logging.basicConfig(level=logging.DEBUG)

DATA_ENV = os.environ["DATA_ENV"].lower()

def ingest_data():
    """WIP: Read data from sklearn dataset"""
    logging.info(DATA_ENV)
    logging.info(os.getcwd())
    data_path = f"src_data/{DATA_ENV}/{DATA_ENV}_data.csv"
    df = pd.read_csv(data_path)
    logging.info(df.head())
    return df

if __name__ == '__main__':
    ingest_data()