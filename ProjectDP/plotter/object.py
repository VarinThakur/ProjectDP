import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

def make_grouped_plot(df):
    
    #create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    #with plotly.go, each trace needs to be added into the figure separately
    fig.add_trace(go.Bar(x=df['X'], y=df['Y1'], name='Y1' ,marker_color = '#43B02A',offsetgroup=1 ,), secondary_y=False)
    fig.add_trace(go.Bar(x=df['X'], y=df['Y2'], name='Y2' ,marker_color = '#00A3E0',offsetgroup=2 ,hovertemplate = '%{y:$,.0f}'), secondary_y=True)
    #change layout preferences
    fig.update_layout(
    barmode='group',
    font_size = 14,
    hovermode="x unified",
    )
    
    #set y-axes titles
    fig.update_yaxes(title_text="Y1 Title", secondary_y=True)
    fig.update_yaxes(title_text="Y2 Title", secondary_y=False)
    return fig