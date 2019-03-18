'''
Create an account at freecycle or use the following:
user: martin-martin
pwd:  bali2019

Using python's request_html library:
* log in to the website
* navigate to the site that contains all posts for the Denver, CO group
* retrieve all post titles from the first page
* save the titles to a file called 'denver_posts.txt'

BONUS: use pagination features to retrieve all posts of all pages in the group
       and save them to the file

'''
# import requests_html
#
# requests = requests_html.HTMLSession()
#
# #.post = Sends a POST request. Returns Response object.
# # Return type:	requests.Response
# payload = {'username': 'martin-martin', 'pass': 'bali2019'}
# url = 'https://my.freecycle.org/'
# info = requests.post(url, data=payload)
# #print(info.text)


from requests_html import HTMLSession

#requests = requests_html.HTMLSession()

#.post = Sends a POST request. Returns Response object.
# Return type:	requests.Response
#payload = {'username': 'martin-martin', 'pass': 'bali2019'}
#url = 'https://my.freecycle.org/'
#info = HTMLSession().post(url, data=payload)
#print(info.text)



url = 'https://groups.freecycle.org/group/North_Denver_CO/posts/all'
webpage = HTMLSession().get(url)
#section = webpage.html.xpath('//*[@id="group_posts_table"]/tbody', first=True)
#link = webpage.html.find('#group_posts_table > tbody > tr:nth-child(1)', first=True)
print(webpage.html.find('#group_posts_table'))

#group_posts_table > tbody > tr:nth-child(1)




