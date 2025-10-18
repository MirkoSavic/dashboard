!pip install dash plotly pandas numpy

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

# Overview: Time series shows temporal patterns
fig1 = px.line(data, x='month', y='sales', 
               title='Sales Trend Analysis',
               markers=True)

# Relationship: Correlation analysis reveals dependencies 
fig2 = px.scatter(data, x='marketing_spend', y='sales',
                  title='Marketing ROI Analysis',
                  trendline='ols')

# Distribution: Shows data shape and outliers
fig3 = px.histogram(data, x='profit_margin', nbins=8,
                    title='Profit Margin Distribution')

# Comparison: Group analysis reveals differences
fig4 = px.box(data, x='region', y='sales',
              title='Sales Performance by Region')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Performance Statistical Dashboard", 
            style={'textAlign': 'center', 'marginBottom': 30}),
    
    # Primary analysis row: Overview charts
    html.Div([
        html.Div([dcc.Graph(figure=fig1)], 
                style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=fig2)], 
                style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ], style={'marginBottom': 20}),
    
    # Secondary analysis row: Detail charts 
    html.Div([
        html.Div([dcc.Graph(figure=fig3)], 
                style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=fig4)], 
                style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ])
])

if __name__ == '__main__':
    app.run(debug=True)

