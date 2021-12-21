# origin idea: https://github.com/spotboard/domjudge-converter
from datetime import datetime
import json
import requests
from requests.auth import HTTPBasicAuth

class domjudgeConverter:
    # admin or jury account
    def init(self):
        self.apiServer = "http://%s/api/v4"%("")
        self.cid = 1
        self.juryName = ""
        self.juryPassword = ""
        self.dest = '.'

    def loadApi(self):
        domjudge_info = requests.get("%s"%(self.apiServer), auth=HTTPBasicAuth(self.juryName, self.juryPassword), headers={'User-Agent': 'Mozilla'})
        domjudge_info = json.loads(domjudge_info.text)
        self.domjudgeVersion = domjudge_info.get("domjudge_version", "")

    def loadConfig(self):
        config = requests.get("%s/config"%(self.apiServer), auth=HTTPBasicAuth(self.juryName, self.juryPassword), headers={'User-Agent': 'Mozilla'})
        config = json.loads(config.text)
        self.config = []
        self.config.append(config)
    
    def loadContest(self):
        contest = requests.get("%s/contests/%d"%(self.apiServer,self.cid), auth=HTTPBasicAuth(self.juryName, self.juryPassword), headers={'User-Agent': 'Mozilla'})
        contest = json.loads(contest.text)
        self.contest = contest
        
        startTime = datetime.fromisoformat(self.contest["start_time"])
        endTime = datetime.fromisoformat(self.contest["end_time"])
        curTime = datetime.now()
        if curTime.timestamp() > endTime.timestamp():
            self.elapsedTimeinSec = int(endTime.timestamp() - startTime.timestamp())
        else:
            self.elapsedTimeinSec = int(curTime.timestamp() - startTime.timestamp())


    def loadTeams(self):
        data = requests.get("%s/contests/%d/teams"%(self.apiServer,self.cid), auth=HTTPBasicAuth(self.juryName, self.juryPassword), headers={'User-Agent': 'Mozilla'})
        data = json.loads(data.text)
        teams = []
        for d in data:
            teams.append({"id": int(d["id"]), "name": d["name"], "group": d["affiliation"]})
        self.teams = teams

    def loadProblems(self):
        data = requests.get("%s/contests/%d/problems"%(self.apiServer,self.cid), auth=HTTPBasicAuth(self.juryName, self.juryPassword), headers={'User-Agent': 'Mozilla'})
        data = json.loads(data.text)
        problems = []
        for d in data:
            problems.append({"id": int(d["id"]), "title": d["name"], "name": d["short_name"], "color": d["color"]})
        self.problems = problems

    def loadSubmissions(self):
        data = requests.get("%s/contests/%d/submissions"%(self.apiServer,self.cid), auth=HTTPBasicAuth(self.juryName, self.juryPassword), headers={'User-Agent': 'Mozilla'})
        data = json.loads(data.text)
        submissions = []
        for d in data:
            if d["contest_time"][0] == "-":
                continue
            submissionTime = d["contest_time"].split(":")
            submissions.append({"id": int(d["id"]), "team": int(d["team_id"]), "problem": int(d["problem_id"]), "result": "", "submissionTime": int(submissionTime[0]) * 60 + int(submissionTime[1])})

        data = requests.get("%s/contests/%d/judgements"%(self.apiServer,self.cid), auth=HTTPBasicAuth(self.juryName, self.juryPassword), headers={'User-Agent': 'Mozilla'})
        data = json.loads(data.text)
        judgements = []
        for d in data:
            judgements.append({"submission_id": d["submission_id"], "valid": d["valid"], "result": d["judgement_type_id"]})
        
        transform = {}
        for judgement in judgements:
            if judgement["valid"] == True:
                transform[judgement["submission_id"]] = judgement
        
        resultMap = {"AC": "Yes", "NO": "No - Other", "PE": "No - Wrong Answer", "WA": "No - Wrong Answer", "TLE": "No - Time Limit Exceeded", "RTE": "No - Run-time Error", "OLE": "No - Output Limit Exceeded", "MLE": "No - Run-time Error", "CE": "No - Compilation Error"}
        for submission in submissions:
            judgement = transform.get(str(submission["id"]), None)
            if judgement == None:
                submission["result"] = ""
            elif resultMap[judgement["result"]] is not None:
                submission["result"] = resultMap[judgement["result"]]
            else:
                submission["result"] = judgement["result"]

        def isnotCE(submission):
            return submission["result"] != "No - Compilation Error"
        
        if self.contest["penalty_time"] != 0:
            submissions = [submission for submission in submissions if isnotCE(submission)]
        self.submissions = submissions
    
    def writeContest(self):
        contest = []
        contest.append({"title": self.contest["formal_name"], "systemName": "DOMjudge", "systemVersion": self.domjudgeVersion, "problems": self.problems, "teams": self.teams})
        with open('%s/contest.json'%(self.dest), 'w', encoding='utf8') as fp:
            json.dump(contest[0],fp,indent=4, ensure_ascii=False)

    def writeRuns(self):
        runs = []
        runs.append({"time":{"contestTime": self.elapsedTimeinSec, "noMoreUpdate": False, "timestamp": 0,}, "runs": self.submissions})
        with open('%s/runs.json'%(self.dest), 'w', encoding='utf8') as fp:
            json.dump(runs[0],fp,indent=4, ensure_ascii=False)

    def run(self):
        self.init()
        self.loadApi()
        self.loadConfig()
        self.loadContest()
        self.loadTeams()
        self.loadProblems()
        self.loadSubmissions()
        self.writeContest()
        self.writeRuns()
        
converter = domjudgeConverter()
converter.run()