# list comprehension

digitos = [i for i in range(10)]
exponencial2 = [2**i for i in range(10)]
exponencial2_2 = [2**i for i in range(1, 10)]


# pandas
# cd ..
# cd <folder>
# ls
# columna Index

import pandas as pd
from pandas import ExcelWriter


d = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(data=d)

print(df)
print(df.head())
print(df.columns)



xl = pd.ExcelFile("Notorious_ordenes.xls")
xl.sheet_names
df = xl.parse("Orders")

print(df)
print(df.head())
print(df.columns)

df.iloc[2, 5]

df.loc[2, 'Producto']

df['Estado interno']

def tipos_de_estado(df):
    estados_internos = []
    for i in range(len(df)):
        if df.loc[i, 'Estado interno'] not in estados_internos:
            estados_internos.append(df.loc[i, 'Estado interno'])
        else:
            pass
    return estados_internos

tipos_de_estado = tipos_de_estado(df)

df['Estado interno'].values

df2 = df[df['Estado interno'] == 'problemas']



def generar_DF_Excel(df, nombre_archivo):
    nombre_final = nombre_archivo + '.xlsx' 
    writer = ExcelWriter(nombre_final)
    df.to_excel(writer,'Orders')
    writer.save()
    print('Ok')


generar_DF_Excel(df2, 'ordenes_problemas')
