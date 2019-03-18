'''
Using requests_html scrape information from a wikipedia page that interests you.
( you can use: https://en.wikipedia.org/wiki/Ubud )

Collect:
* all the information recorded in the infobox on the right
* 2 links to images on the site
* an interesting fact or quote from the page
* a collection of all the resources (titles and links) related to the page

Store the information in a nicely formatted text file.


<div style="display:inline" class="fn org">Christchurch</div>
<div class="nickname" style="font-weight:normal;display:inline;"><i lang="mi" title="Māori language text">Ōtautahi</i>&nbsp;&nbsp;<span class="languageicon" style="font-size:85%;font-weight:normal;">(<a href="/wiki/M%C4%81ori_language" title="Māori language">Māori</a>)</span></div>
'''


from requests_html import HTMLSession


url = "https://en.wikipedia.org/wiki/Christchurch" #https://en.wikipedia.org/wiki/Christchurch"

session = HTMLSession()
r = session.get(url)

# for link in r.html.absolute_links:
#     print(link)

#names = r.html.xpath('//*[@id="mw-content-text"]/div/p[7]', first=True)  # first=True because otherwise it returns a list

#infobox = r.html.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody', first=True)  # first=True because otherwise it returns a list

map = r.html.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr[8]/td/div/div/div/div[1]/a/img', first=True)  # first=True because otherwise it returns a list




print(map.absolute_links)

#ps = content.find('p')

# for p in ps:
#     print(p.text, end='\n\n')

'''
from requests_html import HTMLSession


url = "https://en.wikipedia.org/wiki/Ubud"
session = HTMLSession()
r = session.get(url)

for link in r.html.absolute_links:
    print(link)

# using CSS selectors
history = r.html.find('#Buildings', first=True)  # first=True because otherwise it returns a list

# or using XPATH
content = r.html.xpath('//*[@id="mw-content-text"]/div', first=True)

ps = content.find('p')

for p in ps:
    print(p.text, end='\n\n')
    '''




