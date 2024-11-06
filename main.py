import pandas as pd

df = pd.read_csv("dbPy.csv")
print(df.head())

df["Fecha"] = df["Fecha"].apply(lambda x: x.replace(x, f"{x[7:12]}-{x[4:6]}-{x[1:3]}") )
print(df.head())

df.to_csv("CDD_FormatoFecha.csv")