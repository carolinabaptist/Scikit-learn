import pandas as pd
#Write a Python program to load the iris data from a given csv file into 
#a dataframe and print the shape of the data, type of the data and first 3 rows.

"""
data = pd.read_csv("iris.csv")
print("Shape of the data:")
print(data.shape)
print("\nData Type:")
print(type(data))
print("\nFirst 3 rows:")
print(data.head(3))
"""

#Write a Python program using Scikit-learn to print the keys, number 
#of rows-columns, feature names and the description of the Iris data.

"""
iris_data = pd.read_csv("iris.csv")
print("\nKeys of Iris dataset:")
print(iris_data.keys())
print("\nNumber of rows and columns of Iris dataset:")
print(iris_data.shape) 
"""

#Write a Python program to get the number of observations, missing 
#values and nan values.

"""
iris = pd.read_csv("iris.csv")
print(iris.info())
"""

#Write a Python program to create a 2-D array with ones on the diagonal 
#and zeros elsewhere. Now convert the NumPy array to a SciPy sparse matrix in 
#CSR format.
import numpy as np
from scipy import sparse
"""
id_matrix = np.eye(3)
sparse_matrix = sparse.csr_matrix(id_matrix)
"""

#Write a Python program to view basic statistical details like percentile,
# mean, std etc. of iris data.

#standard deviation: indicates how spread out the values ​​in a data set are 
#relative to the set mean. A low standard deviation indicates that the values 
#​​tend to be close to the mean, while a high standard deviation 
#indicates that the values ​​are more spread out.

#percentile: indicates the value below which a certain percentage of observations 
#in a data set fall. Ex: 25th percentile (1st quartile): 25% of the data is below this value.
# 2nd quartile is the median
"""
df = pd.read_csv('iris.csv')
df.describe()
"""

#Write a Python program to get observations of each species 
# (setosa, versicolor, virginica) from iris data.

"""
data = pd.read_csv("iris.csv")
print("Observations of each species:")
print(data['variety'].value_counts()) 
"""

#Write a Python program to drop variety column from 
#a given Dataframe and print the modified part. 
# Call iris.csv to create the Dataframe.

"""
data = pd.read_csv("iris.csv")
df_new = data.drop(columns=['variety'])
print(df_new.head())
"""

#Write a Python program to access first four cells 
# from a given Dataframe using the index and column 
# labels. Call iris.csv to create the Dataframe.

"""
data = pd.read_csv("iris.csv")
print(data.iloc[:, [1, 2, 3, 4]].values)
"""
