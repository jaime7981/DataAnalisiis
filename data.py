import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_excel("BASEFUGA2020_F.xls")

cuantitative = ['EDAD', 'M_MOROSO', 'MONTO']

qualitative = ['NIV_EDUC', 'E_CIVIL', 'CIUDAD', 'SEGURO', 'FUGA']

months = ["D_Marzo", 'D_Abril', 'D_Mayo', 'D_Junio', 'D_Julio', 'D_Agosto', 'D_Septiembre']

'''
ds = dataset[dataset['EDAD'].notna()]
plt.plot(ds['EDAD'])
plt.show()
'''

for headname in dataset.head():
    if (headname in cuantitative):
        print("\n" + headname)

        ds = dataset[dataset[headname].notna()]
        print(ds[headname].describe())
        plt.plot(ds[headname])
        plt.show()

'''
for headname in dataset.head():
    if (headname in cuantitative):
        print("\n" + headname)
        print(dataset[headname].describe())
        plt.xticks(dataset[headname].notna())
        plt.show()
'''

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

for quality in qualitative_ploting:
    print(quality)
    plt.bar(quality.keys(), quality.values())
    plt.show()