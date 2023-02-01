#Importar pandas
import pandas as pd

#Traer fuente de datos
edadescasa1=[25,25,25,25,25]
edadescasa2=[1,4,24,26,70]

#Generar data frames

dataframe1=pd.DataFrame(edadescasa1)
dataframe2=pd.DataFrame(edadescasa2)

#Generar analisis descriptivo
analisis1=dataframe1.describe()
analisis2=dataframe2.describe()

#Mostrar resultados

print(analisis1)
print("\n")
print(analisis2)