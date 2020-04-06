import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read csv into data variable 
data = pd.read_csv("C:\projects\Spring_2020\Capstone\document_word_statistics.csv")

# Drops all illegal values(NaN) from data
data.dropna(inplace = True)

# Drops all rows whos Word column does not contain the listed words,
data = data[data["Word"].isin(['Fire','insulation','Monitoring','Electrical','distance','system'])]

# Plot line graph using Word as x variable and Frequency as y variable 
data.plot(kind='line',x='Word',y='Frequency')

plt.show()