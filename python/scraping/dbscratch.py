from tinydb import TinyDB, Query
import re
db = TinyDB('dbScratch.json')

prefix={'p':10.0**-12,'n':10.0**-9,'u':10.0**-6,'m':10.0**-3,'k':10.0**3}

foo={}
foo['type']='mosfet'
foo['part_number']='EPC2034'
bar={}
bar['type']='mosfet'
bar['part_number'] = 'EPC2032'

#b.insert(foo)
#db.insert(bar)


txtstr= "0.26nC @ 10V"



FET = Query()
for results in db.search(FET.Vds<200):
    print results['partNumber']
    print results['status']
    print results['Vds']
