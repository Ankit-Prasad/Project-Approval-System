import sqlite3
import hashlib
import os


def set_password(raw_password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', raw_password.encode('utf-8'), salt, 100000)
    password = salt + key
    return password

def check_password(raw_password, enc_password):
    salt = enc_password[:32]
    key = enc_password[32:]
    new_key = hashlib.pbkdf2_hmac('sha256', raw_password.encode('utf-8'), salt, 100000)
    return new_key == key

def student_login(roll_number,user_password):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    crsr.execute('SELECT Password FROM Student WHERE Roll_No = ?', [str(roll_number)])
    record = crsr.fetchone()
    password = record
    if password == None or len(password) == 0 or len(password[0]) == 0 or check_password(user_password,password[0]) == False:
        return False
    return True
    crsr.close()
    connection.close()

def student_register(name,roll_number,email,password,):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    ciphered_password = set_password(password)
    user_id = crsr.execute('INSERT or IGNORE INTO Student(Roll_No,Name,Email,Password) values(?,?,?,?)',(roll_number,name,email,ciphered_password))
    connection.commit()
    affected_rows = format(crsr.rowcount)
    if int(affected_rows) == 0:
        return False
    return True
    crsr.close()
    connection.close()


def faculty_register(fid,name,email,password,):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    ciphered_password = set_password(password)
    user_id = crsr.execute('INSERT or IGNORE INTO Faculty(F_Id,F_Name,Email,Password) values(?,?,?,?)',(fid,name,email,ciphered_password))
    connection.commit()
    affected_rows = format(crsr.rowcount)
    if int(affected_rows) == 0:
         return False
    return True
    crsr.close()
    connection.close()

def faculty_login(F_Id,user_password):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    crsr.execute('SELECT Password FROM Faculty WHERE F_Id = ?', [str(F_Id)])
    record = crsr.fetchone()
    password = record
    if password == None or len(password) == 0 or len(password[0]) == 0 or check_password(user_password,password[0]) == False:
        return False
    return True
    crsr.close()
    connection.close

def ta_login(roll_number,user_password):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    crsr.execute('SELECT Password FROM Student WHERE EXISTS(SELECT * FROM TA WHERE Roll_No = ?)  AND  Roll_No = ?',[str(roll_number),str(roll_number)])
    record = crsr.fetchone()
    password = record
    if password == None or len(password) == 0 or len(password[0]) == 0 or check_password(user_password,password[0]) == False:
        return False
    return True
    crsr.close()
    connection.close()    

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def uploadProjectDetails(course,pt,member_1,member_2,member_3,member_4,faculty):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()

    result = crsr.execute('DELETE FROM PROJECT WHERE Course_Id = ? AND EXISTS(SELECT * FROM Project WHERE Member_1 =? OR Member_2=? OR Member_3=? OR Member_4=?)',(course,member_1,member_2,member_3,member_4))

    project =crsr.execute('INSERT or IGNORE INTO Project(Course_Id,Member_1,Member_2,Member_3,Member_4,Project_Name,F_Id) values(?,?,?,?,?,?,?)',(course,member_1,member_2,member_3,member_4,pt,faculty))
    connection.commit()
    crsr.close()
    connection.close()
    return True

def getGroup_Id(pt):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT Group_Id FROM Project WHERE Project_Name = ?',[str(pt)]):
        results.append([row])
    crsr.close()
    connection.close()
    return results 

def course_dropdown(roll_number):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT * FROM COURSE WHERE COURSE_ID IN (SELECT COURSE_ID FROM Student_Course WHERE Roll_No = ?)', [str(roll_number)]):
        results.append([row])
    crsr.close()
    connection.close()
    return results

def facCourseDropdown(F_Id):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT * FROM COURSE WHERE COURSE_ID IN (SELECT COURSE_ID FROM Faculty_Course WHERE F_Id = ?)', [str(F_Id)]):
        results.append([row])
    crsr.close()
    connection.close()
    return results

def getProjectList(username,course):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT Group_Id,Project_Name,Response FROM Project WHERE F_Id = ? AND Course_Id=?',(username,course)):
        results.append([row])
    crsr.close()
    connection.close()
    return results    

def writeTofile(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


def update_status(Group_Id):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    crsr.execute('SELECT Group_Id,Course_Id,Member_1,Member_2,Member_3,Member_4,Project_Name,F_Id FROM Project WHERE Group_Id = ?',[(Group_Id)])
    record = crsr.fetchall()
    for row in record:
        results.append([row])    
    crsr.close()
    connection.close()
    return results

def findTA(course):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT Roll_No,Name FROM Student WHERE Roll_No IN (SELECT Roll_No FROM TA WHERE Course_Id = ?)',[str(course)]):
        results.append([row])
    crsr.close()
    connection.close()
    return results

def UpdateProject(Group_Id,status,Suggestion,TA):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    user_id = crsr.execute('UPDATE Project SET Response = ?,Suggestion = ?,TA = ? WHERE Group_Id = ?',(status,Suggestion,TA,Group_Id))
    user_id = crsr.execute('INSERT or IGNORE INTO TA_Proj(Group_Id,TA_Id) values(?,?)',(Group_Id,TA))
    connection.commit()
    return True
    crsr.close()
    connection.close()
    


def getTAprojects(roll_number):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT Group_Id,Project_Name FROM Project WHERE TA = ?',[str(roll_number)]):
        results.append([row])
    crsr.close()
    connection.close()
    return results    

def update_TA_Project(username,Group_Id,Suggestion):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    user_id = crsr.execute('UPDATE TA_Proj SET TA_Suggestion = ? WHERE Group_Id = ?',(Suggestion,Group_Id))
    connection.commit()
    return True
    crsr.close()
    connection.close()

def ViewFacultyResponse(username,course):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results =[]
    for row in crsr.execute('SELECT Response,Suggestion FROM Project WHERE Course_Id = ? AND (Member_1=? OR Member_2=? OR Member_3=? OR Member_4=?)',(course,username,username,username,username)):
        results.append([row])
    print(results) 
    return results 
    crsr.close()
    connection.close()


def ViewTaResponse(username,course):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT TA_SUGGESTION FROM TA_Proj WHERE Group_Id IN (SELECT Group_Id FROM Project WHERE Course_Id = ? AND (Member_1=? OR Member_2=? OR Member_3=? OR Member_4=?))',(course,username,username,username,username)):
        results.append([row])
    return results
    crsr.close()
    connection.close()



def selectFaculty(course):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results = []
    for row in crsr.execute('SELECT F_Name, F_Id FROM Faculty WHERE F_Id IN (SELECT F_Id FROM Faculty_Course WHERE Course_Id = ?)',[str(course)]):
        results.append([row])
    crsr.close()
    connection.close()
    return results    

def checkProjectExist(username,c_id):
    connection = sqlite3.connect('project_approval.db')
    crsr = connection.cursor()
    results =[]
    for row in crsr.execute('SELECT Group_Id FROM Project WHERE Course_Id=? AND (Member_1=? OR Member_2=? OR Member_3=? OR Member_4=?)',(c_id,username,username,username,username)):
        results.append([row])
    if not results:
        return False
    else:
        return True        
    crsr.close()
    connection.close()


       
