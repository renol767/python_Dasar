import csv, urllib.request
response = urllib.request.urlopen('https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv')
lines = [l.decode('utf-8') for l in response.readlines()]
cr = csv.reader(lines)
for row in cr:
    print(row)