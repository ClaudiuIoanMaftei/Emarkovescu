import requests
import re

poems=[]

def scrape():
    global poems

    html_text = requests.get("https://ro.wikisource.org/wiki/Autor:Mihai_Eminescu").text
    html_text = html_text.split("Corespond")[2]

    poem_links=re.findall(r'<li><a href=\"/wiki/(.*?)\" title',html_text)
    for link in poem_links:
        print(link)
        poem_html=requests.get("https://ro.wikisource.org/wiki/"+link).text
        if not "class=\"poem\">" in poem_html: continue
        poem_html=poem_html.split("class=\"poem\">")[1]
        poem_html=poem_html.split("</div>")[0]
        text=re.sub(r'<.*?>',r'',poem_html)
        text=text.replace("&#160;","")
        poems.append(text)