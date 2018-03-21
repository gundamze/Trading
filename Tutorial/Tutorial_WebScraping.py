############ web scraping: xml and html #################

x = 1

"""    check out the code of the html

<table>                 # start of a table
  <tr>                  # start of a row
    <th>Month</th>      # start a header, Month
    <th>Savings</th>    # start a header, Savings
  </tr>                 # end of the row
  <tr>                  # start of a row
    <td>January</td>    # start a standard cell, input January,
    <td>$100</td>       # start a cell, input $100
  </tr>                 # end of a row
  <tr>                  # start of row
    <td>February</td>   # start a cell, input Febrary
    <td>$80</td>        # start of a cell, input $80
  </tr>                 # end of row
</table>                # end of table


# this table is like this

Month	  Savings
January	  $100
February  $80

# if want to check the tag's code, click the link : http://www.w3schools.com/tags/

"""


""" ______________________________________________________________________________________
                            beatifulsoup module
    the document link : http://www.crummy.com/software/BeautifulSoup/bs4/doc/

                            the first example
the target web link :  https://en.wikipedia.org/wiki/List_of_postcode_districts_in_the_United_Kingdom
    ______________________________________________________________________________________
"""

import BeautifulSoup
import urllib2


wiki = "http://en.wikipedia.org/wiki/List_of_postcode_districts_in_the_United_Kingdom"   # the url string
header = {'User-Agent': 'Mozilla/5.0'}        # Needed to prevent 403/10054 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup.BeautifulSoup(page)
# Beautifulsoup is a module, is also a kind of data structure, like DataFrame, soup now is the script of the html
type(soup)
soup.name
soup.head
soup.body

""" ######################################
              the link (href)

"""
soup.findAll('a')

""" #######################################
              the table
"""
soup.findAll('table')

# find out the script about the table, this table's class is wikitable sortable, only one table(our target) is that class
table = soup.find("table", { "class" : "wikitable sortable" })
table_header = table.findAll('tr')[0]     # the first row of table, the header of table
table_fr = table.findAll('tr')[1]     # the second row of table, the cell of table

table_header_th = table_header.findAll('th')         # a list of headers in header row
table_header_th[0]         # the first header
len(table_header_th)       # the number of column


table_fr_td = table_fr.findAll('td')
table_fr_td[0]             # the value in second column of first row, it is a tag
len(table_fr_td)           # the number of column
type(table_fr_td[0])

table_fr_td_1 = table_fr_td[0].findAll(text = True)    # it is NavigableString, one type of string
type(table_fr_td_1)
dir(table_fr_td_1)              # check attributes of object


""" #########################################
      use the loop to get the table values
"""
# initial the empty variables
area = []
district = []
town = []
county = []

for row in table.findAll("tr"):
    cells = row.findAll("td")
    #For each "tr", assign each "td" to a variable.
    if len(cells) == 4:
        area.append(cells[0].find(text=True))
        district.append(cells[1].findAll(text=True))
        town.append(cells[2].find(text=True))
        county.append(cells[3].find(text=True))


district[0]
type(district[0])
' '.join(district[0]).replace('\n','')
x = 0


# district can be a list of lists, so we want to iterate through the top level lists first...
district_new = []
for x in range(len(district)):
    new = ' '.join(district[x]).replace('\n','')
    district_new.append(new)

""" _________________________________________________________________________________

                      second example: financial data
    link: http://finance.yahoo.com/q/op?s=AAPL+Options
    _________________________________________________________________________________

"""


import BeautifulSoup
from urllib2 import urlopen

page = urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options')
soup = BeautifulSoup.BeautifulSoup(page)

""" #################################
                soup
"""
type(soup)
soup.head
soup.title
soup.body
soup.contents    # the same to body



"""  ###############################
          the link
"""

links = soup.findAll('a')       # you find the "<\a>" in the document, which is indicator of HREF, kind of a list of address

links[:10]

lnk = links[0]    # pick out a link
type(lnk)         # it is a tag
lnk.name          # a, means it is a HREF
lnk.attrs
lnk.parents
lnk.get('href')   # return the URL of the link

urls = [lnk.get('href') for lnk in soup.findAll('a')]      # get all the URL from the links


""" ###########################################
                  table
"""
tables = soup.findAll('table')      # find all the tables in the document(web)

len(tables)     # check how many tables in this html
type(tables)
calls = tables[1]
puts = tables[2]
type(calls)

####################### the header ########################

header = calls.findAll('th')
type(header)           # this is list, do not have .findAll method, and .contents method
len(header)            # the number of column

header[0]              # the script of first column name
type(header[0])        # this is tag, it has .findAll, .contents method

header[0].findAll('div')[1].contents                 # the first header
header[1].contents                                   # the second header
header[3].findAll('div')[1].contents                 # the third header


##################### the value ####################

rows = calls.findAll('tr')    # find out rows in the call table
len(rows)   # the number of rows
rows[2]     # the header line
type(rows[2])
rows[2].findAll('td')[0].findAll('a')[0].contents       # the 0 and 1 entry
rows[2].findAll('td')[2].findAll('div')[0].contents     # the 2-6, 8-9 entry
rows[2].findAll('td')[7].findAll('strong')[0].contents  # the 7 entry

rows[2].findAll('td')[0].contents[1].contents[0].contents[0]   # the 0, 1st entry
rows[2].findAll('td')[2].contents[1].contents[0]               # 2-9 entry

### deal with header again
rows[0].findAll('th')[0].findAll('div')[1].contents   # the 0, 2-9 header
rows[0].findAll('th')[1].contents                     # the 1 header


def _unpack(row, kind='td'):
    # row: the single row, such as rows[2]
    row_value = []
    elts = row.findAll(kind)
    if kind == 'th':
        for i in range(10):
            if i == 1:
                row_value.append(elts[i].contents[0])
            else:
                row_value.append(elts[i].findAll('div')[1].contents[0])
    else:
        for i in range(10):
            if i in [0,1]:
                row_value.append(elts[i].contents[1].contents[0].contents[0])
            else:
                row_value.append(elts[i].contents[1].contents[0])
    return row_value


_unpack(rows[0], kind='th')
_unpack(rows[2])

##### convert list of string in each row into DataFrame

from pandas.io.parsers import TextParser

def parse_options_data(table):
    rows = table.findAll('tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[2:]]         # a list of row string
    return TextParser(data, names=header).get_chunk()

call_data = parse_options_data(calls)
put_data = parse_options_data(puts)
call_data[:5]
put_data[-5:]

