import urllib.request, json
api_keys = ['8c2d02be-5bd5-4985-9996-17b81b140fde','58e4c625-4d17-48b1-b4d2-c6ba7e04af4d']
urlAPI = "https://content.guardianapis.com/search?api-key=58e4c625-4d17-48b1-b4d2-c6ba7e04af4d&page-size=100&from-date=2008-01-01&to-date=2017-04-16&page=1"
save = ''
with urllib.request.urlopen(urlAPI) as url:
    first_page = json.loads(url.read().decode())
    page_len = first_page['response']['pages']

file = open('Guardian_headlines.csv','a')
counter = 0

for i in list(range(1,int(page_len))):
    counter += 1
    print(str(counter/int(page_len)*100) + '%',end='\r')
    try:
        urlAPI = "https://content.guardianapis.com/search?api-key=58e4c625-4d17-48b1-b4d2-c6ba7e04af4d&page-size=100&from-date=2008-01-01&to-date=2017-04-16&page=" + str(i)
        with urllib.request.urlopen(urlAPI) as url:
            data = json.loads(url.read().decode())
            for record in data['response']['results']:
                file.write(record['webPublicationDate'] + ',' + record['webTitle'].replace(',','') + '\n')
    except:
        print('Error!!!!!!')
        print('Changing the key')

file.close()
file.close()