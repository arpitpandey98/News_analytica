import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px

def linePlot(data):



    layout = go.Layout(
        title= "<b>Revenue and cost of Tiki, Sendo & Shopee</b>",
        paper_bgcolor = 'rgb(248, 248, 255)',
        plot_bgcolor = 'rgb(248, 248, 255)',
        barmode = "stack"
        )

    data = []
    line_chart= go.Scatter(x=[1, 2, 3, 4],y=[5, 6, 7, 8], xaxis="x2", yaxis="y2", showlegend=False)
    data.append(line_chart)
    fig= go.Figure(data=data, layout=layout)
    return fig