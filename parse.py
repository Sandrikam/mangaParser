import requests,json,re,sys
from bs4 import BeautifulSoup

url = 'https://mangasee123.com/directory/'
print(url)
response = requests.get(url)
desiredManga='5-Ji-Kara9-Ji-Made'
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

manga_names = []
chapters = []
data = soup.find_all('script')

pattern = re.compile(r'vm.FullDirectory = (\{.*?\});', re.DOTALL)
outp = None

## Will Need for function later
# print(manga_names.index('3-Gatsu-No-Lion',0,len(manga_names)))

for script in data:
    match = pattern.search(str(script))
    if match:
        outp = json.loads(match.group(1))
        break

if outp:
    directory_list = outp['Directory']

    for directory in directory_list:
        manga_names.append(directory['i'])
else:
    print("JSON data not found")

mangaCode=manga_names.index(desiredManga,0,len(manga_names))
url = f'https://mangasee123.com/manga/'+manga_names[mangaCode]
print(url)

print(mangaCode)
response = requests.get(url)
html_content = response.content
productPage = BeautifulSoup(html_content, 'html.parser')

chapterLinks = productPage.find_all('script')
chptpattern = re.compile(r'vm.Chapters = (\[[^\]]*\]);', re.DOTALL)
i = None


for i in chapterLinks:
    match = chptpattern.search(str(i))
    if match:
        i = json.loads(match.group(1))
        break

if i:
    chapters= [json_object['Chapter'] for json_object in i]
    chapterNum = str(int(chapters[1][1:-1]))
    print(manga_names[mangaCode])
    print(len(chapters))

else:
    print("JSON data not found")

url=f'https://mangasee123.com/read-online/'+manga_names[mangaCode]+'-chapter-'+chapterNum+'-page-1.html'
    
print(url)
#chapterNum = int(chapters[1][1:-1])
#print(chapterNum)