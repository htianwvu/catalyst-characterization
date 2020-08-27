import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information, changable
sample_name = 'standard CuO'

XRD = pd.read_excel(r"C:/Users/htian/Desktop/book in reading/python littlefly learning/CuO XRDStandard.xls", 
                   sheet_name='CuO Std Data')

print(XRD,'\n')



#########################################
##########process data##########

# dropna all unnecessary data in columns######
##Raman2 = Raman.dropna(axis =1)
##print(Raman2)

plt.figure(figsize=(20,8),dpi=400)

################################
##########Change the name of first line #########
XRD.columns= ['2 Delta','position','Relative Intensity (a.u)']

# check the first and last five lines###
XRD

## Plot the Spectra and add all labels###

XRD.plot(kind = "line", x = '2 Delta', y='Relative Intensity (a.u)',
                 linewidth=1, alpha=0.8,color = 'b')

plt.title("X-Ray Diffraction" + sample_name)
plt.legend(labels= [sample_name], loc='best',fontsize=8)
plt.xlabel('2 Delta', fontsize=10)
plt.ylabel('Relative Intensity (a.u.)',fontsize=10)


plt.show()
