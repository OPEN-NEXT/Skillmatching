# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:57:06 2021

@author: konierik
"""


# Python program to read 
# json file 
# more instructions: 
    #https://www.geeksforgeeks.org/json-load-in-python/
    #https://pythonexamples.org/python-read-json-file/
   
    
import json 


#file location
filepath ='C:\\Users\\konierik\\Nextcloud2\\MA-Arbeit\\03_Ontology\\Skills\\WIF_data'
userfilepath=filepath+'\\sampledata_user.json'
projectfilepath=filepath+'\\sampledata_projects.json'
issuefilepath=filepath+'\\sampledata_issues.json'

#keys to look out for
change_keys=["id","username"]
user_keys=[["data","profiles", "result", "edges", "~", "node","user"],
           ["data","profiles", "result", "edges", "~", "node","projects","edges","~","node","creator"],
           ["data","profiles", "result", "edges", "~", "node","projects","edges","~","node","contributors","edges","~", "node","user"],
           ["data","profiles", "result", "edges", "~", "node","projects","edges","~","node","tracker","issues","edges","~", "node","creator"],
           ["data","profiles", "result", "edges", "~", "node","sharedFiles","edges","~","node","participants","~"]]

project_keys=[["data","projects", "result", "edges", "~", "node","creator"],
              ["data","projects", "result", "edges", "~", "node","contributors","edges","~","node","user"],
              ["data","projects", "result", "edges", "~", "node","tracker","issues","edges","~","node", "creator"]]

issue_keys=[["data","issues", "result", "edges","~", "node","creator"],
            ["data","issues", "result", "edges","~", "node","project","creator"],
            ["data","issues", "result", "edges","~", "node","project","contributors","edges","~", "node","user"],
            ["data","issues", "result", "edges","~", "node","project", "tracker","issues","edges","~", "node","creator"],
            ["data","issues", "result", "edges","~", "node","assignees", "~"]] 
  

#dictionaries for id and username anonymization
random_id={}
random_username={}
random=[random_id,random_username]

#generating files  from the paths
userfile=open(userfilepath, encoding="utf8")
projectfile=open(projectfilepath, encoding="utf8")
issuefile=open(issuefilepath, encoding="utf8")

#loading the files as jsondata
userdata=json.load(userfile)
issuedata=json.load(issuefile)
projectdata=json.load(projectfile)

def anonymizeIssues():
    arr=issuedata[issue_keys[0][0]][issue_keys[0][1]][issue_keys[0][2]][issue_keys[0][3]]
    for index in range(len(arr)):
        creatorid=f"{ issuedata[issue_keys[0][0]][issue_keys[0][1]][issue_keys[0][2]][issue_keys[0][3]][index][issue_keys[0][5]][issue_keys[0][6]][change_keys[0]] }"
        creatorname=f"{ issuedata[issue_keys[0][0]][issue_keys[0][1]][issue_keys[0][2]][issue_keys[0][3]][index][issue_keys[0][5]][issue_keys[0][6]][change_keys[1]] }"
        newcreatorid=anonymizeID(creatorid)
        newcreatorname=anonymizeName(creatorname)
        issuedata[issue_keys[0][0]][issue_keys[0][1]][issue_keys[0][2]][issue_keys[0][3]][index][issue_keys[0][5]][issue_keys[0][6]][change_keys[0]]=newcreatorid
        issuedata[issue_keys[0][0]][issue_keys[0][1]][issue_keys[0][2]][issue_keys[0][3]][index][issue_keys[0][5]][issue_keys[0][6]][change_keys[1]]=newcreatorname
        
        creatorid2=f"{ issuedata[issue_keys[1][0]][issue_keys[1][1]][issue_keys[1][2]][issue_keys[1][3]][index][issue_keys[1][5]][issue_keys[1][6]][issue_keys[1][7]][change_keys[0]] }"
        creatorname2=f"{ issuedata[issue_keys[1][0]][issue_keys[1][1]][issue_keys[1][2]][issue_keys[1][3]][index][issue_keys[1][5]][issue_keys[1][6]][issue_keys[1][7]][change_keys[1]] }"
        newcreatorid2=anonymizeID(creatorid2)
        newcreatorname2=anonymizeName(creatorname2)
        issuedata[issue_keys[1][0]][issue_keys[1][1]][issue_keys[1][2]][issue_keys[1][3]][index][issue_keys[1][5]][issue_keys[1][6]][issue_keys[1][7]][change_keys[0]]=newcreatorid2
        issuedata[issue_keys[1][0]][issue_keys[1][1]][issue_keys[1][2]][issue_keys[1][3]][index][issue_keys[1][5]][issue_keys[1][6]][issue_keys[1][7]][change_keys[1]]=newcreatorname2
    
        arr2=issuedata[issue_keys[2][0]][issue_keys[2][1]][issue_keys[2][2]][issue_keys[2][3]][index][issue_keys[2][5]][issue_keys[2][6]][issue_keys[2][7]][issue_keys[2][8]]
        for index2 in range(len(arr2)):
            contributorid=f"{ issuedata[issue_keys[2][0]][issue_keys[2][1]][issue_keys[2][2]][issue_keys[2][3]][index][issue_keys[2][5]][issue_keys[2][6]][issue_keys[2][7]][issue_keys[2][8]][index2][issue_keys[2][10]][issue_keys[2][11]][change_keys[0]] }"
            contributorname=f"{ issuedata[issue_keys[2][0]][issue_keys[2][1]][issue_keys[2][2]][issue_keys[2][3]][index][issue_keys[2][5]][issue_keys[2][6]][issue_keys[2][7]][issue_keys[2][8]][index2][issue_keys[2][10]][issue_keys[2][11]][change_keys[1]] }"
            newcontributorid=anonymizeID(contributorid)
            newcontributorname=anonymizeName(contributorname)
            issuedata[issue_keys[2][0]][issue_keys[2][1]][issue_keys[2][2]][issue_keys[2][3]][index][issue_keys[2][5]][issue_keys[2][6]][issue_keys[2][7]][issue_keys[2][8]][index2][issue_keys[2][10]][issue_keys[2][11]][change_keys[0]]=newcontributorid
            issuedata[issue_keys[2][0]][issue_keys[2][1]][issue_keys[2][2]][issue_keys[2][3]][index][issue_keys[2][5]][issue_keys[2][6]][issue_keys[2][7]][issue_keys[2][8]][index2][issue_keys[2][10]][issue_keys[2][11]][change_keys[1]]=newcontributorname
        
        arr3=issuedata[issue_keys[3][0]][issue_keys[3][1]][issue_keys[3][2]][issue_keys[3][3]][index][issue_keys[3][5]][issue_keys[3][6]][issue_keys[3][7]][issue_keys[3][8]][issue_keys[3][9]]
        for index3 in range(len(arr3)):
            creatorid3=f"{ issuedata[issue_keys[3][0]][issue_keys[3][1]][issue_keys[3][2]][issue_keys[3][3]][index][issue_keys[3][5]][issue_keys[3][6]][issue_keys[3][7]][issue_keys[3][8]][issue_keys[3][9]][index3][issue_keys[3][11]][issue_keys[3][12]][change_keys[0]] }"
            creatorname3=f"{ issuedata[issue_keys[3][0]][issue_keys[3][1]][issue_keys[3][2]][issue_keys[3][3]][index][issue_keys[3][5]][issue_keys[3][6]][issue_keys[3][7]][issue_keys[3][8]][issue_keys[3][9]][index3][issue_keys[3][11]][issue_keys[3][12]][change_keys[1]] }"
            newcreatorid3=anonymizeID(creatorid3)
            newcreatorname3=anonymizeName(creatorname3)
            issuedata[issue_keys[3][0]][issue_keys[3][1]][issue_keys[3][2]][issue_keys[3][3]][index][issue_keys[3][5]][issue_keys[3][6]][issue_keys[3][7]][issue_keys[3][8]][issue_keys[3][9]][index3][issue_keys[3][11]][issue_keys[3][12]][change_keys[0]]=newcreatorid3
            issuedata[issue_keys[3][0]][issue_keys[3][1]][issue_keys[3][2]][issue_keys[3][3]][index][issue_keys[3][5]][issue_keys[3][6]][issue_keys[3][7]][issue_keys[3][8]][issue_keys[3][9]][index3][issue_keys[3][11]][issue_keys[3][12]][change_keys[1]]=newcreatorname3
        
        arr4=issuedata[issue_keys[4][0]][issue_keys[4][1]][issue_keys[4][2]][issue_keys[4][3]][index][issue_keys[4][5]][issue_keys[4][6]]
        for index4 in range(len(arr4)):
            assigneeid=f"{ issuedata[issue_keys[4][0]][issue_keys[4][1]][issue_keys[4][2]][issue_keys[4][3]][index][issue_keys[4][5]][issue_keys[4][6]][index4][change_keys[0]] }"
            assigneename=f"{ issuedata[issue_keys[4][0]][issue_keys[4][1]][issue_keys[4][2]][issue_keys[4][3]][index][issue_keys[4][5]][issue_keys[4][6]][index4][change_keys[1]]}"
            newassigneeid=anonymizeID(assigneeid)
            newassigneename=anonymizeName(assigneename)
            issuedata[issue_keys[4][0]][issue_keys[4][1]][issue_keys[4][2]][issue_keys[4][3]][index][issue_keys[4][5]][issue_keys[4][6]][index4][change_keys[0]]=newassigneeid
            issuedata[issue_keys[4][0]][issue_keys[4][1]][issue_keys[4][2]][issue_keys[4][3]][index][issue_keys[4][5]][issue_keys[4][6]][index4][change_keys[1]]=newassigneename
        
    return issuedata

def anonymizeUsers():
    #first entry in user_keys
    arr=userdata[user_keys[0][0]][user_keys[0][1]][user_keys[0][2]][user_keys[0][3]]
    for index in range(len(arr)):
        userid=f"{ userdata[user_keys[0][0]][user_keys[0][1]][user_keys[0][2]][user_keys[0][3]][index][user_keys[0][5]][user_keys[0][6]][change_keys[0]] }"
        username=f"{ userdata[user_keys[0][0]][user_keys[0][1]][user_keys[0][2]][user_keys[0][3]][index][user_keys[0][5]][user_keys[0][6]][change_keys[1]] }"
        newuserid=anonymizeID(userid)
        newusername=anonymizeName(username)
        userdata[user_keys[0][0]][user_keys[0][1]][user_keys[0][2]][user_keys[0][3]][index][user_keys[0][5]][user_keys[0][6]][change_keys[0]]=newuserid
        userdata[user_keys[0][0]][user_keys[0][1]][user_keys[0][2]][user_keys[0][3]][index][user_keys[0][5]][user_keys[0][6]][change_keys[1]]=newusername
        
        arr2=userdata[user_keys[1][0]][user_keys[1][1]][user_keys[1][2]][user_keys[1][3]][index][user_keys[1][5]][user_keys[1][6]][user_keys[1][7]]
        for index2 in range(len(arr2)):
            #2nd entry in user_keys
            userid2=f"{ userdata[user_keys[1][0]][user_keys[1][1]][user_keys[1][2]][user_keys[1][3]][index][user_keys[1][5]][user_keys[1][6]][user_keys[1][7]][index2][user_keys[1][9]][user_keys[1][10]][change_keys[0]] }"
            username2=f"{ userdata[user_keys[1][0]][user_keys[1][1]][user_keys[1][2]][user_keys[1][3]][index][user_keys[1][5]][user_keys[1][6]][user_keys[1][7]][index2][user_keys[1][9]][user_keys[1][10]][change_keys[1]] }"
            newuserid2=anonymizeID(userid2)
            newusername2=anonymizeName(username2)
            userdata[user_keys[1][0]][user_keys[1][1]][user_keys[1][2]][user_keys[1][3]][index][user_keys[1][5]][user_keys[1][6]][user_keys[1][7]][index2][user_keys[1][9]][user_keys[1][10]][change_keys[0]]=newuserid2
            userdata[user_keys[1][0]][user_keys[1][1]][user_keys[1][2]][user_keys[1][3]][index][user_keys[1][5]][user_keys[1][6]][user_keys[1][7]][index2][user_keys[1][9]][user_keys[1][10]][change_keys[1]]=newusername2
            
            arr3=userdata[user_keys[2][0]][user_keys[2][1]][user_keys[2][2]][user_keys[2][3]][index][user_keys[2][5]][user_keys[2][6]][user_keys[2][7]][index2][user_keys[2][9]][user_keys[2][10]][user_keys[2][11]]
            for index3 in range(len(arr3)):
                #3rd entry in user_keys
                userid3=f"{ userdata[user_keys[2][0]][user_keys[2][1]][user_keys[2][2]][user_keys[2][3]][index][user_keys[2][5]][user_keys[2][6]][user_keys[2][7]][index2][user_keys[2][9]][user_keys[2][10]][user_keys[2][11]][index3][user_keys[2][13]][user_keys[2][14]][change_keys[0]] }"
                username3=f"{ userdata[user_keys[2][0]][user_keys[2][1]][user_keys[2][2]][user_keys[2][3]][index][user_keys[2][5]][user_keys[2][6]][user_keys[2][7]][index2][user_keys[2][9]][user_keys[2][10]][user_keys[2][11]][index3][user_keys[2][13]][user_keys[2][14]][change_keys[1]] }"
                newuserid3=anonymizeID(userid3)
                newusername3=anonymizeName(username3)
                userdata[user_keys[2][0]][user_keys[2][1]][user_keys[2][2]][user_keys[2][3]][index][user_keys[2][5]][user_keys[2][6]][user_keys[2][7]][index2][user_keys[2][9]][user_keys[2][10]][user_keys[2][11]][index3][user_keys[2][13]][user_keys[2][14]][change_keys[0]]=newuserid3
                userdata[user_keys[2][0]][user_keys[2][1]][user_keys[2][2]][user_keys[2][3]][index][user_keys[2][5]][user_keys[2][6]][user_keys[2][7]][index2][user_keys[2][9]][user_keys[2][10]][user_keys[2][11]][index3][user_keys[2][13]][user_keys[2][14]][change_keys[1]]=newusername3
            
            arr4=userdata[user_keys[3][0]][user_keys[3][1]][user_keys[3][2]][user_keys[3][3]][index][user_keys[3][5]][user_keys[3][6]][user_keys[3][7]][index2][user_keys[3][9]][user_keys[3][10]][user_keys[3][11]][user_keys[3][12]]
            for index4 in range(len(arr4)):
                #4th entry in user_keys
                userid4=f"{ userdata[user_keys[3][0]][user_keys[3][1]][user_keys[3][2]][user_keys[3][3]][index][user_keys[3][5]][user_keys[3][6]][user_keys[3][7]][index2][user_keys[3][9]][user_keys[3][10]][user_keys[3][11]][user_keys[3][12]][index4][user_keys[3][14]][user_keys[3][15]][change_keys[0]] }"
                username4=f"{ userdata[user_keys[3][0]][user_keys[3][1]][user_keys[3][2]][user_keys[3][3]][index][user_keys[3][5]][user_keys[3][6]][user_keys[3][7]][index2][user_keys[3][9]][user_keys[3][10]][user_keys[3][11]][user_keys[3][12]][index4][user_keys[3][14]][user_keys[3][15]][change_keys[1]] }"
                newuserid4=anonymizeID(userid4)
                newusername4=anonymizeName(username4)
                userdata[user_keys[3][0]][user_keys[3][1]][user_keys[3][2]][user_keys[3][3]][index][user_keys[3][5]][user_keys[3][6]][user_keys[3][7]][index2][user_keys[3][9]][user_keys[3][10]][user_keys[3][11]][user_keys[3][12]][index4][user_keys[3][14]][user_keys[3][15]][change_keys[0]]=newuserid4
                userdata[user_keys[3][0]][user_keys[3][1]][user_keys[3][2]][user_keys[3][3]][index][user_keys[3][5]][user_keys[3][6]][user_keys[3][7]][index2][user_keys[3][9]][user_keys[3][10]][user_keys[3][11]][user_keys[3][12]][index4][user_keys[3][14]][user_keys[3][15]][change_keys[1]]=newusername4                                                                                                                                                                                       
        
        arr5=userdata[user_keys[4][0]][user_keys[4][1]][user_keys[4][2]][user_keys[4][3]][index][user_keys[4][5]][user_keys[4][6]][user_keys[4][7]]
        for index5 in range(len(arr5)):
            #5th entry in user_keys
            arr6=userdata[user_keys[4][0]][user_keys[4][1]][user_keys[4][2]][user_keys[4][3]][index][user_keys[4][5]][user_keys[4][6]][user_keys[4][7]][index5][user_keys[4][9]][user_keys[4][10]]
            for index6 in range(len(arr6)):
                userid5=f"{ userdata[user_keys[4][0]][user_keys[4][1]][user_keys[4][2]][user_keys[4][3]][index][user_keys[4][5]][user_keys[4][6]][user_keys[4][7]][index5][user_keys[4][9]][user_keys[4][10]][index6][change_keys[0]] }"
                username5=f"{ userdata[user_keys[4][0]][user_keys[4][1]][user_keys[4][2]][user_keys[4][3]][index][user_keys[4][5]][user_keys[4][6]][user_keys[4][7]][index5][user_keys[4][9]][user_keys[4][10]][index6][change_keys[1]] }"
                newuserid5=anonymizeID(userid5)
                newusername5=anonymizeName(username5)
                userdata[user_keys[4][0]][user_keys[4][1]][user_keys[4][2]][user_keys[4][3]][index][user_keys[4][5]][user_keys[4][6]][user_keys[4][7]][index5][user_keys[4][9]][user_keys[4][10]][index6][change_keys[0]]=newuserid5
                userdata[user_keys[4][0]][user_keys[4][1]][user_keys[4][2]][user_keys[4][3]][index][user_keys[4][5]][user_keys[4][6]][user_keys[4][7]][index5][user_keys[4][9]][user_keys[4][10]][index6][change_keys[1]]=newusername5                                                                                                                                                                                     
                
    return userdata

def anonymizeProjects():
    arr=projectdata[project_keys[0][0]][project_keys[0][1]][project_keys[0][2]][project_keys[0][3]]
    for index in range(len(arr)):
        creatorid=f"{ projectdata[project_keys[0][0]][project_keys[0][1]][project_keys[0][2]][project_keys[0][3]][index][project_keys[0][5]][project_keys[0][6]][change_keys[0]] }"
        creatorname=f"{ projectdata[project_keys[0][0]][project_keys[0][1]][project_keys[0][2]][project_keys[0][3]][index][project_keys[0][5]][project_keys[0][6]][change_keys[1]] }"
        newcreatorid=anonymizeID(creatorid)
        newcreatorname=anonymizeName(creatorname)
        projectdata[project_keys[0][0]][project_keys[0][1]][project_keys[0][2]][project_keys[0][3]][index][project_keys[0][5]][project_keys[0][6]][change_keys[0]]=newcreatorid
        projectdata[project_keys[0][0]][project_keys[0][1]][project_keys[0][2]][project_keys[0][3]][index][project_keys[0][5]][project_keys[0][6]][change_keys[1]]=newcreatorname
        
        arr2=projectdata[project_keys[1][0]][project_keys[1][1]][project_keys[1][2]][project_keys[1][3]][index][project_keys[1][5]][project_keys[1][6]][project_keys[1][7]]
       
        for index2 in range(len(arr2)):
            contributorid=f"{ projectdata[project_keys[1][0]][project_keys[1][1]][project_keys[1][2]][project_keys[1][3]][index][project_keys[1][5]][project_keys[1][6]][project_keys[1][7]][index2][project_keys[1][9]][project_keys[1][10]][change_keys[0]] }"
            contributorname=f"{ projectdata[project_keys[1][0]][project_keys[1][1]][project_keys[1][2]][project_keys[1][3]][index][project_keys[1][5]][project_keys[1][6]][project_keys[1][7]][index2][project_keys[1][9]][project_keys[1][10]][change_keys[1]] }"
            newcontributorid=anonymizeID(contributorid)
            newcontributorname=anonymizeName(contributorname)
            projectdata[project_keys[1][0]][project_keys[1][1]][project_keys[1][2]][project_keys[1][3]][index][project_keys[1][5]][project_keys[1][6]][project_keys[1][7]][index2][project_keys[1][9]][project_keys[1][10]][change_keys[0]]=newcontributorid
            projectdata[project_keys[1][0]][project_keys[1][1]][project_keys[1][2]][project_keys[1][3]][index][project_keys[1][5]][project_keys[1][6]][project_keys[1][7]][index2][project_keys[1][9]][project_keys[1][10]][change_keys[1]]=newcontributorname
        
        arr3=projectdata[project_keys[2][0]][project_keys[2][1]][project_keys[2][2]][project_keys[2][3]][index][project_keys[2][5]][project_keys[2][6]][project_keys[2][7]][project_keys[2][8]]
       
        for index3 in range(len(arr3)):
            creatorid2=f"{ projectdata[project_keys[2][0]][project_keys[2][1]][project_keys[2][2]][project_keys[2][3]][index][project_keys[2][5]][project_keys[2][6]][project_keys[2][7]][project_keys[2][8]][index3][project_keys[2][10]][project_keys[2][11]][change_keys[0]] }"
            creatorname2=f"{ projectdata[project_keys[2][0]][project_keys[2][1]][project_keys[2][2]][project_keys[2][3]][index][project_keys[2][5]][project_keys[2][6]][project_keys[2][7]][project_keys[2][8]][index3][project_keys[2][10]][project_keys[2][11]][change_keys[1]] }"
            newcreatorid2=anonymizeID(creatorid2)
            newcreatorname2=anonymizeName(creatorname2)
            projectdata[project_keys[2][0]][project_keys[2][1]][project_keys[2][2]][project_keys[2][3]][index][project_keys[2][5]][project_keys[2][6]][project_keys[2][7]][project_keys[2][8]][index3][project_keys[2][10]][project_keys[2][11]][change_keys[0]]=newcreatorid2
            projectdata[project_keys[2][0]][project_keys[2][1]][project_keys[2][2]][project_keys[2][3]][index][project_keys[2][5]][project_keys[2][6]][project_keys[2][7]][project_keys[2][8]][index3][project_keys[2][10]][project_keys[2][11]][change_keys[1]]=newcreatorname2
    
    return projectdata


         
def anonymizeID(id):
    if id in random_id:
        return random_id.get(id)
    else:
        uid="uid"+str(len(random_id)) #alternative uuid.uuid4()
        random_id[id]=uid
        return uid
    
def anonymizeName(name):
    if name in random_username:
        return random_username.get(name)
    else:
        uname="USER"+str(len(random_username)) #alternative uuid.uuid4()
        random_username[name]=uname
        return uname

def saveJsonFile(obj, path):
    with open(path, "w") as f:
        json.dump(obj,f,indent=4)
    f.close() 
    


newusers= anonymizeUsers()
newuserfilepath=filepath+'\\sampledata_user_anonym.json'
saveJsonFile(newusers,newuserfilepath)

newissues=anonymizeIssues()
newissuefilepath=filepath+'\\sampledata_issues_anonym.json'
saveJsonFile(newissues,newissuefilepath)

newprojects=anonymizeProjects()
newprojectfilepath=filepath+'\\sampledata_projects_anonym.json'
saveJsonFile(newprojects,newprojectfilepath)



def getID(data,arr):
    val=data
    #print(f"value= : {val}")
    for i in range(len(arr)):
        print(i)
        if arr[i]=="~":
            for j in range(len(val)):
                arr[i]=j
                getID(val,arr[i:len(arr)])
        elif arr[i]!="~": 
           try: val=val[arr[i]]
           except: print("Did not work")
    print(f"value: {val}") 