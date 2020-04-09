import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read csv into data variable 
data = pd.read_csv("C:\projects\Spring_2020\Capstone\section_total_word_count.csv")

#dx = data.plot(x='Section_Index',y='Total_Word_Count',xticks=data['Section_Index'])
dx = data.plot(x='Section_Index',y='Total_Word_Count')
dx.set_xlim(1,data['Section_Index'].max())
plt.show()