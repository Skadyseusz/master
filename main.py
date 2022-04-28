import requests

link = requests.get('https://app.api.trainerday.com/api/workout/search?s=&pageNumber=0&pageSize=1&myLibrary=0&textDescriptions=0&authorDescriptions=0&hasCadence=0&hasIntervalComments=0&minutesBetween[]=&minutesBetween[]=&stressBetween[]=&stressBetween[]=&intensityBetween[]=&intensityBetween[]=&sortBy=popularity')
sz = link.text

#tyt_pocz = sz.find('"description":')
#tyt_kon = sz.find('","hasTextDescription"')
tytul = sz[sz.find('"description":')+14:sz.find(',"hasTextDescription"')]
print(tytul)

slug_linka = sz[sz.find('"slug":"')+8:sz.find('","createdAt"')]
print(slug_linka)

konstruktor_linka = 'https://app.trainerday.com/workouts/'+slug_linka
print(requests.get(konstruktor_linka).text)

segmenty = sz[sz.find('"segments":')+11:sz.find(',"isOutdoor"')]
segmenty = segmenty.replace('],[', ' ')
segmenty = segmenty.replace('[[', '')
segmenty = segmenty.replace(']]', '')
segmenty = segmenty.split(' ')
ilosc_segmentow = len(segmenty)
print(ilosc_segmentow)
print(segmenty)
print(segmenty[25])