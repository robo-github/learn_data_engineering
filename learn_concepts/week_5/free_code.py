import pandas as pd

data = {
    "number": [10, 20, 10],
    "index": [1, 2, 3]
}

df = pd.DataFrame(data)
print(df.iloc[0])
