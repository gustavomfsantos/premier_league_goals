
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots





def plot_simu(df, filter_column, category_column_pie1, category_column_pie2):
    def generate_pieplot(ins):
        fig = make_subplots(rows=1, cols=2,
                            subplot_titles=(f"Goals per {category_column_pie1}", f"Goals per {category_column_pie2}"),
                            specs=[[{"type": "bar"}, {"type": "bar"}]])


        fig.add_trace(go.Bar(x=(df[df[filter_column] == ins][category_column_pie1]),
                             y=(df[df[filter_column] == ins]['Goals']),
                            showlegend=False, marker_color = 'steelblue',
                             ),

                      row=1, col=1)

        fig.add_trace(go.Scatter(
            x=df[df[filter_column] == ins].groupby(['Player Nationality'])['Goals'].sum().index,
            y=df[df[filter_column] == ins].groupby(['Player Nationality'])['Goals'].sum(),
            text=df[df[filter_column] == ins].groupby(['Player Nationality'])['Goals'].sum(),
            mode='text',
            textposition='top center',
            textfont=dict(
                size=18,
            ),
            showlegend=False
        ), row=1, col=1)

        fig.add_trace(go.Bar(x=(df[df[filter_column] == ins][category_column_pie2]),
                             y=df[df[filter_column] == ins]['Goals'],
                                    marker_color = 'firebrick',
                             showlegend=False,
                             ),
                      row=1, col=2)
        return fig

    uplist1 = df[filter_column].unique()
    uplist2 = [generate_pieplot(ins) for ins in uplist1]

    # Dropdown: Implementation
    upfilter = [{'method': 'animate', 'label': i1, 'args': [i2]} for i1, i2 in zip(uplist1, uplist2)]
    updatemenus = [{'buttons': upfilter}]

    # Initial barchart
    fig = go.Figure(uplist2[0])

    # Add dropdown
    fig.update_layout(updatemenus=updatemenus, title_text="Top Scorers Analysis")

    # Result
    fig.show()


def pieplot_2(df, filter_column, value_columns, category_column):
    def generate_pieplot(ins):
        fig = px.pie(df[df[filter_column] == ins], values=value_columns, names=category_column,
                     title=f'Goals per {category_column} per Season', color=category_column, hole=0.4,
                     template='plotly_dark')
        return fig

    # Dropdown: Content
    uplist1 = df[filter_column].unique()
    uplist2 = [generate_pieplot(ins) for ins in uplist1]

    # Dropdown: Implementation
    upfilter = [{'method': 'animate', 'label': i1, 'args': [i2]} for i1, i2 in zip(uplist1, uplist2)]
    updatemenus = [{'buttons': upfilter}]

    # Initial barchart
    fig = go.Figure(uplist2[0])

    # Add dropdown
    fig.update_layout(updatemenus=updatemenus, title_text="Club Total Goals")

    # Result
    fig.show()
    return 'plot done'
