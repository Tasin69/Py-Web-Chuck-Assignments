#  In this assignment you will write a Python program that expands 
#                        on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below,
#   extract the href= vaues from the anchor tags, scan for a tag that is 
#   in a particular position relative to the first name in the list,
#   follow that link and repeat the process a number of times and report 
#   the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name
#  for your testing and the other is the actual data you need to process for the assignment

#     Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#     Find the link at position 3 (the first name is 1). Follow that link. 
#     Repeat this process 4 times. The answer is the last name that you retrieve.
#     Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#     Last name in sequence: Anayah
#     Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Deecan.html
#     Find the link at position 18 (the first name is 1). Follow that link. 
#     Repeat this process 7 times. The answer is the last name that you retrieve.
#     Hint: The first character of the name of the last page that you will load is: M

import urllib as ub
from bs4 import BeautifulSoup
import ssl
import re

new_context = ssl.create_default_context()
new_context.check_hostname = False
new_context.verify_mode = ssl.CERT_NONE


url = input("URL: ")
html_data = ub.request.urlopen(url, context = new_context).read()
thai = BeautifulSoup(html_data, 'html.parser') 
    
for i in range(7):
    tags = thai('a')
    links = [tag.get('href') for tag in tags]
    print(re.findall('by_(.+).html', links[17]))
    url = links[17]
    html_data = ub.request.urlopen(url, context = new_context).read()
    thai = BeautifulSoup(html_data, 'html.parser') 