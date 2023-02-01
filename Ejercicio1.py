import pandas as pd

paciente1= [45,280,124,250,79,300,26,59,200,60,210,39,110,59,69,54]
paciente2= [120,125,122,125,119,121,120,119,120,124,125,120,117,130,127,125]


dataframe1=pd.DataFrame(paciente1)
dataframe2=pd.DataFrame(paciente2)

analisis1=dataframe1.describe()
analisis2=dataframe2.describe()

print(analisis1)
print(analisis2)