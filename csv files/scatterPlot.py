import pandas as pd
import plotly.express as px

readFile=pd.read_csv("data.csv")
fig = px.scatter(readFile, x="Population", y="Per capita", size="Percentage",color="Country", size_max=60)
fig.show()