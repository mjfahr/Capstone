import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read csv into data variable 
data = pd.read_csv(r"C:\Users\miser\Documents\GitHub\Capstone\csv\section_word_statistics.csv")

# Drops all illegal values(NaN) from data
data.dropna(inplace = True)

# Drops all rows whos Word column does not contain Fire,
# Could use a list of multiple words instead of just Fire
data = data[data["Word"].isin(['Fire'])]

# Print dataset in console
print(data)

# Plot bar graph with Section_ID column as x and Frequency column as y
data.plot.bar(x='Section_ID',y='Frequency',rot=0)

# Display plotted graph
plt.show()