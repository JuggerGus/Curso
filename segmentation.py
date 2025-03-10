# Library
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


"""
# Lectura de archivos

path_age="/Users/gusano2398gmail.com/Desktop/Internship/NeuroNexus/Neurodevelopment/genes_matrix_csv/"
rnaseq=pd.read_csv("BrainSpan.txt", delimiter="\t", index_col=0, header=None)

# Impresión de archivos

print("rnaseq")
#print(rnaseq)

#print("rnaseq Transpose \n")
rnaseq=rnaseq.transpose()
#print(rnaseq)


age=pd.read_csv(path_age+"columns_metadata.csv")
age=age["age"].tolist()
#print("\Age:\n",age,"\n")

rnaseq["Age"]= age
rnaseq.set_index(['gene_symbol'], inplace=True)


rnaseq.to_csv("BrainSpan.csv")
print(rnaseq)
"""




"""


rnaseq=pd.read_csv("BrainSpan.csv")
print("Base de datos \n")
print(rnaseq)

ages = ["11 yrs", "40 yrs"]


# Filter the DataFrame
filtered_df = rnaseq[rnaseq["Age"].isin(ages)]
filtered_df=filtered_df.drop("Age", axis=1)
# Display the result

filtered_df=filtered_df.set_index(["gene_symbol"])

print("Base de datos co Indice\n")
print(filtered_df)

filtered_df.to_csv("filtered_df.csv")

"""


"""
rnaseq=pd.read_csv("filtered_df.csv", header=None)
print("Base de datos \n")
print(rnaseq)

np.savetxt("Brain_Bulk.txt",rnaseq, fmt='%s', delimiter='\t')


"""


