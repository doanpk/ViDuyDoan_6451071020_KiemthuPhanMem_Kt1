import urllib.request
from html.parser import HTMLParser

class P(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag in ['input', 'button', 'form', 'a']:
            d = dict(attrs)
            print(f'{tag}: id={d.get("id","")}, name={d.get("name","")}, class={d.get("class","")}, type={d.get("type","")}, href={d.get("href","")}')

P().feed(urllib.request.urlopen('https://vanphongdientu.utc.edu.vn/Login').read().decode('utf-8'))
