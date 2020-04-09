import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read csv into data variable 
data = pd.read_csv("C:\projects\Spring_2020\Capstone\section_word_statistics.csv")

# Drops all illegal values(NaN) from data
data.dropna(inplace = True)

# Drops all rows whos Word column does not contain the listed words,
data = data[data["Word"].isin(['Fire','Transformer'])]

# Set index(row labels) for the DataFrame in this case setting two labels
# The primary is the Section ID, secondary is the words in each section
#data = data.set_index(['Section_ID','Word']).Frequency

test = dict(tuple(data.groupby('Word')))

fireframe = pd.DataFrame(test['Fire'])
fireframe.name='Fire'
del fireframe['Word']
del fireframe['Index']

transformerframe = pd.DataFrame(test['Transformer'])
transformerframe.name='Transformer'
del transformerframe['Word']
del transformerframe['Index']

print(fireframe)
print(transformerframe)

xmax = fireframe['Section_ID'].max() if fireframe['Section_ID'].max() > transformerframe['Section_ID'].max() else transformerframe['Section_ID'].max()

ax = fireframe.plot(x='Section_ID',y='Frequency')
bx = transformerframe.plot(x='Section_ID',y='Frequency',ax=ax)
bx.legend(['Fire','Transformer'])
bx.set_xlim(1,xmax)

plt.show()