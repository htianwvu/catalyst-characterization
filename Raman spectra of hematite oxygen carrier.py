import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
Raman = pd.read_csv(r'C:/Users/htian/Desktop/book in reading/Hermatite_3.csv')
sample_name = "Hematite"

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
                 linewidth=1, alpha=0.8,color = 'BLK')

plt.title("Raman Spectra of" + sample_name)
plt.legend(labels= [sample_name], loc='best',fontsize=8)
plt.xlabel('Raman shift(cm-1)', fontsize=10)
plt.ylabel('Relative Intensity (a.u.)',fontsize=10)


plt.show()
