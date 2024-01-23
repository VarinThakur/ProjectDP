import panel as pn
import pandas as pd
from .object import *

def app(doc):
    df = pd.read_csv('D:/CodingAndDevelopment/PycharmProjects/DjangoPanel2/ProjectDP/test_dataset.csv')
    # pn.extension('Plotly')
    fig = make_grouped_plot(df)
    # print(fig)
    plotly_pane = pn.pane.Plotly(fig)
    plotly_pane.server_doc(doc)