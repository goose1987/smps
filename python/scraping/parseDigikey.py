from bs4 import BeautifulSoup # beautifu soup for parsing html
from tinydb import TinyDB, Query # database to store info

import requests
import csv
import re # reg ex searching


# prefixes
prefix={'p':10.0**-12,'n':10.0**-9,'u':10.0**-6,'m':10.0**-3,'k':10.0**3}

# table order
# compare parts, pdf, image, digikey part no, manufacturer part no, manufacturer, description, quanty, unit price, min quantity, packaging, series, part status, fet type, tech, Vds, Id, Vdrive, Vgsth, Qg, Vgsmax,Ciss, Fet feature, Pdiss max, Rds, operating temp, mounting type, package, case
#https://www.digikey.com/products/en/discrete-semiconductor-products/transistors-fets-mosfets-single/278?FV=ffe00116&mnonly=0&ColumnSort=0&page=1
# url = "https://www.digikey.com/products/en/discrete-semiconductor-products/transistors-fets-mosfets-single/278?FV=pageSize=500"
# link to stepping through pages https://www.digikey.com/products/en/discrete-semiconductor-products/transistors-fets-mosfets-single/278/page/3
urlhead="https://www.digikey.com/products/en/discrete-semiconductor-products/transistors-fets-mosfets-single/278?FV=ffe00116&mnonly=0&ColumnSort=0&page="
urltail="&pageSize=25" # results per page 25, 50, 100, 500
url = "https://www.digikey.com/products/en/discrete-semiconductor-products/transistors-fets-mosfets-single/278?FV=ffe00116&mnonly=0&ColumnSort=0&page=1&pageSize=500"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

# find how many page is avalailbe
pagediv=soup.find("div",{"class":"paging"})
# locate the link of the last page which contains the page number
lasturl=pagediv.find("a",{"class":"Last"})['href']
idxstr=re.search('page/[0-9]+',lasturl).group(0)

lastidx=int(re.search('[0-9]+',idxstr).group(0))
# match regex page/[0-9]+

db = TinyDB('dbScratch.json')
# step through available pages
for idx in range(1,2):
    req = requests.get(urlhead+str(idx)+urltail)
    data = req.text
    soup = BeautifulSoup(data,"lxml")
    # find the table with data
    table = soup.find("table",{"id":"productTable"}).find("tbody")
    for fets in table.find_all('tr'):
        #rowdat = []
        idxtd = 0 # init index to 0
        fetEntry={} # make empty dictionary for entry
        duplicate = 0 # duplicate flag
        fq = Query()
        for row in fets.find_all('td'):
            # index starts at 0
            snipstr = row.get_text().strip().replace("\n",'').encode('utf-8') # grab the text from cell
            if re.search('[0-9.]+',snipstr):
                snipbase = float(re.search('[0-9,.]+',snipstr).group(0).replace(',','')) # convert string to float
                if re.search('[p|n|u|m|k][O|V|F|C|A|W]',snipstr.split('@')[0]):
                    snippre = prefix[re.search('p|n|u|m|k',snipstr).group(0)] # grab prefix
                else :
                    snippre = 1.0
                snipnum = snipbase*snippre
            else :
                snipnum = 0
            # grab manufacturer part number  index = 4
            if idxtd == 4:
                fetEntry['partNumber']=snipstr
                if db.search(fq.partNumber==fetEntry['partNumber']):
                    break # if duplicate break out of for loop

            # check manufacturer part number against database to see if its already added
            # if already added, dont do anything
            # if not already added, create a new dictionary

            # add manufacturer string index = 5
            if idxtd == 5:
                fetEntry['manufacturer']=snipstr

            # add unit price number index = 8
            if idxtd == 8:
                fetEntry['unitPrice']=snipnum # convert to float in USD

            # add part status string index = 12
            if idxtd == 12:
                fetEntry['status']=snipstr
            # add fet type N or P string index = 13
            if idxtd == 13:
                fetEntry['fetType']=snipstr
            # add technology  string index = 14
            if idxtd == 14:
                fetEntry['technology']=snipstr
            # Vds number  index = 15
            if idxtd == 15:
                fetEntry['Vds']=snipnum
            # Id number index = 16
            if idxtd == 16:
                fetEntry['Id']=snipnum
            # drive voltage number index = 17
            if idxtd == 17:
                fetEntry['VgsDrive']=snipnum
            # Vgs number index = 18
            if idxtd == 18:
                fetEntry['Vgsth']=snipnum
            # gate charge Qg index = 21
            if idxtd == 19:
                fetEntry['Qg'] = snipnum
            # Ciss number index = 21
            if idxtd == 21:
                fetEntry['Ciss']=snipnum
            # Pdissipation number index = 23
            if idxtd == 23:
                fetEntry['Pdiss']=snipnum
            # rdson number index = 24
            if idxtd == 24:
                fetEntry['rdson']=snipnum
            # operating temperature number index = 25
            if idxtd == 25:
                fetEntry['Temp']=snipstr
            # package string index = 27
            if idxtd == 27:
                fetEntry['package']=snipstr
                db.insert(fetEntry) # insert entry into database
            # increment index
            idxtd=idxtd+1


'''
with open('digikeyfets.csv','w') as f:
    writer = csv.writer(f)

    for idx in range(1,3):
        req = requests.get(urlhead+str(idx)+urltail)
        data = req.text
        soup = BeautifulSoup(data,"lxml")
        # find the table with data
        table = soup.find("table",{"id":"productTable"}).find("tbody")

        #print urlpage+str(idx)
        #print lastidx['href']
        #print re.search('page/[0-9]+',lastidx['href']).group(0)




        for fets in table.find_all('tr'):
            rowdat = []
            idxtd = 0
            fetEntry={}
            for row in fets.find_all('td'):
                # index starts at 0
                # grab manufacturer part number  index = 4
                if idxtd == 4:

                # check manufacturer part number against database to see if its already added
                # if already added, dont do anything
                # if not already added, create a new dictionary

                # add manufacturer string index = 5
                if idxtd == 5:

                # add unit price number index = 8
                if idxtd == 8:

                # add part status string index = 12
                if idxtd == 12:
                # add technology  string index = 14
                if idxtd == 14:
                # Vds number  index = 15
                if idxtd == 15:
                # Id number index = 16
                if idxtd == 16
                # drive voltage number index = 17
                if idxtd == 17
                # Vgs number index = 18
                if idxtd == 18
                # Ciss number index = 19
                if idxtd == 19
                # Pdissipation number index = 21
                if idxtd == 21
                # rdson number index = 22
                if idxtd == 22
                # operating temperature number index = 23
                if idxtd == 23
                # package string index = 25
                if idxtd == 25
                # increment index
                idxtd=idxtd+1
                snippet = row.get_text().strip().replace("\n",'').encode('utf-8')
                if re.search('[0-9]+',snippet):

                    snippet = re.search('[0-9]+',snippet).group(0) # parse out number only from the cell to separate units like mOhm, pF etc...
                rowdat.append(snippet)
                #print row.get_text().encode('utf-8')

            #print rowdat
            writer.writerow(rowdat)
'''
