from collections import defaultdict
import requests

a = {}
r = requests.get("https://dfedorov.spb.ru/python3/sport.txt")
r.encoding = 'cp1251'
d = r.text.split('\r\n')
all_sports = defaultdict(int)
for lines in d:
    line = lines.split('\t')
    if len(line) > 3:
        sports = line[3].strip()
        s = [sport.strip() for sport in sports.split(',')]
        for sport in s:
            if sport:
                all_sports[sport] += 1
all_sports = dict(all_sports)
all_sports = sorted(all_sports.items(), key= lambda item: item[1], reverse = True)[:3]
print(all_sports)



            

# for lines in r:
#     d = lines.decode('cp1251')
#     s = d.split("\t")
#     print(s, "\n")
# print(d, sorted(d.split(), key = str.lower), '\n')
