import services
import sqlite3
import hashlib
import os

conn = sqlite3.connect('project_approval.db')
print ('''Opened database successfully''');
# conn.execute('''DROP TABLE Project;''')
# conn.execute('''DROP TABLE User;''')
#conn.execute('''DROP TABLE Student_Course;''')
# conn.execute('''DROP TABLE TA_Proj;''')


conn.execute('''CREATE TABLE  IF NOT EXISTS Student
         (Roll_No varchar(12) PRIMARY KEY,
         Name  varchar(50)    NOT NULL,
         Email varchar(50) UNIQUE,
         Password BLOB NOT NULL
         )
         ;''')

conn.execute('''CREATE TABLE IF NOT EXISTS Course(
              Course_Id VARCHAR(12) PRIMARY KEY,
              Course_Name VARCHAR(80) NOT NULL
              )
           ;''')


conn.execute('''CREATE TABLE IF NOT EXISTS  Faculty
         (
          F_Id VARCHAR(20) PRIMARY KEY,
          F_Name VARCHAR(50) NOT NULL,
          Email VARCHAR(50) UNIQUE,
          Password BLOB NOT NULL
         )
         ;''')

conn.execute('''CREATE TABLE IF NOT EXISTS Faculty_Course(
              Course_Id VARCHAR(12),
              F_Id VARCHAR(50),
              FOREIGN KEY(F_Id) REFERENCES Faculty(F_Id),
              FOREIGN KEY(Course_Id) REFERENCES Course(Course_Id)
              )
           ;''')
conn.execute('''CREATE TABLE IF NOT EXISTS TA
         (
          Roll_No varchar(10) ,
          Course_Id varchar(12), 
          FOREIGN KEY(Roll_No) REFERENCES Student(Roll_No),
          FOREIGN KEY(Course_Id) REFERENCES Course(Course_Id)
         )
         ;''')
conn.execute('''CREATE TABLE IF NOT EXISTS Student_Course
         (
          Roll_No varchar(10) ,
          Course_Id varchar(12), 
          FOREIGN KEY(Roll_No) REFERENCES Student(Roll_No),
          FOREIGN KEY(Course_Id) REFERENCES Course(Course_Id)
         )
         ;''')
conn.execute('''CREATE TABLE IF NOT EXISTS Project
         (
          Group_Id INTEGER PRIMARY KEY AUTOINCREMENT,
          Course_Id varchar(12) NOT NULL,
          Member_1 varchar(12) NOT NULL,
          Member_2 varchar(12) NOT NULL,
          Member_3 varchar(12) NOT NULL,
          Member_4 varchar(12) NOT NULL, 
          Project_Name varchar(30) NOT NULL,
          Proposal_Doc BLOB ,
          GitHub varchar(255) UNIQUE,
          F_Id varchar(20) NOT NULL,
          Response varchar(10) DEFAULT "Pending" ,
          Suggestion varchar(255) DEFAULT "Pending",
          TA varchar(10),

          FOREIGN KEY(Member_1) REFERENCES Student(Roll_No),
          FOREIGN KEY(Member_2) REFERENCES Student(Roll_No),
          FOREIGN KEY(Member_3) REFERENCES Student(Roll_No),
          FOREIGN KEY(Member_4) REFERENCES Student(Roll_No)
          FOREIGN KEY(Course_Id) REFERENCES Course(Course_Id),
          FOREIGN KEY(TA) REFERENCES TA(Roll_No)
          FOREIGN KEY(F_Id) REFERENCES Faculty(F_Id)
         )
         ;''')

conn.execute('''CREATE TABLE IF NOT EXISTS TA_Proj
         (
          Group_Id varchar(10) PRIMARY KEY,
          TA_Id varchar(12) NOT NULL,
          TA_SUGGESTION varchar(255) DEFAULT "Pending",
          FOREIGN KEY(TA_ID) REFERENCES Student(Roll_No),
          FOREIGN KEY(Group_Id) REFERENCES Project(Group_Id) ON DELETE CASCADE
         )
         ;''')



password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019013','Aishwarya Panicker','Aishwarya.Panicker@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019019','Aniruddha Trivedi','Aniruddha.Trivedi@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019020','Ankit Prasad','Ankit.Prasad@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019022','Anmol Jain','Anmol.Jain022@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019027','Arth Gupta','Arth.Gupta@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019069','Nidhi Budhraja','Nidhi.Budhraja@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019092','Ritik Kakwani','Ritik.Kakwani@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019102','Shikha Vyas','Shikha.Vyas@iiitb.org',?);''', (password,))


