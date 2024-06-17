import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Sample data for demonstration
df_iris = px.data.iris()
df_gapminder = px.data.gapminder().query("country=='Canada'")
df_tips = px.data.tips()

# Create four different figures
fig_scatter = px.scatter(df_iris, x='sepal_width', y='sepal_length', color='species', size='petal_length', hover_data=['petal_width'])
fig_line = px.line(df_gapminder, x='year', y='lifeExp', title='Life expectancy in Canada')
fig_bar = px.bar(df_tips, x='day', y='total_bill', color='sex', barmode='group')
fig_histogram = px.histogram(df_tips, x='total_bill', nbins=20)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1("DASH DASHBOARD",
            style={'textAlign': 'center', 'color': 'red', 'font-size': 40}),
    html.P("Visualizations",
           style={'textAlign': 'right', 'color': 'green', 'font-size': 30}),
    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dcc.Graph(id='scatter-plot', figure=fig_scatter)
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(id='line-plot', figure=fig_line)
        ]),
    ]),
    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dcc.Graph(id='bar-chart', figure=fig_bar)
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(id='histogram', figure=fig_histogram)
        ]),
    ]),
], style={'maxWidth': '1200px', 'margin': 'auto'})

# Run the app
if __name__ == '__main__':
    app.run_server()
