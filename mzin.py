import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
website_url = requests.get('https://survivor.fandom.com/wiki/Survivor:_China').text

soup = BeautifulSoup(website_url,'lxml')
##print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable article-table'})
#print(My_table)

table_text = My_table.get_text()
table_array = table_text.splitlines()

#clean up the table text.
cleaned_array = table_array[14:]

def get_next_castaway(array, pointer):
    clean = array[pointer:pointer+3]
    count = pointer + 3
    while clean[count-1] !='' or clean[count-2] !='' or clean[count-3]!='':
        count = count + 1
        clean = array[0:count]
    #print(count)
    #print(clean)
    return count

pointer = 0
prev_pointer = 0
while len(cleaned_array) > pointer:
    prev_pointer = pointer
    pointer = get_next_castaway(cleaned_array, pointer)
    castaway_array = cleaned_array[prev_pointer:pointer]
    print(pointer, prev_pointer)
    #get the name
    if castaway_array[0].find(',') != -1:
        name_age = castaway_array[0][0:castaway_array[0].find(',')]
        #print(name_age)
        num_index = re.search(r"\d", name_age)
        name = name_age[0:num_index.start()]
        age = name_age[num_index.start():]
        #print(name)
        #print(age)


#create the table of castaway info
column_names = ["Name", "Age", "Hometown", "Tribe", "Rank", "Day voted out", "Votes against"]
df = pd.DataFrame(columns = column_names)

##Extract import info from the table
##We want Name, Tribes, Day voted out

## This function will take text (which represents on row for a castaway) and extract its info
def extract_castaway_info (text):
    print(text)


## Todo Create the castaways dataset, with a row for each individuals castaway + tribe
## Todo add image URLs to the dataset
## Todo get a list of all fandom survivor seasons, an use that to iterate through
## Todo make sure that all seasons have the same format