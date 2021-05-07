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

def plotBar(df, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    fig.add_trace( go.Bar(x = df.index,y= df.values.flatten()))
    return fig

def plotGroupedBar(datapoints , categories, title, xlabel, ylabel, colors = ['indianred', 'lightsalmon']):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)

    for category, point, color in zip(categories, datapoints, colors):
        fig.add_trace( go.Bar(x = point.index,y= point.values.flatten(), name = category, marker_color = color))
        
    return fig