import plotly.graph_objects as go

def risk_gauge(risk_score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={'text': "Risk Level"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "crimson"},
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "red"}
            ]
        }
    ))

    return fig


def growth_meter(growth):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=growth,
        title={'text': "Growth Potential"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "cyan"},
            'steps': [
                {'range': [0, 40], 'color': "#ef4444"},
                {'range': [40, 70], 'color': "#facc15"},
                {'range': [70, 100], 'color': "#22c55e"}
            ]
        }
    ))

    return fig


def scenario_bar(a, b):

    fig = go.Figure(data=[
        go.Bar(name='Scenario A', x=['Sales'], y=[a]),
        go.Bar(name='Scenario B', x=['Sales'], y=[b])
    ])

    fig.update_layout(
        title="Scenario Comparison",
        barmode='group'
    )

    return fig