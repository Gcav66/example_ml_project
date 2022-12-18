import pandas as pd

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting workflow")

df1 = pd.read_csv("src_data/dev/dev_data.csv")
df1 = df1.drop('MedInc', axis=1)

df2 = pd.read_csv("src_data/stg/stg_data.csv")
df2 = df1.drop('MedInc', axis=1)

df3 = pd.read_csv("src_data/prod/dev_data.csv")
df3 = df1.drop('MedInc', axis=1)

