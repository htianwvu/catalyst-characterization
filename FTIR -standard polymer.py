import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##################################
###Import original data
###Basic sample information
FTIR = pd.read_csv(r'C:/Users/htian/Desktop/book in reading/WVU Share facility data/FTIR data1.csv')

###### to read full table information
print(FTIR)
print(FTIR.info(),'n')

######## very carefully read full list of first few lines#####
##### to identify the data your collected######
print(FTIR.loc[0])
print(FTIR.loc[1])
print(FTIR.loc[0:1])   ## see the unit corresponding relationship


### Identify key parmeters

sample_name = "Standard polymer"
ramping_rate = "RT"
wavenumber_label_unit = "cm-1"
Absorbance_Unit = " a.u."
Weigt_uni = 'mg'

# drop the first few lines , which is the 3 line##
FTIR2 = FTIR.drop([0,1,2,3])
print(FTIR2)

### reindix from beginning###

FTIR3 = FTIR2.reset_index(drop = True)

print(FTIR3)

### rename the columns###

FTIR3.columns= ['Wavenumbers','Absorbance']

print(FTIR3)

### change from "object" to "float" type, this is critical

FTIR3[['Wavenumbers','Absorbance']] = FTIR3[['Wavenumbers','Absorbance']].astype(float)

###

plt.figure(figsize=(20,8),dpi=400)



###### Plot the Spectra and add all labels###

x= FTIR3['Wavenumbers']
y= FTIR3['Absorbance']

print(y)
####y2 = TGA_CLC3['Temperature']

##ax1.plot(x,y1,'b-')

#FTIR3.plot(x,y, color = 'b')

FTIR3.plot(kind = "line", x = 'Wavenumbers', y='Absorbance',
               linewidth=1, alpha=0.8,color = 'b')       

plt.title("FTIR of " + sample_name)
plt.legend(labels= [sample_name], loc='best',fontsize=8)
plt.xlabel('Wavenumbers cm-1', fontsize=10)
plt.ylabel('Absorbance (a.u.)',fontsize=10)


plt.show()


