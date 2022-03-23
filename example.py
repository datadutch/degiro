import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13],['Thomas',13],['Tom',120]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)