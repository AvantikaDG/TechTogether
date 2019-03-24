# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:47:57 2019

@author: AvantikaDG
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\AvantikaDG\Desktop\Wage Gap\genderpaygay1718.csv")

l = list()
comm = list()
for index, row in df.iterrows():
    for col in df.columns:
        l.append(len(str(row[col])))
    comm.append(len(row))
print(max(l))
print("Min ",min(comm), "Max ", max(comm))

gpg1718 = pd.read_csv(r"C:\Users\AvantikaDG\Desktop\Wage Gap\output.csv")
gpg1819 = pd.read_csv(r"C:\Users\AvantikaDG\Desktop\Wage Gap\genderpaygap1819.csv")
bonusdiff1718 = gpg1718.MaleBonusPercent - gpg1718.FemaleBonusPercent
bonusdiff1819 = gpg1819.MaleBonusPercent - gpg1819.FemaleBonusPercent
colors = ["red"]* len(bonusdiff1718)
colors.extend(["blue"]* len(bonusdiff1819))
a = range(0,len(bonusdiff1718))
plt.scatter(list(a), bonusdiff1718, c = "red")
a = range(0,len(bonusdiff1819))
plt.scatter(list(a), bonusdiff1819, c = "blue")
plt.show()


df = pd.read_csv(r"C:\Users\AvantikaDG\Desktop\Wage Gap\genderpaygap1819.csv")
df.Address = df.Address.str.replace("\r\n", " ")
df.SicCodes = df.SicCodes.str.replace(",\r\n", " ")
df.EmployerName = df.EmployerName.str.replace(",", " ")
df.Address = df.Address.str.replace(",", " ")
df.SicCodes = df.SicCodes.str.replace(",", " ")
df.ResponsiblePerson = df.ResponsiblePerson.str.replace(",", " ")
df.EmployerSize = df.EmployerSize.str.replace(",", " ")
df.CurrentName = df.CurrentName.str.replace(",", " ")

df.to_csv(r"C:\Users\AvantikaDG\Desktop\Wage Gap\wagegap1819.csv", index = False)
