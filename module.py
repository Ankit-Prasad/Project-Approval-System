import services
import os
from flask import Flask, render_template ,request, url_for,flash,session,jsonify,redirect,send_file
from werkzeug.utils import secure_filename
import logging
import json_log_formatter

ALLOWED_EXTENSIONS = set(['pdf'])


formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='log/app_log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('__name__')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


app = Flask(__name__)
app.secret_key = "jhjdgshaklkjfd"
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/firstpage',methods=['POST'])
def firstpage():
    logger.info('On Homepage')
    mode = request.form['mode']
    if mode == "student":
        logger.info('Student Option Selected')
        return render_template('student_login.html')
    elif mode == "faculty":
        logger.info('Faculty Option Selected')
        return render_template('faculty_login.html')
    else:
        logger.info('TA Option Selected')
        return render_template('ta_login.html')

@app.route('/student_login', methods=['POST'])
def student_login():
    logger.info('On Student Login Page')
    roll_number = request.form['roll_number']
    user_password = request.form['psw']
    status = services.student_login(roll_number, user_password)
    logger.info('Student Logging In')
    if (status == True):
        logger.info('Student Login Successful')
        session['username'] = roll_number
        if(check()):
            results = services.course_dropdown(roll_number)
            logger.info('On Student Course Page')
            return render_template('student_course.html',username=session['username'],results=results)

    else:
        logger.warning('Student Login Failed')
        logger.info('Going Back to Homepage')
        return render_template('firstpage.html')

@app.route('/registers')
def registers():
    logger.info('On Student Register Page')
    return render_template("student_register.html")

@app.route('/student_register',methods=['POST'])
def student_register():
    name = request.form['name']
    roll_number = request.form['roll_number']
    email = request.form['email']
    password = request.form['psw']
    mode = request.form['mode']

    if mode == "Signup":
        logger.info('Registering New Student')
        success = services.student_register(name,roll_number,email,password)
        if (success == True):
            logger.info('Registration Successful')
            session['username'] = roll_number
            if(check()):
                logger.info('Student Logged In')
                logger.info('On Student Course Page')
                return render_template('student_course.html',username=session['username'])
        else:
            logger.error('Registratin Failed - Duplicate Email')
            logger.info('Going Back To Homepage')
            return render_template('firstpage.html')
    else:
        logger.info('On Student Login Page')
        return render_template('student_login.html')    


@app.route('/student_course',methods=['POST'])
def student_course():
    c_id = request.form['course']
    success = services.checkProjectExist(session['username'],c_id)
    if (success == True):
        submit = "You have submitted a project for review"
    else:
        submit = ""
    logger.info('On Student Dashboard')    
    return render_template('student_dashboard.html',course=c_id,submit=submit)
    


@app.route('/uploadproject',methods=['GET','POST'])
def uploadproject():
    course = request.args.get('course') 
    faculty = services.selectFaculty(course)
    logger.info('On Project Details Page')
    return render_template('project_details.html',course=course,faculty=faculty)
    
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploadProjectDetails',methods=['GET','POST'])
def uploadProjectDetails():
    course = request.args.get('course')
    pt = request.form['Title']
    member_1 = request.form['member_1']
    member_2 = request.form['member_2']
    member_3 = request.form['member_3']
    member_4 = request.form['member_4']
    file = request.files['filename']
    faculty = request.form['faculty']
    success = services.uploadProjectDetails(course,pt,member_1,member_2,member_3,member_4,faculty)
    results = services.getGroup_Id(pt)
    result = results[0][0]
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = str(result[0])+'.pdf'
            basedir = os.path.abspath(os.path.dirname(__file__))
            file.save(os.path.join(basedir,app.config['UPLOAD_FOLDER'],filename))
            logger.info('Successful - Project Proposal Uploaded')
    if (success == True):
        logger.info('Going Back To Student Dashboard')
        return render_template('student_dashboard.html',course=course,submit="you have submitted a project for review")
    logger.info('On Project Details Page')
    return render_template('project_details.html',course=course)    

@app.route('/ViewFacultyResponse',methods=['GET'])
def ViewFacultyResponse():
    course = request.args.get('unique_id')
    div = request.args.get('div')
    results = services.ViewFacultyResponse(session['username'],course)
    result = results[0][0]
    if(div == '1'):
        return result[0]
    else:
        return result[1]    


@app.route('/ViewTaResponse',methods=['GET']) 
def ViewTaResponse():  
    course = request.args.get('unique_id')
    results = services.ViewTaResponse(session['username'],course)
    result = results[0][0]
    return result[0]

@app.route('/GoToStudentCourse',methods=['GET'])
def GoToStudentCourse():
    results = services.course_dropdown(session['username'])
    return render_template('student_course.html',username=session['username'],results=results)

@app.route('/registerf')
def registerf():
    return render_template("faculty_register.html")

