import numpy as np
import pandas as pd
from pandas import ExcelFile

# Handle Input file:

excel_file = 'Input.xlsx'
Gdata = pd.read_excel(excel_file, sheet_name= 'Generadores')
Ddata = pd.read_excel(excel_file, sheet_name= 'Demandas')
Ldata = pd.read_excel(excel_file, sheet_name= 'Lineas')

Gdict = dict({'Generador': list(), 'Rendimiento': list(), 'Precio Combustible': list(), 'Potencia Maxima': list(), 'Ubicacion': list()})
for i in Gdict:
    for j in Gdata[i]:
        Gdict[i].append(j)

Ddict = dict({'t':list()})
for i in range(len(Ddata)-1):
    Ddict[str(i+1)] = list()
for i in Ddict:
    for j in Ddata[i]:
        Ddict[i].append(j)

Lmatrix = Ldata.as_matrix()

print(Gdict)
print(Ddict)
print(Lmatrix)

# Solve problem:
#Important notes:
'''
P = C => P = Pg - (Pg x pérdida_línea)
Sum(Ci) < Pmax Gi (Cuando sólo hay 1 generador tratando de suplir las demandas)


'''
