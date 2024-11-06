import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings
# Ignore all warnings

warnings.filterwarnings("ignore", category=FutureWarning)

#Step 1: Send an HTTP request to the web page
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text
(data)

#Step 2: Parse the HTML content
soup = BeautifulSoup(data, 'html.parser')
(soup)

#Step 3: Identify the HTML tags
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
print(netflix_data)

#Step 4: Use a BeautifulSoup method for extracting data
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # Finally I appended the data of each row to the table
    netflix_data = pd.concat([netflix_data, pd.DataFrame(
        {"Date": [date], "Open": [Open], "High": [high], "Low": [low], "Close": [close], "Adj Close": [adj_close],
         "Volume": [volume]})], ignore_index=True)
#Step 5: Print the extracted data
print(netflix_data.head())

##Extracting data using pandas library
read_html_pandas_data = pd.read_html(url)
print(read_html_pandas_data)
netflix_dataframe = read_html_pandas_data[0]
print(netflix_dataframe)
netflix_dataframe.head()

