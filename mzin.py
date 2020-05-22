import requests
from bs4 import BeautifulSoup
import pandas as pd
website_url = requests.get('https://survivor.fandom.com/wiki/Survivor:_China').text

soup = BeautifulSoup(website_url,'lxml')
##print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable article-table'})
#print(My_table)

table_text = My_table.get_text()
table_array = table_text.splitlines()

#clean up the table text.
cleaned_array = table_array[14:]


def get_next_castaway(array):
    clean = array[0:3]
    print(clean)
    count = 3
    print(clean[count-1], clean[count-2])
    while clean[count-1] != '' and clean[count-2] != '' and clean[count-3] != '':
        print('text')
        clean = array[0:count]
        count = count + 1
    print(count)
    return count

get_next_castaway(cleaned_array)

#create the table of castaway info
column_names = ["Name", "Age", "Hometown", "Tribe", "Rank", "Day voted out", "Votes against"]
df = pd.DataFrame(columns = column_names)

##Extract import info from the table
##We want Name, Tribes, Day voted out

## This function will take text (which represents on row for a castaway) and extract its info
def extract_castaway_info (text):
    print(text)