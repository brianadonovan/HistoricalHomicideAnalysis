import plotly
import plotly.graph_objs as go


class Grapher:

    def __init__(self):
        pass

    def bar_graph(self, x_values, y_values, title):
        plotly.offline.plot({
            "data": [go.Bar(x=x_values, y=y_values)],
            "layout": go.Layout(title=title)
        }, auto_open=True)

    def scatter_plot(self, x_values, y_values, title):
        plotly.offline.plot({
            "data": [go.Scatter(x=x_values, y=y_values)],
            "layout": go.Layout(title=title)
        }, auto_open=True)

    def stack_bar(self, x_values, y_values, names, title):
        data = []
        for weapon in names:
            trace = go.Bar(
                x=x_values[weapon],
                y=y_values[weapon],
                name=weapon
            )
            data.append(trace)

        layout = go.Layout(
            barmode='stack',
            title=title
        )
        fig = go.Figure(data=data, layout=layout)

        plotly.offline.plot(fig, auto_open=True)
        return data

