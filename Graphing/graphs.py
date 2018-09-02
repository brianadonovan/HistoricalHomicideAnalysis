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

    def stack_bar(self, x_values, y_values, names, graph_format):
        data = []
        for name in names:
            trace = go.Bar(
                x=x_values[name],
                y=y_values[name],
                name=name
            )
            data.append(trace)

        layout = go.Layout(
            barmode='stack',
            title=graph_format['title'],
            xaxis = dict(
                title=graph_format['x_axis'],
                titlefont=dict(
                    family='Arial, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            ),
            yaxis = dict(
                title=graph_format['y_axis'],
                titlefont=dict(
                    family='Arial, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
            )
        fig = go.Figure(data=data, layout=layout)

        return plotly.offline.plot(fig, include_plotlyjs=True, output_type='div')

    def pie_chart(self, incidents, states, title):
        fig = {
          "data": [
            {
              "values": incidents['No'],
              "labels": states['No'],
              "domain": {"x": [0, .48]},
              "name": "Unsolved",
              "text": ["Unsolved"],
              "textposition": "inside",
              "hoverinfo":"label+percent+name",
              "hole": .4,
              "type": "pie"
            },
            {
              "values": incidents['Yes'],
              "labels": states['Yes'],
              "text":["Solved"],
              "textposition":"inside",
              "domain": {"x": [.52, 1]},
              "name": "Solved",
              "hoverinfo":"label+percent+name",
              "hole": .4,
              "type": "pie"
            }],
          "layout": {
                "title":"Solved or Unsolved Homicides by State",
                "annotations": [
                    {
                        "font": {
                            "size": 20
                        },
                        "showarrow": False,
                        "text": "Unsolved",
                        "x": 0.20,
                        "y": 0.5
                    },
                    {
                        "font": {
                            "size": 20
                        },
                        "showarrow": False,
                        "text": "Solved",
                        "x": 0.78,
                        "y": 0.5
                    }
                ]
            }
        }
        #fig = go.Figure(data=data, layout=layout)

        plotly.offline.plot(fig, auto_open=True)
        return fig