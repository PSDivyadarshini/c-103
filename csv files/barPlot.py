import pandas as pd
import plotly.express as px

readFile=pd.read_csv("data.csv")
fig=px.bar(readFile,x='Country',y='InternetUsers')
fig.show()