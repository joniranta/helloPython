# etl to jsoc -harjoitustehtävä käyttän json-kirjastoa
import json 

asiakas = {} 
asiakkaat = []
rivilaskuri=0
key = ['id','etunimi','sukunimi','kaupunki','arvo','tyhja']

with open("customers.txt") as rt: 
    for rivi in rt:
        if (rivilaskuri%6 in (0,4)):
            asiakas[key[rivilaskuri%6]] = int(rivi)
        if (rivilaskuri%6 in (1,2)):
            asiakas[key[rivilaskuri%6]] = rivi.strip()
        if (rivilaskuri%6==5):
            asiakkaat.append(asiakas.copy())
        rivilaskuri+=1

jt = open("customrs2.json", "w+") 
json.dump(asiakkaat, jt, indent = 4, sort_keys = False) 
jt.close() 
