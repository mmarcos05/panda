import pandas as pd

#Las tablas en panda se llaman Dataframe, se crean con el alias df
#Usamos diccionarios para poner las variables donde las claves de los diccionarios son los nombres de las columnas y en el valor usamos una lista 
# con todas las filas que querramos de esa variable tenga

cabros = pd.DataFrame(
    {
        "Nombre" : ["Marcos Matascuso",
                     "Mateo Cicarello",
                     "Valentino Tiscornia",
                     "Leo Duco",
                     "Federico Fiori",
                     "Lucas Giorgeti",
                     "Bruno Berbech",
                     "Fabricio Mollo",
                     "Ignacio Rios",
                     "Constantino Alvarez",
                     "Joaquin Miller",
                     "Geronimo Furland",
                     "Ivan Tupa",
                     "Matias Gueler",
                     "Santino Calvani",
                     "Fide Jazan"
                     ],
        "Edad" : [18, 19, 19, 19, 19, 19, 18, 16, 19, 19, 19, 19 ,19 , 19, 19, 19],
        "Posicion" : ["Lateral", 
                      "Lateral",
                      "Central",
                      "Arquero",
                      "Mediocampista",
                      "Lateral",
                      "Delantero",
                      "Mediocampista",
                      "Delantero",
                      "Delantero",
                      "Lateral",
                      "Central",
                      "Central",
                      "Mediocampista",
                      "Mediocampista",
                      "Delantero"],
        "Dorsal" : [4, 3, 2, 1, 8, 22, 9, None , None, 27, 21, 95, 25, 6, 5, 10],
        "Goles" : [6, 3, 3, 0, 5, 0, 6, 1, 5, 4, 1, 0, 7, 0, 3, 13]
    }
)

cabros

#Cada columna se le llama serie

cabros["Goles"]

#Podemos agregarle una serie a un diccionario

#titulares = pd.Series([], name = "Titulares")

#Usando cabros.describre() nos tira un analisis de las columnas con datos tipo int, como promedios, maximos, minimos
#Tambien podemos usar cabros.max() para obtener el maximo valor de las columnas con valores tipo int

#Queremos analizar un archivo(leerlo)}
#con la funcion archivo = pd.read_"tipo de archivo"()

titanic = pd.read_csv("titanic.csv")


#Para ver las primeras n columnas de un DataFrame usamos .head(n)
#Si queremos ver las ultimas n columnas usamos .tail(n)

titanic.head(10)

#Para ver los tipos de datos que interpreta panda para cada columna usamos .dtypes

titanic.dtypes

#Como usamos read_ para leer archivos, usamos to_ para almacenar data, to_excel() transforma la data en un archivo excel

cabros.to_excel("cabros.xlsx", sheet_name= "cabros", index=False)

cabros_leer  = pd.read_excel("cabros.xlsx", sheet_name = "cabros")

#Si quiero un resumen del DataFrame uso .info()

cabros.info()

#Si queremos ver varias colunmas de nuestro DF:

cabros_goles_dorsal = cabros[["Goles", "Dorsal"]]

#Si queremos ver filas de nuestro DF con condiciones

goles_3_o_mas = cabros[cabros["Goles"] >= 3]

goles_3_o_mas.shape #nos dice la cantidad de filas que cumplen con esta condicion

#Quiero ver los centrales y laterales que tiene el equipo

defensores = cabros[(cabros["Posicion"] == "Lateral") | (cabros["Posicion"] == "Central")]

print(defensores)

#aca no usamos el or y and, sino que usamos | para or y & para and

#El condicional notna() nos devuelve True cuando el valor la de la fila no es Null

sin_dorsal = cabros[["Dorsal"].notna()]

sin_dorsal.shape

#Como selecciono filas y columnas especificas

nombre_goleadores = cabros.loc[cabros["Goles"] > 5, "Nombre"]

cabros.iloc[2:10, 2:5]