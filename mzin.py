import requests
from bs4 import BeautifulSoup
import pandas
website_url = requests.get('https://survivor.fandom.com/wiki/Survivor:_China').text

soup = BeautifulSoup(website_url,'lxml')
##print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable article-table'})
#print(My_table)

table_text = My_table.get_text()
print(table_text.splitlines())

#clean up the table text.


#create the table of castaway info
column_names = ["Name", "Age", "Hometown", "Tribe", "Rank", "Day voted out", "Votes against"]
df = pd.Dataframe(columns = column_names)

##Extract import info from the table
##We want Name, Tribes, Day voted out

## This function will take text (which represents on row for a castaway) and extract its info
def extract_castaway_info (text):
    print(text)