from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = 'https://www.poshantracker.in/'
headers = {
   "Accept-Language": "hi-IN,hi;q=0.9,en-US;q=0.8,en;q=0.7"  # replace with the desired language code
}
s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1)
trail = r.html.xpath('//*[@id="root"]/div/div[4]', first=True)
print('trail.absolute_links ', trail.absolute_links)
for url in trail.absolute_links:
    try:
        s = HTMLSession()
        r = s.get(url)
        r.html.render(sleep=10)
        h = r.html.find('.tab-content', first=True)
        print(h.text)
    except Exception as exp:
        print(exp)


#//*[@id="headingOne"]
#//*[@id="root"]/div/div[4] #home_faq_sect
#response = requests.get(url)
