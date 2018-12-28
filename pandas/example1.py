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
print(df.iloc[3,1]) # row and column
print(type(df[1:2]))
print(type(df[:3]))
print(df[1:2])
print(df[:100])
print(df.A) # 对列有用
print(df.A > 4)
df.B[df.A > 4] = 0
print(df)
print(df.B > 3)
df.iloc[0,1] = np.nan # like the null
df.iloc[0,1]
df.dropna(axis = 0, how = 'any') # remove the first row
df.iloc[0,1] = np.nan
print(df)
df.fillna(value = 100)
df1 = pd.DataFrame(np.ones((3,4)) * 3, columns=['a','b','c','d'], index = [1,2,3])
df2 = pd.DataFrame(np.ones((3,4)) * 0, columns = ['a','b','c','d'], index = [2,3,4])
df3 = pd.DataFrame(np.ones((3,4)) * 2, columns = ['a','b','c','d'])
res = pd.concat([df1,df2,df3],axis = 0) # rows, from top to bottom
print(res)
res = pd.concat([df1,df2,df3], axis = 0, ignore_index=True)# reset row index,
print(res)
res = pd.concat([df1,df2,df3], axis = 0, join = 'inner')
print(res)
s1 = pd.Series([1,2,3,4], index = ['a','b','c','d'])
res = df1.append(s1,ignore_index=True)
print(res)
import numpy as np
ran = np.random.rand(4,4)
df = pd.DataFrame(ran, index = [i for i in range(4)], columns = [i for i in range(4)])
df
df.iloc[0,0]
df2 = df.apply(lambda x:x**2)
df2
df2.describe()
