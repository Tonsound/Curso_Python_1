# Probar estas propiedades de los df
df2 = df.drop_duplicates(['name']) #bota los duplicados de la columna name
df2 = df.drop(['job'], axis=1) #elimina la columna 'job' Si el valor del eje es 1 significa que queremos eliminar columnas, si el valor del eje es 0 o se deja en blanco significa que la fila se eliminará

frame_data = {'name': ['James', 'Jason', 'Rogers'], 'age': [18, 20, 22], 'job': ['Assistant', 'Manager', 'Clerk']}
df = pandas.DataFrame(frame_data, index = ['James', 'Jason', 'Rogers'])
df2 = df.drop(['Rogers']) #elimina la fila en que se encuentre 'Rogers' dentro de la columna indice, en esta base de datos se establecio que el index es la cokumna con los nombres, si no agregamos un index, pandas elaborará uno numerico y lo agregará como columna index
df2 = df.drop(df.index[[0, 1]]) #elimina un rango de filas

suma= df['A'].sum() # esto nos permite sumar los datos de la columna 'A'
valores_unicos =  df['A'].nunique() #cuenta los valores unicos
cantidad de datos = df['A'].count() # cuenta todos los valores de la columna 'A'
df[0:3] #selecciona las 3 primeras columnas