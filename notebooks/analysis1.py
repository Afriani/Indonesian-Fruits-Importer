import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.transform import dodge

# Calling DataFrame
df1 = pd.read_excel("C:\Users\Roy\Indonesian Fruits Importer\data\raw\Fruits Importing Kilos.xlsx")
df2 = pd.read_excel("C:\Users\Roy\Indonesian Fruits Importer\data\raw\Fruits Importing USD.xlsx")

# Merging df1 and df2
df_new = pd.merge(df1, df2, how = "inner", on = "Country Name")
df_new.head()

