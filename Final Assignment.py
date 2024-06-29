#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork900-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo">
#     </a>
# </p>
# 

# <h1>Extracting and Visualizing Stock Data</h1>
# <h2>Description</h2>
# 

# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some stock data, you will then display this data in a graph.
# 

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>Define a Function that Makes a Graph</li>
#         <li>Question 1: Use yfinance to Extract Stock Data</li>
#         <li>Question 2: Use Webscraping to Extract Tesla Revenue Data</li>
#         <li>Question 3: Use yfinance to Extract Stock Data</li>
#         <li>Question 4: Use Webscraping to Extract GME Revenue Data</li>
#         <li>Question 5: Plot Tesla Stock Graph</li>
#         <li>Question 6: Plot GameStop Stock Graph</li>
#     </ul>
# <p>
#     Estimated Time Needed: <strong>30 min</strong></p>
# </div>
# 
# <hr>
# 

# ***Note***:- If you are working Locally using anaconda, please uncomment the following code and execute it.
# 

# In[ ]:


#!pip install yfinance==0.2.38
#!pip install pandas==2.2.2
#!pip install nbformat


# In[2]:


#!pip install yfinance==0.1.67
#!mamba install bs4==4.10.0 -y
#!pip install nbformat==4.2.0


# In[14]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In Python, you can ignore warnings using the warnings module. You can use the filterwarnings function to filter or ignore specific warning messages or categories.
# 

# In[4]:


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# ## Define Graphing Function
# 

# In this section, we define the function `make_graph`. You don't have to know how the function works, you should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.
# 

# In[43]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# ## Question 1: Use yfinance to Extract Stock Data
# 

# Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.
# 

# In[44]:


import yfinance as yf

# Get stock data for Apple Inc.
stock = yf.Ticker("TSLA")


# Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to `max` so we get information for the maximum amount of time.
# 

# In[46]:


# Get current stock price
tesla_data = stock.history(period="max")


# **Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.
# 

# In[48]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# ## Question 2: Use Webscraping to Extract Tesla Revenue Data
# 

# Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named `html_data`.
# 

# In[49]:


url ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"


# Parse the html data using `beautiful_soup`.
# 

# In[55]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Send a GET request to the URL
response = requests.get(url)

# Save the text of the response as a variable
html_data = response.text

# Parse the HTML data
soup = BeautifulSoup(html_data, 'html.parser')


# Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.
# 

# <details><summary>Click here if you need help locating the table</summary>
# 
# ```
#     
# Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab
#     
# soup.find_all("tbody")[1]
#     
# If you want to use the read_html function the table is located at index 1
# 
# We are focusing on quarterly revenue in the lab.
# ```
# 
# </details>
# 

# In[60]:


# Find the table containing the Tesla revenue data
revenue_table = soup.find_all('table')[0]

# Extract the table rows
rows = revenue_table.find_all('tr')

# Initialize lists to store the data
dates = []
revenues = []

# Loop through the rows and extract the data
for row in rows[1:]:
    cols = row.find_all('td')
    date = cols[0].text.strip()
    revenue = cols[1].text.strip().replace('$', '').replace(',', '')
    dates.append(date)
    revenues.append(revenue)

# Create a dataframe
tesla_revenue = pd.DataFrame({"Date": dates, "Revenue": revenues})

# Print the dataframe to verify
print(tesla_revenue)


# Execute the following line to remove the comma and dollar sign from the `Revenue` column. 
# 

# In[61]:


#tesla_revenue["Revenue"] = tesla_revenue['Tesla Quarterly Revenue (Millions of US $).1'].str.replace(',|\$',"")


# Execute the following lines to remove an null or empty strings in the Revenue column.
# 

# In[62]:


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.
# 

# In[63]:


tesla_revenue.tail()


# ## Question 3: Use yfinance to Extract Stock Data
# 

# Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is `GME`.
# 

# In[64]:


mge_data = yf.Ticker("GME")


# Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`. Set the `period` parameter to `max` so we get information for the maximum amount of time.
# 

