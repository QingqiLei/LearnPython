import pandas as pd
import numpy as np
dates = pd.date_range('20180607', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4), index = dates, columns = ['A','B','C','D'])
print(df)
print(type(df['A'])) # pandas.core.series.Series
print(type(df.loc['20180608']))
print(df['A'])
print(df.loc['20180608'])
print(type(df.iloc[3,1]))
print(df.iloc[3,1])
print(type(df[1:2]))
print(type(df[:3]))
print(df[1:2])
print(df[:100])
print(df.A)
print(df.20180608)
print(df)
