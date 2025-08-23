import dash
from dash import html, dcc, Output, Input, State
import plotly.express as px
import pandas as pd
import base64, io

app = dash.Dash(__name__)
app.title = "Daily Vs Monthly Sales Dashboard"

app.layout = html.Div(style={'padding': '20px', 'backgroundColor': '#f4f6f8'}, children=[
    html.Div("📊 DAILY VS MONTHLY SALES DASHBOARD", 
             style={'textAlign': 'center', 'fontSize': '30px', 
                    'fontWeight': 'bold', 'color': '#333', 'marginBottom': '20px'}),

    dcc.Upload(
        id='upload-data',
        children=html.Div('Drag & Drop or Select CSV/Excel (auto-detects Date & Sales)'),
        style={
            'width': '100%', 'height': '50px', 'lineHeight': '50px',
            'borderWidth': '1px', 'borderStyle': 'dashed',
            'borderRadius': '5px', 'textAlign': 'center',
            'marginBottom': '20px', 'backgroundColor': '#fff'
        },
        multiple=False
    ),
    
    html.Div(id='file-info', style={'textAlign': 'center', 'marginBottom': '20px', 'color': '#555'}),

    html.Div(id='dashboard-content')
])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return None
    except Exception as e:
        print(e)
        return None
    return df

@app.callback(
    [Output('file-info', 'children'),
     Output('dashboard-content', 'children')],
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_dashboard(contents, filename):
    if contents is None:
        return "", ""

    df = parse_contents(contents, filename)
    if df is None:
        return "❌ Unsupported file format.", ""

    if 'Month' not in df.columns:
        if 'Date' in df.columns:
            df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%B')

    if 'DailyTotal' not in df.columns:
        df['DailyTotal'] = df['Sales']  

    total_sales = df['Sales'].sum()
    avg_daily_sales = df['DailyTotal'].mean()
    best_month = df.loc[df['Sales'].idxmax(), 'Month']

    fig_monthly = px.bar(df, x='Month', y=['Sales', 'DailyTotal'], barmode='group',
                         title="Daily vs Monthly Sales",
                         color_discrete_sequence=px.colors.qualitative.Set2)
    fig_monthly.update_layout(plot_bgcolor='white', paper_bgcolor='white')

    fig_daily_trend = px.line(df, x='Month', y='Sales', markers=True,
                              title="Daily Sales Trend", color_discrete_sequence=['#1f77b4'])
    fig_daily_trend.update_layout(plot_bgcolor='white', paper_bgcolor='white')

    fig_monthly_summary = px.bar(df, x='Month', y='DailyTotal',
                                 title="Monthly Sales Summary",
                                 color_discrete_sequence=['#2ca02c'])
    fig_monthly_summary.update_layout(plot_bgcolor='white', paper_bgcolor='white')

    fig_pie = px.pie(df, names='Month', values='Sales', title="Sales Share by Month",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    
    fig_scatter = px.scatter(df, x='Month', y='Sales', size='Sales',
                             title="Sales Distribution by Month",
                             color='Sales', color_continuous_scale='Viridis')

    dashboard = html.Div([
        html.Div(style={'display': 'flex', 'gap': '20px', 'justifyContent': 'center', 'marginBottom': '20px'}, children=[
            html.Div([
                html.H3("💰 Total Sales", style={'margin': '0', 'color': '#444'}),
                html.H2(f"{total_sales:,}", style={'margin': '0', 'color': '#1f77b4'})
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),

            html.Div([
                html.H3("📅 Avg Daily Sales", style={'margin': '0', 'color': '#444'}),
                html.H2(f"{avg_daily_sales:,.0f}", style={'margin': '0', 'color': '#2ca02c'})
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),

            html.Div([
                html.H3("🏆 Best Month", style={'margin': '0', 'color': '#444'}),
                html.H2(best_month, style={'margin': '0', 'color': '#ff7f0e'})
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
        ]),

        html.Div(style={'display': 'flex', 'gap': '20px'}, children=[
            html.Div(dcc.Graph(figure=fig_monthly), style={'flex': '1'}),
            html.Div(dcc.Graph(figure=fig_pie), style={'flex': '1'})
        ]),

        html.Div(style={'display': 'flex', 'gap': '20px', 'marginTop': '20px'}, children=[
            html.Div(dcc.Graph(figure=fig_daily_trend), style={'flex': '1'}),
            html.Div(dcc.Graph(figure=fig_monthly_summary), style={'flex': '1'}),
        ]),

        html.Div(style={'marginTop': '20px'}, children=[
            html.Div(dcc.Graph(figure=fig_scatter), style={'flex': '1'})
        ])
    ])

    return f"✅ Uploaded file: {filename}", dashboard

if __name__ == '__main__':
    app.run(debug=True)
