import pandas as pd 
import statistics
import plotly.express as px 

#Uploding the csv 
from google.colab import files
data_to_load = files.upload()

#Poltting the graph
df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df, y="quant_saved", color=rem rem_any)
fig.show()
