import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_excel("BASEFUGA2020_F.xls")

cuantitative = ['EDAD', 'M_MOROSO', 'MONTO']

qualitative = ['NIV_EDUC', 'E_CIVIL', 'CIUDAD', 'SEGURO', 'FUGA']

months = ["D_Marzo", 'D_Abril', 'D_Mayo', 'D_Junio', 'D_Julio', 'D_Agosto', 'D_Septiembre']

#Data Cleaning
cuantitative_ds = dataset

for headname in dataset.head():
    if (headname in cuantitative):
        cuantitative_ds = cuantitative_ds[cuantitative_ds[headname].notna()]

cuantitative_ds = cuantitative_ds[cuantitative_ds['EDAD'] > 0]
cuantitative_ds = cuantitative_ds[cuantitative_ds['EDAD'] < 80]
#END Data Cleaning

#Cuantitative Graphs
plt.scatter(x=cuantitative_ds['MONTO'], y=cuantitative_ds['EDAD'])
plt.show()
plt.scatter(x=cuantitative_ds['MONTO'], y=cuantitative_ds['M_MOROSO'])
plt.show()
plt.scatter(x=cuantitative_ds['EDAD'], y=cuantitative_ds['M_MOROSO'])
plt.show()

for headname in dataset.head():
    if (headname in cuantitative):
        print("\n" + headname)
        print(cuantitative_ds[headname].describe())
        if (headname=='EDAD'):
            plt.hist(cuantitative_ds[headname], bins=80, range=(0,80))
        else:
            plt.hist(cuantitative_ds[headname], bins=50)
        plt.show()

#Cualitative data into dicts
qualitative_ploting = []

for headname in dataset.head():
    if (headname in qualitative):
        aux_dic = {}
        for qualitative_data in dataset[headname]:
            if (qualitative_data not in aux_dic):
                if (qualitative_data is not np.nan):
                    aux_dic[qualitative_data] = 0
            else:
                aux_dic[qualitative_data] += 1
        qualitative_ploting.append(aux_dic)

#print(list(qualitative_ploting[0].keys()))
#print(list(qualitative_ploting[0].values()))

#Cualitative Plots
for quality in qualitative_ploting:
    print(quality)
    plt.bar(quality.keys(), quality.values())
    #plt.pie(x=quality.values(), labels=quality.keys())
    plt.show()