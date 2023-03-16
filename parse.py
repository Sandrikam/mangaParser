import requests,json,re,sys
from bs4 import BeautifulSoup

url = 'https://mangasee123.com/directory/'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

manga_names = []

data = soup.find_all('script')

pattern = re.compile(r'vm.FullDirectory = (\{.*?\});', re.DOTALL)
outp = None

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

url = f'https://mangasee123.com/manga/'+manga_names[1]
#url = 'https://mangasee123.com/read-online/Myuun-I-chapter-1-page-6.html'
response = requests.get(url)
html_content = response.content
productPage = BeautifulSoup(html_content, 'html.parser')

#chapterLinks = productPage.find('a',{"class": "ChapterLink"})["href"]
chapterLinks = productPage.find_all('a',{"class": "list-group-item ChapterLink"})
print(chapterLinks)