@app.route('/faculty_register',methods=['POST'])
def faculty_register():
    fid = request.form['fid']
    name = request.form['name']
    email = request.form['email']
    password = request.form['psw']
    mode = request.form['mode']
    if mode == "Signup":
        logger.info('Registering New Faculty')
        success = services.faculty_register(fid,name,email,password)
        if (success == True):
            logger.info('Registration Successful')
            session['username'] = email
            if(check()):
                logger.info('Faculty Logged In')
                logger.info('On Faculty Dashboard')
                return render_template('faculty_dashboard.html',username=session['username'])
        else:
            logger.warning('Registratin Failed - Duplicate Email')
            logger.info('Going Back To Homepage')
            return render_template('firstpage.html')
    else:
        logger.info('On Faculty Login Page')
        return render_template('faculty_login.html')  

@app.route('/faculty_login', methods=['POST'])
def faculty_login():
    logger.info('On Faculty Login Page')
    F_Id = request.form['F_Id']
    user_password = request.form['psw']
    logger.info('Faculty Logging In')
    status = services.faculty_login(F_Id, user_password)
    if (status == True):
        logger.info('Faculty Login Successful')
        session['username'] = F_Id
        if(check()):
            flash("Successfully logged in.")
            results = services.facCourseDropdown(F_Id)
            logger.info('On Faculty Dashboard')
            return render_template('faculty_dashboard.html',username=session['username'],results=results)
    else:
        logger.warning('Faculty Login Failed')
        logger.info('Going Back to Homepage')
        return render_template('firstpage.html')    


@app.route('/faculty_course',methods=['POST'])
def faculty_course():
    c_id = request.form['course']
    if (check() == False):
        flash("You are logged out. Log in again")
        return render_template('firstpage.html')
    results = services.getProjectList(session['username'],course=c_id)
    logger.info('On View Projects Page')
    return render_template('View_Projects.html',results=results,course=c_id)


@app.route('/update_status',methods=['GET'])
def update_status():
    course = request.args.get('course')
    Group_Id = request.args.get("Group_Id")
    results = services.update_status(Group_Id)
    TA = services.findTA(course)
    logger.info('Updating Project Status')
    return render_template('Upload_Status.html',results=results,TA=TA,course=course)


@app.route('/updateProject',methods=['POST'])
def updateProject():
    c_id = request.args.get("course")
    Group_Id = request.args.get("Group_Id")
    status = request.form['status']
    Suggestion = request.form['Suggestion']
    TA = request.form['TA']
    success = services.UpdateProject(Group_Id,status,Suggestion,TA)
    results = services.getProjectList(session['username'],course=c_id)
    logger.info('On View Projects Page')
    return render_template('View_Projects.html',results=results,course=c_id)


@app.route('/GoToFacultyDashboard',methods=['GET'])
def GoToFacultyDashboard():
    results = services.facCourseDropdown(session['username'])
    return render_template('faculty_dashboard.html',username=session['username'],results=results)


@app.route('/uploads', methods=['GET'])
def uploads():
    Group_Id = request.args.get('Group_Id')
    #print(Group_Id)
    filename = str(Group_Id) + '.pdf' 
    #print(filename)
    file_path = UPLOAD_FOLDER + '/' +filename
    #return send_from_directory(os.path.join(app.instance_path, ''), filename)
    #return send_from_directory(directory=uploads, filename=filename)
    logger.info('Uploading Project Proposal')
    return send_file(file_path, as_attachment=True, attachment_filename='')


@app.route('/ta_login', methods=['POST'])
def ta_login():
    logger.info('On TA Login Page')
    roll_number = request.form['roll_number']
    user_password = request.form['psw']
    status = services.ta_login(roll_number, user_password)
    logger.info('TA Logging In')
    if (status == True):
        logger.info('TA Login Successful')
        session['username'] = roll_number
        if(check()):
            results = services.getTAprojects(roll_number)
            logger.info('On TA Dashboard')
            return render_template('ta_dashboard.html',username=session['username'],results=results)
    else:
        logger.warning('TA Login Failed')
        logger.info('Going Back To Homepage')
        return render_template('firstpage.html')


@app.route('/update_TA_status',methods=['GET','POST'])
def update_TA_status():
    Group_Id = request.args.get('Group_Id')
    results = services.update_status(Group_Id)
    return render_template('update_TA_status.html',username=session['username'],results=results)

@app.route('/update_TA_Project',methods=['POST'])
def update_TA_Project():
    Group_Id = request.args.get('Group_Id')
    Suggestion = request.form['Suggestion']
    success = services.update_TA_Project(session['username'],Group_Id,Suggestion)
    results = services.getTAprojects(session['username']) 
    return render_template('ta_dashboard.html',username=session['username'],results=results)




def check():
   if 'username' in session:
     username = session['username']
     return True
   return False     
      
@app.route('/Logout')
def Logout():
    if(check() == False):
        flash("You've already logged out")
        logger.error('Session Closed')
        logger.info('Going Back To Homepage')
        return render_template('firstpage.html')
    logger.info('Logging Out')
    session.pop('username', None)
    return render_template('firstpage.html')



@app.route('/')
def main():
    return render_template('firstpage.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
