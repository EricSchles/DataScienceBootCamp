import requests
import lxml.html
import re
def clean_str(string):
    if len(string) > 18:
        return ''
    if string == '' or string == ' ' or string == '  ':
        return ''
    string = string.encode('ascii','ignore')
    string = string.replace("\r","")
    string = string.replace("\t","")
    string = string.replace("\n","")
    return string


r = requests.get("http://www.baseballamerica.com/statistics/teams/players/?tm_id=1028&y=2014")
html_yanks = lxml.html.fromstring(r.text)
tables = html_yanks.xpath('//table[@class="small"]')
#print len(tables)
batting,pitching = tables

batting_obj = batting.xpath("//td")
pitching_obj = pitching.xpath("//td")

batting_stats = []

for ind,val in enumerate(batting_obj):
    if ind > 480:
        break
    tmp = val.text_content()
    tmp = clean_str(tmp)
    if tmp == '' or tmp == ' ' or tmp == '  ':
        continue
    if ind < len(batting_obj)-2:
        next_tmp = clean_str(batting_obj[ind+1].text_content())
    else:
        next_tmp = ''
    tmp += ","
    if ind == 27:
        tmp += "\n"
    if next_tmp != '':
        if ind > 27 and (re.match('[a-zA-Z]',next_tmp) is not None):
            tmp += "\n"
    batting_stats.append(tmp)
    
with open("batting_yanks.csv","w") as bat:
    for i in batting_stats:
        bat.write(i)
