import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os
from EDA import create_directory

pio.renderers.default = 'browser'
plt.rcParams["figure.figsize"] = (15, 10)
plt.rcParams["hist.bins"] = 10

_HOME = os.getcwd()
global title_list
title_list = list()


def histogram(dataframe, xaxis, bins, title, xlabel, to_html=True):
    """
    This function generates an interactive histogram in HTML based on a dataframe and saves the plot in the same
    folder as the codes.
    :param dataframe: Pandas dataframe.
    :param xaxis: the column of the Pandas dataframe for
    which you want the histogram.
    :param bins: number of bins in the histogram.
    :param title: title of the histogram.
    :param xlabel: label of the x-axis of the histogram.
    :param to_html: DEFAULT: True. Saves the interactive plot in a .html format within the export/html folder.
    :return: figure.
    """
    create_directory('export/html')
    fig = px.histogram(dataframe, x=xaxis, nbins=bins, title=title, labels={'x_axis': xlabel},
                       color_discrete_sequence=['darkblue'])
    if to_html:
        _extension = 'plt_' + title + '.html'
        fig.write_html(os.path.join(_HOME, 'export', 'html', _extension), auto_open=False)
    else:
        fig.show()

    title_list.append(title)

    return fig


def lineplot(dataframe, xaxis, yaxis, title, xlabel, ylabel, hover_text, to_html=True):
    """
    This function generates an interactive line plot in HTML based on a dataframe.
    :param dataframe: Pandas dataframe.
    :param xaxis: the column of the Pandas dataframe for which you want the line plot's x-axis.
    :param yaxis: the column of the Pandas dataframe for which you want the line plot's y-axis.
    :param title: title of the line plot.
    :param xlabel: label of the x-axis of the line plot.
    :param ylabel: label of the y-axis of the line plot.
    :param to_html: DEFAULT: True. Saves the interactive plot in a .html format within the export/html folder.
    :param: hover_text: text to display when the user hovers over specific datapoints on the plot.
    :return: figure.
    """
    create_directory('export/html')
    fig = px.line(dataframe, x=xaxis, y=yaxis, title=title, labels=dict(x_axis=xlabel, y_axis=ylabel), color=hover_text)
    # fig = go.Figure()
    # fig.add_trace(
    #     go.Scatter(
    #         x=dataframe[x_axis],
    #         y=dataframe[y_axis],
    #         mode='lines',
    #         name=x_axis,
    #         line={'color': 'darkblue'}))
    # fig.add_annotation(text=hover_text)
    # fig.update_layout(
    #     title=title,
    #     xaxis_title=xlabel,
    #     yaxis_title=ylabel
    # )
    if to_html:
        _extension = 'plt_' + title + '.html'
        fig.write_html(os.path.join(_HOME, 'export', 'html', _extension), auto_open=False)
    else:
        fig.show()

    title_list.append(title)

    return fig


def barplot(dataframe, xaxis, yaxis, title, xlabel, ylabel, hover_text, barmode='stack', to_html=True):
    """
    This function generates an interactive barplot plot in HTML based on a dataframe.
    :param dataframe: Pandas dataframe.
    :param xaxis: the column of the Pandas dataframe for which you want the bar plot's x-axis.
    :param yaxis: the column of the Pandas dataframe for which you want the bar plot's y-axis.
    :param title: title of the bar plot.
    :param xlabel: label of the x-axis of the bar plot.
    :param ylabel: label of the y-axis of the bar plot.
    :param to_html: DEFAULT: True. Saves the interactive plot in a .html format within the export/html folder.
    :param: hover_text: text to display when the user hovers over specific datapoints on the plot.
    :param: barmode: DEFAULT: stack. The type of barplot the user requires. The user can choose between two options - 'stack' and 'group'.
    :return: figure.
    """
    create_directory('export/html')
    fig = px.bar(dataframe, x=xaxis, y=yaxis, title=title, labels=dict(x_axis=xlabel, y_axis=ylabel),
                 color=hover_text, barmode=barmode)
    fig.update(layout_coloraxis_showscale=False)
    # fig = go.Figure()
    # fig.add_trace(
    #     go.Bar(
    #         x=dataframe[xaxis],
    #         y=dataframe[yaxis],
    #         marker={'color': 'darkblue'},
    #         name=xlabel,
    #         color=hover_text
    #     ))
    # fig.update_layout(
    #     title=title,
    #     xaxis_title=xlabel,
    #     yaxis_title=ylabel
    # )
    if to_html:
        _extension = 'plt_' + title + '.html'
        fig.write_html(os.path.join(_HOME, 'export', 'html', _extension), auto_open=False)
    else:
        fig.show()

    title_list.append(title)

    return fig


def boxplot(dataframe, title, to_html=True, **kwargs):
    """
    This function generates an interactive box plot in HTML based on a dataframe.
    :param dataframe: Pandas dataframe.
    :param title: title of the box plot.
    :param to_html: DEFAULT: True. Saves the interactive plot in a .html format within the export/html folder.
    :return: figure.
    """
    create_directory('export/html')
    fig = go.Figure()
    fig.update_layout(
        title=title
    )
    for key, value in kwargs.items():
        fig.add_trace(go.Box(y=dataframe[value], name=key))
    if to_html:
        _extension = 'plt_' + title + '.html'
        fig.write_html(os.path.join(_HOME, 'export', 'html', _extension), auto_open=False)
    else:
        fig.show()

    title_list.append(title)

    return fig
