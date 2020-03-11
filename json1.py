# etl ja json -harjoitustyön esimerkkivastaus (C) Joni'20
t = open("customers.txt", "r")
w = open("customers.json", "w+")
rivilaskuri=0
w.write("[")
for rt in t:
    rt = rt[:len(rt)-1]
    if (rivilaskuri%6 == 0):
        r1 = ('"id":' + rt)
    elif (rivilaskuri%6 == 1):
        r2 = ('"etunimi":"' + rt + '"')
    elif (rivilaskuri%6 == 2):
        r3 = ('"sukunimi":"' + rt + '"')
    elif (rivilaskuri%6 == 4):
        r4 = ('"arvo":' + rt )
    elif (rivilaskuri%6 == 5):
        if (rivilaskuri>5):
            w.write(",")
        rivi = "{" + r1+"," + r2 + "," + r3 + "," + r4 + "}"
        w.write(rivi)
        rivi=""
    rivilaskuri+=1
w.write("]")
w.close()