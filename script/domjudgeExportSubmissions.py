import base64
import json
import os
import requests
import subprocess
from requests.auth import HTTPBasicAuth

# parameter
server = ""
adminPassword = ""

def getSpecificResultSubmission(cid, submission, result):
    judgements = json.loads(requests.get("http://%s/api/v4/contests/%d/judgements"%(server,cid), auth=HTTPBasicAuth(adminName, adminPassword), headers={'User-Agent': 'Mozilla'}).text)
    sid = [j["submission_id"] for j in list(filter(lambda j: j["judgement_type_id"] == result, judgements))]
    submission = list(filter(lambda s: s["id"] in sid, submission))
    return submission

def downloadCode(cid, category = 0, originID = 0, onlyAC=False):
    # category: 0-> by team, 1-> by problem

    submissions = json.loads(requests.get("http://%s/api/v4/contests/%d/submissions?strict=false"%(server,cid), auth=HTTPBasicAuth(adminName, adminPassword), headers={'User-Agent': 'Mozilla'}).text)
    submissions = getSpecificResultSubmission(cid, submissions, "AC") if onlyAC else submissions
    problems = json.loads(requests.get("http://%s/api/v4/contests/%d/problems"%(server,cid), auth=HTTPBasicAuth(adminName, adminPassword), headers={'User-Agent': 'Mozilla'}).text)
    problemDict = {d["id"]: d["short_name"] for d in problems} if originID else {d["id"]: d["label"] for d in problems}

    folderList = list(set([problemDict[s["problem_id"]] for s in submissions] if category == 1 else [s["team_id"] for s in submissions]))
    for folder in folderList:
        try:
            os.mkdir(folder)
        except:
            pass

    for s in submissions:
        s["language_id"] = "py" if s["language_id"] == "python3" else s["language_id"]
        filename = "%s/%s_%s.%s"%(problemDict[s["problem_id"]],s["team_id"],s["id"],s["language_id"]) if category == 1 else "%s/%s_%s.%s"%(s["team_id"],problemDict[s["problem_id"]],s["id"],s["language_id"])

        submit = json.loads(requests.get("http://%s/api/v4/contests/%d/submissions/%s/source-code"%(server,cid,s["id"]), auth=HTTPBasicAuth(adminName, adminPassword),headers={"accept":"application/json","Authorization":"Basic xxxxx"}).text)[0]

        with open(filename, "wb") as f:
            f.write(base64.b64decode(submit["source"]))
        
        print("Success download code with id=%s"%s["id"])

def compressFolder(L,R):    
    teamId = set()
    for cid in range(L,R):
        teams = json.loads(requests.get("http://%s/api/v4/contests/%d/teams"%(server,cid), auth=HTTPBasicAuth(adminName, adminPassword), headers={'User-Agent': 'Mozilla'}).text)
        for t in teams:
            teamId.add(f'{t["id"]}')

    for id in teamId:
        path = "./" + id
        if os.path.isdir(path):
            subprocess.call("zip -r 1112_comp_2_" + str(id) + ".zip " + path)

def getTeamInfo(L,R):
    teamId = set()
    for cid in range(L,R):
        teams = json.loads(requests.get("http://%s/api/v4/contests/%d/teams"%(server,cid), auth=HTTPBasicAuth(adminName, adminPassword), headers={'User-Agent': 'Mozilla'}).text)
        for t in teams:
            teamId.add(f'{t["id"]}_{t["name"]}')

    teamId = sorted(teamId)
    for item in teamId:
        print(item)
    

if __name__ == '__main__':
    try:
        os.mkdir("out/submits")
    except:
        pass
    os.chdir("out/submits")
