
#  pip install beautifulsoup4
# pip install lxml (we shall be using this)
# pip instal html5lib
# pip install request

from bs4 import BeautifulSoup
import  requests as rq 
import csv

# open a file using context manager
#with open('Dir_Sraping\scaping.csv','w') as csv_file:
    #csv_writer = csv.writer(csv_file)
    #csv_writer.writerow(['Title','Tag'])

csv_file = open('Dir_Sraping\scaping.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Tag'])


def getContent():
    results = rq.get('http://qa.loginapp.nsncareers.com/') 
    # http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168
    soup = BeautifulSoup(results.text,'lxml') # lxml parser helps to parse xml and html contenet
    # content = soup.prettify() # Helps to indent
    # content = soup.title # Gets page title
    title = soup.title.text # Gets only title withot html tags
    # div = soup.div # Gets the first dive tag of the page
    # content = soup.find('a', {'class':'navbar-brand'}) # get tag a with class 

    # container = soup.find('div', {'class':'navbar-collapse collapse d-sm-inline-flex flex-sm-row-reverse'}) 
    # text = container.ul.li.a.text # Get text using child tag

    content = soup.find_all('div', {'class':'container'}) # returns a list of all the specified elements

    # We can loop through
    #for x in content:
        #content1 = x.h1
        #content2 = x.a
        #print(content1)
        #print(content2)
    

    # Get specific tag by using dictionary object
    href_list = soup.find('li', {'class':'nav-item'}).a['href']
    # Split list
    split_list = href_list.split('/')
    # Get 4 th index
    content = split_list[3]
    csv_writer.writerow([title,content])
    csv_file.close()
    # print(content)


getContent()


