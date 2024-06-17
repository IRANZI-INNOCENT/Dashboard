import streamlit as st
import plotly.express as px

# Sample data for demonstration
df_iris = px.data.iris()
df_gapminder = px.data.gapminder().query("country=='Canada'")
df_tips = px.data.tips()

# Create four different figures using Plotly Express
fig_scatter = px.scatter(df_iris, x='sepal_width', y='sepal_length', color='species', size='petal_length', hover_data=['petal_width'])
fig_line = px.line(df_gapminder, x='year', y='lifeExp', title='Life expectancy in Canada')
fig_bar = px.bar(df_tips, x='day', y='total_bill', color='sex', barmode='group')
fig_histogram = px.histogram(df_tips, x='total_bill', nbins=20)

# Streamlit app layout
st.title("STREAMLIT DASHBOARD")
st.markdown("## Visualizations")

# Display the figures using Streamlit's plotly_chart method
st.plotly_chart(fig_scatter)
st.plotly_chart(fig_line)
st.plotly_chart(fig_bar)
st.plotly_chart(fig_histogram)
