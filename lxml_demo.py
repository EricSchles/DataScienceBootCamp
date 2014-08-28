import requests #pip install
from unidecode import unidecode
import lxml.html #pip install
r = requests.get("https://www.google.com")
#print type(r.text)
text = unidecode(r.text)
#print type(text)

#print text[18500:] #this is a terrible idea

html_obj = lxml.html.fromstring(text)
links = html_obj.xpath("//a")
links_values = [elem.values() for elem in links]
#print links_values
#print links_values[0]
#print links_values[0][1]

#links_values = [elem.values() for elem in links]

# <==>

#links_values = []
#for elem in links:
#    links_values.append(elem.values())

#motivating the need for unidecode - you will forget, don't

#links_text = [str(elem.text_content()) for elem in links] #another reason we need to decode
#print type(links_text)

links_text = [unidecode(elem.text_content()) for elem in links]
links_str = [str(elem) for elem in links_text] 
print type(links_str[0])

#don't skip ahead!
links_iter = [elem.iterlinks() for elem in links]

hyperlink_mapping = {}

for gen in links_iter:
    i = [elem for elem in gen]
    i = i[0]
    #print i[0].text_content(), i[2]
    hyperlink_mapping[i[0].text_content()] = i[2]

print hyperlink_mapping['+Google']
