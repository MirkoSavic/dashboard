import os
import pandas as pd
import plotly.express as px
import numpy as np
from dash import Dash, dcc, html

np.random.seed(42)
data = pd.DataFrame({
    'month': pd.date_range('2023-01', periods=12, freq='M'),
    'sales': np.random.normal(50000, 10000, 12),
    'marketing_spend': np.random.normal(5000, 1000, 12),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 12)
})
data['profit_margin'] = (data['sales'] - data['marketing_spend']) / data['sales']

fig1 = px.line(data, x='month', y='sales', title='Sales Trend Analysis', markers=True)
fig2 = px.scatter(data, x='marketing_spend', y='sales', title='Marketing ROI Analysis', trendline='ols')
fig3 = px.histogram(data, x='profit_margin', nbins=8, title='Profit Margin Distribution')
fig4 = px.box(data, x='region', y='sales', title='Sales Performance by Region')

app = Dash(__name__)
server = app.server  # expose Flask server for WSGI (gunicorn)

app.layout = html.Div([
    html.H1("Sales Performance Statistical Dashboard",
            style={'textAlign': 'center', 'marginBottom': 30}),
    html.Div([
        html.Div([dcc.Graph(figure=fig1)],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=fig2)],
                 style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ], style={'marginBottom': 20}),
    html.Div([
        html.Div([dcc.Graph(figure=fig3)],
                 style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=fig4)],
                 style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ])
])

if __name__ == '__main__':
    # dev server (not for production)
    port = int(os.environ.get("PORT", 8050))
    app.run(host='0.0.0.0', port=port, debug=False)