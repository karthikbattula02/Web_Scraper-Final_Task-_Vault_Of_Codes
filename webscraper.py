from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Sending a GET request to the URL
page = requests.get(url)

# Parsing the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Find all table elements in the HTML content
table = soup.find_all('table')[1]  # Selecting the second table (index 1) which contains the desired data

# Extract all the table headers (column titles)
world_titles = table.find_all('th')

# Extract the text from each header and strip any surrounding whitespace
world_table_titles = [title.text.strip() for title in world_titles]

# Create a DataFrame with the extracted column titles
df = pd.DataFrame(columns=world_table_titles)

# Find all the table rows in the table
column_data = table.find_all('tr')

# Loop through each row (skipping the first row which contains headers)
for row in column_data[1:]:
    # Extract all the table data (cells) from the row
    row_data = row.find_all('td')
    # Extract the text from each cell and strip any surrounding whitespace
    individual_row_data = [data.text.strip() for data in row_data]
    # Find the current length of the DataFrame to use as the index for the new row
    length = len(df)
    # Add the extracted data as a new row in the DataFrame
    df.loc[length] = individual_row_data

# Save the DataFrame to a CSV file
df.to_csv(r'F:\Engineering\Internships\Internship_2k24_VaultsOfCode\Final Project\Companies.csv', index=False)
