from requests_html import HTMLSession

url = "https://www.tripadvisor.co.uk/ShowUserReviews-g297701-d8563593-r519115639-Sage-Ubud_Gianyar_Regency_Bali.html"

res = requests.get(url)

with open('sagereview_TA.html', 'w', encoding='utf-8') as fout:
    fout.write(res.text)
