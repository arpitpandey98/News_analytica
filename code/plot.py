import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px


def plot(df, xcol, ycol):
    graph = px.bar(
    df, 
    x=xcol,
    y=ycol,
    # labels={'Number of cases'},
    color=xcol)

    return graph