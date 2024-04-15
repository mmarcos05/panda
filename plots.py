import pandas as pd
import matplotlib.pyplot as plt

#Como crear plots en panda

#Usaremos el csv de air_quality

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

#Usamos index_col y parse_dates como parametros para convertir las columnas en objetos Timestamp y que aparezcan como variable independiente en los graficos

air_quality.plot() #es necesario primero hacer el plot para que despues el plt.show nos muestre el grafico

plt.show() #con esto obtenemos un grafico 