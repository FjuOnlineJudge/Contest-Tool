import base64
import json
import os
import requests
import subprocess
from requests.auth import HTTPBasicAuth

# parameter
server = ""
contest_id = 1
adminName = ""
adminPassword = ""
onlyCorrectCode = True
L, R = 1,100

# get the correct code ID
if onlyCorrectCode:
    judgements = requests.get("http://%s/api/v4/contests/%d/judgements"%(server,contest_id), auth=HTTPBasicAuth(adminName, adminPassword), headers={'User-Agent': 'Mozilla'})
    print(judgements.status_code)
    judgements = json.loads(judgements.text)
    AC = []
    for j in judgements:
        if j["judgement_type_id"] == "AC":
            AC.append(j["submission_id"])

# get the submissions' information in json format
submissions = requests.get("http://%s/api/v4/contests/%d/submissions?strict=false"%(server,contest_id), auth=HTTPBasicAuth(adminName, adminPassword), headers={'User-Agent': 'Mozilla'})
submissions = json.loads(submissions.text)

# make and change to "submit" folder
try:
    os.mkdir("submits")
except:
    pass

os.chdir("submits")

# map problem ID to alphabet
problemDict = {"4":"A","5":"E","6":"F","7":"D","8":"G","9":"C","10":"B"}

# download code
for s in submissions:
    if s["language_id"] == "python3":
        s["language_id"] = "py"
    tid = s["team_id"]
    
    try:
        os.mkdir(str(tid))
    except:
        pass

    if onlyCorrectCode and (s["id"] not in AC):
        continue

    submit = requests.get("http://%s/api/v4/contests/%d/submissions/%s/source-code"%(server,contest_id,s["id"]), auth=HTTPBasicAuth(adminName, adminPassword),headers={"accept":"application/json","Authorization":"Basic xxxxx"})
    submit = json.loads(submit.text)[0]
    
    with open("%s\%s_%s.%s"%(s["team_id"],problemDict[s["problem_id"]],s["id"],s["language_id"]),"wb") as f:
        f.write(base64.b64decode(submit["source"]))
    
    print("Success download code with id=%s"%s["id"])

# compress every participant's code
for id in range(L,R):
    path = "./" + str(id)
    if os.path.isdir(path):
        subprocess.call("zip -r " + str(id) + ".zip " + path)
