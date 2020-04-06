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
data = data.set_index(['Section_ID','Word']).Frequency

# Plot bar graph of data
data.unstack().plot(kind='bar')

plt.show()