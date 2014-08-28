import requests #pip install
from unidecode import unidecode #pip install
r = requests.get("https://www.google.com")
#print r.status_code
#print dir(r)
#print type(r.text)

text = unidecode(r.text)
#print type(text)

print text[18500:] #google search bar "did you mean?", "I'm feeling lucky", "Learn more", "Search by image", "Google Search"