password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019111','Smit Limbani','Smit.Limbani@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019115','Srishti Adil','Srishti.Adil@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019123','Tarun Kumar Rai','TarunKumar.Rai@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019128','Uttkarsh Jha','Uttkarsh.Jha@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2019132','Varun Agrawal','Varun.Agrawal@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2018018','Ansh Goyal','Ansh.Goyal@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2018039','Harsh Tripathi','Harsh.Tripathi@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('MT2018092','Rakesh Kumar','Rakesh.Kumar@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('IMT2016117','Aarushi Mohania','Aarushi.Mohania@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('IMT2016003','Vibhav Agarwal','Vibhav.Agarwal@iiitb.org',?);''', (password,))

password = services.set_password('1234')
conn.execute('''INSERT INTO Student(Roll_No, Name, Email,Password) VALUES('IMT2016025','Akshi','Akshi@iiitb.org',?);''', (password,))




# COURSE TABLE

conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-19-DN615','Techno-Economics of Networks');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-19-DS823','Automatic Speech Recognition');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-19-CS816','Software Production Engineering');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-19-CD817','Optimization,Learning & Cognition');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-CS/NC824','Cyber Security Fundamentals with tools and techniques for defense');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-DS603','Data Modeling');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-DS703','Geographic Information Systems');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-NC601','Wireless Access Networks');''')
conn.execute('''INSERT INTO Course(Course_Id, Course_Name) VALUES('T2-CS/DS704','Multi-Agent Systems');''')



# STUDENT_COURSE TABLE

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019013','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019013','T2-CS/NC824');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019013','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019013','T2-19-DS823');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019019','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019019','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019019','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019019','T2-19-CD817');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019020','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019020','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019020','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019020','T2-19-CD817');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019022','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019022','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019022','T2-19-CS816');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019027','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019027','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019027','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019027','T2-19-CD817');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019069','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019069','T2-DS603');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019069','T2-DS703');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019092','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019092','T2-DS603');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019092','T2-NC601');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019102','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019102','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019102','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019102','T2-19-CD817');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019111','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019111','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019111','T2-19-CS816');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019115','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019115','T2-CS/DS704');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019115','T2-19-DN615');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019115','T2-NC601');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019123','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019123','T2-CS/DS704');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019123','T2-CS/NC824');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019123','T2-19-DN615');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019128','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019128','T2-CS/DS704');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019128','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019128','T2-19-DN615');''')

conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019132','T2-19-CS816');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019132','T2-CS/DS704');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019132','T2-19-DS823');''')
conn.execute('''INSERT INTO Student_Course(Roll_No, Course_Id) VALUES('MT2019132','T2-19-DN615');''')


# FACULTY TABLE

password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('001','Prof V Sridhar','vsridhar@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('002','Prof V Ramasubramanian','v.ramasubramanian@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('003','Prof B Thangaraju','b.thangaraju@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('004','Prof G N S Prasanna','gnsprasanna@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('005','Prof Harish Ramani','harishramani@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('006','Prof Mohanram C','mohanramc@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('007','Prof Chandrashekar Ramanathan','rc@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('008','Prof Uttam Kumar','uttamkumar@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('009','Prof Debabrata Das','debabratadas@iiitb.ac.in',?);''', (password,))
password = services.set_password('1234')
conn.execute('''INSERT INTO Faculty(F_Id, F_Name, Email, Password) VALUES('010','Prof Srinath Srinivasa','srinathsrinivasa@iiitb.ac.in',?);''', (password,))


# FAULTY_COURSE TABLE

conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-19-DN615','001');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-19-DS823','002');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-19-CS816','003');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-19-CD817','004');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-CS/NC824','005');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-CS/NC824','006');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-DS603','007');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-DS703','008');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-NC601','009');''')
conn.execute('''INSERT INTO Faculty_Course(Course_Id, F_Id) VALUES('T2-CS/DS704','010');''')


# TA TABLE

#SPE
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2018018','T2-19-CS816');''')
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2018039','T2-19-CS816');''')
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2018092','T2-19-CS816');''')
#TECHNO
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('IMT2016117','T2-19-DN615');''')
#ASR
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('IMT2016003','T2-19-DS823');''')
#OLC
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('IMT2016025','T2-19-CD817');''')
#CYBER SEC
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2019123','T2-CS/NC824');''')
#DM
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2019092','T2-DS603');''')
#GIS
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2019069','T2-DS703');''')
#WAN
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2019115','T2-NC601');''')
#MAS
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2019128','T2-CS/DS704');''')
conn.execute('''INSERT INTO TA(Roll_No, Course_Id) VALUES('MT2019132','T2-CS/DS704');''')





conn.commit()
conn.close()

print ('''Tables created successfully''');


