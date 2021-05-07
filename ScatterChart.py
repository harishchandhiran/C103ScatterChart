import pandas as pd
import plotly.express as px

data = pd.read_csv("data.csv")
fig = px.scatter(data,
    x="date",
    y="cases",
    color="country",
    size="cases",
    size_max=15,
    title="Daily Covid Cases")
fig.show()