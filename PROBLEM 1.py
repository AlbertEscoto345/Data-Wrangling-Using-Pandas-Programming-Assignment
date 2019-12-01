import pandas as pd

data1={'Student': ['Ice Bear','Panda','Grizzly'],'Math': [80,95,79]}
df1=pd.DataFrame(data1, columns=['Student','Math'])

data2={'Student': ['Ice Bear','Panda','Grizzly'],'Electronics': [85,81,83]}
df2=pd.DataFrame(data2, columns=['Student','Electronics'])

data3={'Student': ['Ice Bear','Panda','Grizzly'],'GEAS': [90,79,93]}
df3=pd.DataFrame(data3, columns=['Student','GEAS'])

data4={'Student': ['Ice Bear','Panda','Grizzly'],'ESAT': [93,89,88]}
df4=pd.DataFrame(data4, columns=['Student','ESAT'])

df5=df1.merge(df2,on='Student').merge(df3,on='Student').merge(df4,on='Student')
df6=pd.melt(df5,id_vars=['Student'],var_name='Subjects', value_name='Grades')