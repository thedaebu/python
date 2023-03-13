from bs4 import BeautifulSoup
import requests

# with open('./working_files/html_sample.html', 'r') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# # prettify method returns with proper indents
# # print(soup.prettify())

# # returns first encounter of specified html element
# soup_title = soup.title
# print(soup_title.prettify())
# # returns text of html element
# print(soup_title.text)

# # find method searches for element according to tag and attribute key
# soup_footer = soup.find('div', class_='footer')

# # find_all method searches for all element according to tag as a list
# soup_divs = soup.find_all('div')

# requests get method returns html from url
source = requests.get('http://coreyms.com').text
soup_from_source = BeautifulSoup(source, 'lxml')
print(soup_from_source.prettify())
