# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:32:25 2019

@author: k.sandhu
"""
import os
os.getcwd()
os.chdir('C:\\Users\\k.sandhu\\Desktop\\Python')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
cols=[]
data = pd.read_csv('Madsen.csv', header = 0)
#append column names in cols list
for col in data.columns: 
    cols.append(col)
#ignoring 1,2 and 3rd column
columns=cols[3:]
#make a list of values for DAWS (1st row)
list1=data.iloc[1,3:].tolist()
for i in range(0, len(list1)): 
    list1[i] = float(list1[i])
#list2 contains intergers upto the number of columns
list2=[]
for i in range(0,20):
    list2.append(i)
#barplot
plt.bar(list2,list1,color = ['gray','gray','gray','red','gray','gray','red','gray','red','red','gray','gray','red','red','gray','gray','red','red','gray','gray'])
#making the labels vertical
plt.xticks(list2,columns, rotation='vertical')
#adding legends for each color
red_patch = mpatches.Patch(color='red', label='Madsen')
gray_patch = mpatches.Patch(color='gray', label='DAWS')
plt.legend(handles=[red_patch,gray_patch], loc='upper left')
#lables and titile for plot
plt.xlabel('Traits', fontsize=16)
plt.ylabel('t-score', fontsize=16)
plt.title('Comparison between DAWS and Madsen',fontsize=16)
plt.savefig('DAWSvsMadsen.png')






import os
os.getcwd()
os.chdir('C:\\Users\\k.sandhu\\Desktop\\Python')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
cols=[]
data = pd.read_csv('Madsen.csv', header = 0)
#append column names in cols list
for col in data.columns: 
    cols.append(col)
#ignoring 1,2 and 3rd column
columns=cols[3:]
#make a list of values for DAWS (1st row)
list1=data.iloc[1,3:].tolist()
for i in range(0, len(list1)): 
    list1[i] = float(list1[i])
#list2 contains intergers upto the number of columns
list2=[]
for i in range(0,20):
    list2.append(i)
#barplot
plt.bar(list2,list1,color = ['gray','red','red','red','red','gray','red','red','gray','red','red','gray','red','gray','gray','gray','red','red','red','gray'])
#making the labels vertical
plt.xticks(list2,columns, rotation='vertical')
#adding legends for each color
red_patch = mpatches.Patch(color='red', label='Madsen')
gray_patch = mpatches.Patch(color='gray', label='LEWJAIN')
plt.legend(handles=[red_patch,gray_patch], loc='upper left')
#lables and titile for plot
plt.xlabel('Traits', fontsize=16)
plt.ylabel('t-score', fontsize=16)
plt.title('Comparison between LEWJAIN and MADSEN',fontsize=16)
plt.savefig('LEWJAINvsMadsen.png')




import os
os.getcwd()
os.chdir('C:\\Users\\k.sandhu\\Desktop\\Python')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
cols=[]
data = pd.read_csv('Madsen.csv', header = 0)
#append column names in cols list
for col in data.columns: 
    cols.append(col)
#ignoring 1,2 and 3rd column
columns=cols[3:]
#make a list of values for DAWS (1st row)
list1=data.iloc[2,3:].tolist()
for i in range(0, len(list1)): 
    list1[i] = float(list1[i])
#list2 contains intergers upto the number of columns
list2=[]
for i in range(0,20):
    list2.append(i)
#barplot
plt.bar(list2,list1,color = ['red','gray','red','red','gray','red','red','red','red','red','gray','red','red','gray','gray','gray','red','red','gray','red'])
#making the labels vertical
plt.xticks(list2,columns, rotation='vertical')
#adding legends for each color
red_patch = mpatches.Patch(color='red', label='Madsen')
gray_patch = mpatches.Patch(color='gray', label='ORCF102')
plt.legend(handles=[red_patch,gray_patch], loc='upper left')
#lables and titile for plot
plt.xlabel('Traits', fontsize=16)
plt.ylabel('t-score', fontsize=16)
plt.title('Comparison between ORCF102 and MADSEN',fontsize=16)
plt.savefig('ORCF102vsMadsen.png')



import os
os.getcwd()
os.chdir('C:\\Users\\k.sandhu\\Desktop\\Python')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
cols=[]
data = pd.read_csv('Madsen.csv', header = 0)
#append column names in cols list
for col in data.columns: 
    cols.append(col)
#ignoring 1,2 and 3rd column
columns=cols[4:]
#make a list of values for DAWS (1st row)
list1=data.iloc[3,3:].tolist()
for i in range(0, len(list1)): 
    list1[i] = float(list1[i])
#list2 contains intergers upto the number of columns
list2=[]
for i in range(0,20):
    list2.append(i)
#barplot
plt.bar(list2,list1,color = ['gray','gray','red','red','red','gray','gray','red','gray','red','gray','gray','red','gray','gray','red','red','red','red','red'])
#making the labels vertical
plt.xticks(list2,columns, rotation='vertical')
#adding legends for each color
red_patch = mpatches.Patch(color='red', label='Madsen')
gray_patch = mpatches.Patch(color='gray', label='PUMA')
plt.legend(handles=[red_patch,gray_patch], loc='upper left')
#lables and titile for plot
plt.xlabel('Traits', fontsize=16)
plt.ylabel('t-score', fontsize=16)
plt.title('Comparison between PUMA and MADSEN',fontsize=16)
plt.savefig('PUMAvsMadsen.png')




import os
os.getcwd()
os.chdir('C:\\Users\\k.sandhu\\Desktop\\Python')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
cols=[]
data = pd.read_csv('Madsen.csv', header = 0)
#append column names in cols list
for col in data.columns: 
    cols.append(col)
#ignoring 1,2 and 3rd column
columns=cols[4:]
#make a list of values for DAWS (1st row)
list1=data.iloc[4,3:].tolist()
for i in range(0, len(list1)): 
    list1[i] = float(list1[i])
#list2 contains intergers upto the number of columns
list2=[]
for i in range(0,20):
    list2.append(i)
#barplot
plt.bar(list2,list1,color = ['red','red','red','red','gray','red','red','red','gray','red','gray','gray','red','gray','red','gray','red','red','red','red'])
#making the labels vertical
plt.xticks(list2,columns, rotation='vertical')
#adding legends for each color
red_patch = mpatches.Patch(color='red', label='Madsen')
gray_patch = mpatches.Patch(color='gray', label='STEPHENS')
plt.legend(handles=[red_patch,gray_patch], loc='upper left')
#lables and titile for plot
plt.xlabel('Traits', fontsize=16)
plt.ylabel('t-score', fontsize=16)
plt.title('Comparison between STEPHENS and MADSEN',fontsize=16)
plt.savefig('STEPHENSvsMadsen.png')


import os
os.getcwd()
os.chdir('C:\\Users\\k.sandhu\\Desktop\\Python')
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
cols=[]
data = pd.read_csv('Madsen.csv', header = 0)
#append column names in cols list
for col in data.columns: 
    cols.append(col)
#ignoring 1,2 and 3rd column
columns=cols[4:]
#make a list of values for DAWS (1st row)
list1=data.iloc[5,3:].tolist()
for i in range(0, len(list1)): 
    list1[i] = float(list1[i])
#list2 contains intergers upto the number of columns
list2=[]
for i in range(0,20):
    list2.append(i)
#barplot
plt.bar(list2,list1,color = ['red','red','red','gray','gray','red','red','red','red','red','gray','gray','red','red','gray','gray','red','gray','gray','red'])
#making the labels vertical
plt.xticks(list2,columns, rotation='vertical')
#adding legends for each color
red_patch = mpatches.Patch(color='red', label='Madsen')
gray_patch = mpatches.Patch(color='gray', label='TUBBS06')
plt.legend(handles=[red_patch,gray_patch], loc='upper left')
#lables and titile for plot
plt.xlabel('Traits', fontsize=16)
plt.ylabel('t-score', fontsize=16)
plt.title('Comparison between TUBBS06 and MADSEN',fontsize=16)
plt.savefig('TUBBS06vsMadsen.png')