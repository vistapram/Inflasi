import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv('inflasi.csv', sep = ',')
content.head()
y_columns = ['Inflasi']
content.groupby(by=[content.Year]).sum().plot(kind='bar')
plt.title('Data Inflasi')
plt.ylabel('Inflasi')
plt.show()

