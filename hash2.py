d={}
with open('nyc_weather.csv','r') as fobj:
    for line in fobj:
        ln=line.split(',')
        if ln[0] not in d:
            d[ln[0]]=ln[1]
    print(d['Jan 9'])
    print(d['Jan 4'])
            
