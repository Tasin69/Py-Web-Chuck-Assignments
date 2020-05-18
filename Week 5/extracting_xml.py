import urllib as ub
import ssl
import xml.etree.ElementTree as et

# Test link: http://py4e-data.dr-chuck.net/comments_42.xml

# This ignores SSL certificate errors, meaning https will work now.
new_context = ssl.create_default_context()
new_context.check_hostname = False
new_context.verify_mode = ssl.CERT_NONE

url = input("URL: ")
xml_data = ub.request.urlopen(url, context = new_context).read().decode()
xml_tree = et.fromstring(xml_data)
cmnt_list = xml_tree.findall('comments/comment') # This finds all the 'comment' tags 

# Creating a dynamic list containing the numbers under 'count' tags (as strings), 
#  converting them to integers and summing the list, we get the output.                                                  
print(sum([int(cmnt.find('count').text) for cmnt in cmnt_list]))

# Ignoring ssl certificates isn't necessary as long as we aren't dealing with https.

# Another way to find the 'count' tag is to use an XPath selector string.......
# ...(xml_tree.findall('.//count')). This searches for any tag named 'count'.
# We can then create a dynamic list going over all the elements in 'count', converting
#  them to text and then to integers, then by summing the list, we get the output.
# This results in a simpler implementation. Check 'extracting_xml_submitted.py'