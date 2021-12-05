import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#df = pd.read_csv('/Users/ezequieldjemdjemian/Documents/TP_FIUBA_Regresion/ventas.csv')
df = pd.read_csv('ventas.csv')


df['ambientes'] = df['ambientes'].fillna(df['ambientes'].mean())
df['habitaciones'] = df['habitaciones'].fillna(df['habitaciones'].mean())
df['banos'] = df['banos'].fillna(df['banos'].mean())
    #vamos a realizar la imputacion para las columnas 'lat' y 'lon', imputando el promedio de calculado para cada ciudad. Es decir, si existiese un registro con 'lat' y 'lon' con missing value para la 'Ciudad' = 'Achiras', 
    # a ese registro le imputaremos el promedio de las coordenadas, obtenidos a partir de nuestra muestra, pero calculada sobre 'Ciudad' = 'Achiras'.

    #creo el dataframe con los promedios de latitud y longitud por ciudad
coordenadas_mean_by_ciudad = df.groupby(['Ciudad'], as_index=False)['lat','lon'].mean()
coordenadas_mean_by_ciudad.rename(columns={'lat':'latitud' , 'lon':'longitud'}, inplace=True)

    #del df original, me quedo con aquellos registros que no tienen latitud ni longitud, y en donce la ciudad no es nula
df_sin_coordenadas = df[(df['lat'].isnull() | df['lon'].isnull() ) &  (df['Ciudad'].isnull()==False)] 


    #joineo los promedios de lat y long por ciudad, junto con el subconjunto del dataset que no tiene lat ni long
subconjunto = df_sin_coordenadas.join(coordenadas_mean_by_ciudad.set_index('Ciudad'), on='Ciudad')
subconjunto.drop(columns = ['lat','lon'], inplace=True)

    #renombro las columnas del conjunto original, y borro los registros nulos para esos registros
conjunto_original = df.rename(columns={'lat':'latitud' , 'lon':'longitud'})
conjunto_original.dropna(subset=['latitud','longitud'], inplace=True)

df = conjunto_original.append(subconjunto)

    #finalmente renombro las columnas como 'lat' y 'lon'
df.rename(columns={'latitud':'lat', 'longitud':'lon'}, inplace=True)