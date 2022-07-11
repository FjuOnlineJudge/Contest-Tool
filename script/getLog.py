import re
from bs4 import BeautifulSoup

def listToStr(list):
    return "".join(list)

log = []
L, R = 1, 2

for pageCount in range(L, R):
        with open("%d.html"%(pageCount), encoding="utf-8") as f:
            soup = BeautifulSoup(f, 'html.parser')
            table = soup.find("table", id="DataTables_Table_0")
            for row in table.find_all("tr"):
                row = row.text.replace("\n",",").split(",")
                time = listToStr(row[2:3]).replace(" ","")
                user = listToStr(row[3:4]).replace(" ","")
                if user.find("team") == -1:
                    continue
                action = listToStr(row[5:6])
                if action.find("submission") != -1:
                    log.append("%s,%s,submission,"%(user,time))
                ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",action)
                if ip:
                    log.append("%s,%s,login,%s"%(user,time,ip.group()))

with open("out/log.csv","w",encoding="utf-8") as f:
    for item in log:
        f.write(item+'\n')