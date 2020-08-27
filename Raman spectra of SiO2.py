import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data

Raman = pd.read_csv(r'C:/Users/htian/Desktop/book in reading/Standard SiO2 sample.csv')
print(Raman.info(),'n')
print(Raman)


#########################################
##########process data##########

# dropna all unnecessary data in columns######
Raman2 = Raman.dropna(axis =1)
print(Raman2)

plt.figure(figsize=(20,8),dpi=400)

################################
##########Change the name of first line #########
Raman2.columns= ['Raman shift','Relative Intensity (a.u)']
print(Raman2)

## Plot the Spectra and add all labels###

Raman2.plot(kind = "line", x = 'Raman shift', y='Relative Intensity (a.u)',
                 linewidth=1, alpha=0.8,color = 'r')

plt.title("Visible (532nm) Raman Calibration")
plt.legend(labels=['Standard Raman Spectra of SiO2'],loc='best',fontsize=8)
plt.xlabel('Raman shift(cm-1)', fontsize=10)
plt.ylabel('Relative Intensity (a.u.)',fontsize=10)


plt.show()