# In[65]:


# Get current stock price
gme_data = stock.history(period="1y")


# **Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.
# 

# In[66]:


gme_data.reset_index(inplace=True)
gme_data.head()


# ## Question 4: Use Webscraping to Extract GME Revenue Data
# 

# Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named `html_data`.
# 

# In[67]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html."


# Parse the html data using `beautiful_soup`.
# 

# In[68]:


import requests

# URL of the webpage to download
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# Send a GET request to the URL
response = requests.get(url)

# Save the text of the response
html_data = response.text

# Print the first 500 characters of the HTML data
print(html_data[:500])


# Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. Make sure the comma and dollar sign is removed from the `Revenue` column using a method similar to what you did in Question 2.
# 

# In[69]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
response = requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data, 'lxml')
revenue_table = soup.find('table', attrs={'class': 'historical_data_table'})
rows = revenue_table.find_all('tr')

dates = []
revenues = []

for row in rows[1:]:
    cols = row.find_all('td')
    date = cols[0].text.strip()
    revenue = cols[1].text.strip().replace('$', '').replace(',', '')
    dates.append(date)
    revenues.append(revenue)

gme_revenue = pd.DataFrame({"Date": dates, "Revenue": revenues})
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"])

print(gme_revenue)


# <details><summary>Click here if you need help locating the table</summary>
# 
# ```
#     
# Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab
#     
# soup.find_all("tbody")[1]
#     
# If you want to use the read_html function the table is located at index 1
# 
# 
# ```
# 
# </details>
# 

# Display the last five rows of the `gme_revenue` dataframe using the `tail` function. Take a screenshot of the results.
# 

# In[39]:


pd.DataFrame(gme_revenue).tail()


# ## Question 5: Plot Tesla Stock Graph
# 

# Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(tesla_data, tesla_revenue, 'Tesla')`. Note the graph will only show data upto June 2021.
# 

# In[73]:


def make_graph(stock_data, title):
    trace_stock = go.Scatter(x=stock_data['Date'], y=stock_data['Close'], mode='lines', name='Stock Close Price')

    layout = go.Layout(
        title=title,
        xaxis=dict(title='Date'),
        yaxis=dict(title='Stock Close Price'),
        legend=dict(x=0.1, y=1.1, orientation='h'),
        hovermode='x',
        margin=dict(l=40, r=20, t=40, b=20)
    )

    fig = go.Figure(data=[trace_stock], layout=layout)
    fig.show()

make_graph(tesla_data.loc[:'2021-06-30'], 'Tesla Stock Close Price (Up to June 2021)')


# ## Question 6: Plot GameStop Stock Graph
# 

# Use the `make_graph` function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`. Note the graph will only show data upto June 2021.
# 

# In[77]:


def make_graph(stock_data, revenue_data, title):
    trace_stock = go.Scatter(x=stock_data['Date'], y=stock_data['Close'], mode='lines', name='Stock Close Price',line=dict(color='red'))

    layout = go.Layout(
        title=title,
        xaxis=dict(title='Date'),
        yaxis=dict(title='Stock Close Price'),
        legend=dict(x=0.1, y=1.1, orientation='h'),
        hovermode='x',
        margin=dict(l=40, r=20, t=40, b=20)
    )

    fig = go.Figure(data=[trace_stock], layout=layout)
    fig.show()

# Assuming gme_data and gme_revenue are already defined DataFrames
make_graph(gme_data.loc[:'2021-06-30'], gme_revenue, 'GameStop Stock Close Price (Up to June 2021)')


# <h2>About the Authors:</h2> 
# 
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# Azim Hirjani
# 

# ## Change Log
# 
# | Date (YYYY-MM-DD) | Version | Changed By    | Change Description        |
# | ----------------- | ------- | ------------- | ------------------------- |
# | 2022-02-28        | 1.2     | Lakshmi Holla | Changed the URL of GameStop |
# | 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |
# | 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |
# 
# <hr>
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 
# <p>
# 
