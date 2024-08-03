import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = pd.read_csv("iris.csv")

#Write a Python program to create a plot to get a general Statistics of Iris data.

"""
iris.describe().plot(kind = "area",fontsize=16, figsize = (12,6), table = True, colormap="Accent")
plt.xlabel('Statistics',)
plt.ylabel('Value')
plt.title("General Statistics of Iris Dataset")
plt.show()
"""

#Write a Python program to create a Bar plot to get the frequency of the three species 
#of the Iris data.
