from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
from pathlib import Path

 
bank_marketing = fetch_ucirepo(id=222)
# Check file accessed.
# print(bank_marketing)

# Check structure
#print(type(bank_marketing))
#print(dir(bank_marketing))

X = bank_marketing.data.features
y = bank_marketing.data.targets
# print(X.head())
# print(y.head())

df = pd.concat([X, y], axis=1)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isna().sum())
print((df == "NaN").sum())