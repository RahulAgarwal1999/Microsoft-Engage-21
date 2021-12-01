<h1 align="center">VirtualClassroom</h1>
<h3 align="center">WEBSITE DEPLOYED : <a href="https://virtual-classroom1.herokuapp.com/">CLICK HERE</a></h3>

<h3> Full Documentation : <a href="https://drive.google.com/file/d/1BZVtMcB_c0o1louNacUw-Xxy3a4JqEQi/view?usp=sharing">CLICK HERE</a><h3>
<h3> Demo Video : <a href="https://www.youtube.com/watch?v=h7EkSFCbLmY">CLICK HERE</a><h3>
    
**We'll cover the following:**

* [System Requirements](#system-requirements)
* [Use Case Diagram](#use-case-diagram)
* [Class Diagram](#class-diagram)
* [Activity Diagrams](#activity-diagrams)
* [Database Schema](#database-schema)
* [Tech Stacks and Frameworks](#tech-stacks-and-frameworks)
* [Project Setup Guide](#project-setup-guide)
* [Admin Cresentials](#admin-credentials)
* [Sample Sstudent And Faculty Account Credentials](#sample-student-and-faculty-account-credentials)
* [Step By Step Guide](#step-by-step-guide)

VirtualClassroom is a web platform that gives students an array of digital academic and social tools to stay engaged with their academics and help teaching professional in creating and managing virtual classrooms. 
It gives the faculty in smooth conducting of both online and offline classes alongwith various features such as updating class timetable, posting announcement, posting assignments, taking attendence, updating meeting details, and switching between online and offline class mode.
The student has the options to join the classroom, check announcements, submit the assignments, check attendence, and choose preferred class mode.


<p align="center">
    <img src="/readme_images/VirtualClassroom.PNG" alt="VirtualClassroom">
    <br />
    VirtualClassroom
</p>

### System Requirements

We will focus on the following set of requirements while designing the application:

1. The system will support the creating ,conducting and managing of classes and will enable the interaction between students and faculties.
2. Faculty and student should be able to register and login to the portal and the system should be able to authenticate and save the users data in the database.
3. Faculty should be able to create classroom with all the necessary class details and the system should generate a unique code for each classroom.
4. Faculty should be able to Edit his/her profile.
5. Faculty should be able to update the class timetable.
6. Faculty should be able to join or update the online class meeting link.
7. Faculty should be able to send class invite code to the students through Emails by entering the Student ID.
8. Faculty should be able make any announcements and it should be visible to the student in their class dashboard.
9. Faculty should be able to post an assignment with assignment link and can set a deadline of submission to it.
10. Faculty should be able to mark, update and upload the attendance of those in the classroom.
11. Faculty should have the option to choose the mode of classes (online/offline). If opted for offline classes, faculty should fill the class strength allowed and the vaccination status required for the students.
12. The system should be able to create a offline class object and should set the limit on the number of instances allowed , according to the strength % mentioned by faculty.
13. Students should be able to Edit his/her profile.
14. Students should be able to join the classroom by entering the class code.
15. Students should be able to check class timing, announcements and assignments in the class dashboard.
16. Students after completing the assignment should be able to submit it in their portal and faculty should be able view the assignment answers as well.
17. Students should be able to opt for offline classes for the upcoming classes and the system should check student vaccination status to that of class requirements and  whether the seats are available for assignment for offline mode.
18. Students should be able to view the total class conducted, total class attended, total class missed by them, and their attendance percentage.
19. Faculty and faculty should have the option to view each other profile and can view all academic  information of theirs.

### Use Case Diagram

We have four main Actors in our system:

* **Admin:** Responsible for managing the entire application.
* **System:** Responsible for email notification, authentication and registration.
* **Faculty:** Responsible for registration and login, creating classrooms, opting class mode, sending classroom invites, marking attendance, posting announcements and assignments, and assigning grades to assignments.
* **Student:** Responsible for registration and login, updating personal info with vaccination status, joining classroom, opt for class mode, attending classes, submitting assignment, check attendance status.


Here are the top use cases of the VirtualClassroom:

* **Add/update profile:** Any member should be able to create their profile and fill all the necessary information.
* **Create classroom:** Faculty should be able to create classroom.
* **Join classroom:** Student should be able to join the classroom.
* **Post announcement:** Faculty should be able to post announcement in classroom.
* **Post assignment:** Faculty should be able to upload assignment in the classroom.
* **Submit assignment:** Students should be able to submit the assignment.

Here is the use case diagram of our application - VirtualClassroom:

<p align="center">
    <img src="/readme_images/Use case diagram.jpg" alt="VirtualClassroom Use Case Diagram">
    <br />
    Use Case Diagram for VirtualClassroom
</p>

### Class Diagram

Here are the main classes of our application:

* **Faculty:** Contains authentication related information about the Faculty like FacultyID, name, email and  passwords.
* **Student:** Contains authentication related information about the student like StudentID, name, email and  password.
* **ClassRoom:** Contains all information related to the classroom like classId, className, classDept, etc.
* **System:** Performs various backend functions like user registration, authentication and sending email notifications.
* **Announcement:** Contains all information related to announcement like announcementId, announcementDate, etc.
* **Assignment:** Contains all information related to assignment like assignmentId, assignmentDate, etc.
* **Attendence:** Contains all attendence related details of students


<p align="center">
    <img src="/readme_images/ClassDiagram.jpg" alt="VirtualClassroom Class Diagram">
    <br />
    Class Diagram for VirtualClassroom
</p>



### Activity Diagrams

**Faculty Activities:** Login, Registration, Edit Profile,  Create Classroom, Send Class Invites, Update Timetable, Post Announcements, Post Assignments, Take Attendence, Choose Class Mode

<p align="center">
    <img src="/readme_images/Activity Diagram_Faculty.jpg" alt="Virtual Classroom - Faculty Activity Diagram">
    <br />
    Activity Diagram for VirtualClassroom - Faculty 
</p>

* **Student Activities:** Registration, Login, Edit Profile,  Join Classroom, Check Attendence, Submit Assignments, Choose Class Mode

<p align="center">
    <img src="/readme_images/Activity Diagram_Student.jpg" alt="Virtual Classroom - Student Activity Diagram">
    <br />
    Activity Diagram for VirtualClassroom - Student
</p>


### Database Schema
Here is the database schema of our application:

<p align="center">
    <img src="/readme_images/Database Schema.jpg" alt="Database Schema">
    <br />
    Database Schema for VirtualClassroom
</p>


### TECH STACKS AND FRAMEWORKS
    
* **Python** - Python is an interpreted high-level general purpose programming language mainly used to build websites and software, automate tasks, and conduct data analysis.
* **Django Framework** - Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. Some features of Django are : 
* **SQLite** - SQLite is a relational database management system contained in a C library. SQLite is a server-less database and is self-contained. This is also referred to as an embedded database which means the DB engine runs as a part of the app. Thus it is a lot faster than SQL server.
* **Heroku** - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud
* **Cloudinary** - Cloudinary is an end-to-end image- and video-management solution for websites and mobile apps, covering everything from image and video uploads, storage, manipulations, optimizations to delivery.
* **Bootstrap**  - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development
* **HTML , CSS , Javascript , Json**
    


### PROJECT SETUP GUIDE

NOTE: PROJECT SETUP GUIDE (IF WANTS TO CLONE THE REPO IN LOCAL SYSTEM)

**PYTHON SETUP:**
* Install Python on your system. Download Link : <a href="https://www.python.org/downloads/">Click Here</a>
* An Exe file will be downloaded, open it.
* A dialog box will appear as shown in the figure below. Do not forget to click on the check box of “ADD PYTHON TO PATH”
* Then click on ‘INSTALL NOW’, the installation will be completed.

<p align="center">
    <img src="/readme_images/Python-setup.PNG" alt="Dialog Box in Python Installation">
    <br />
    Dialog Box in Python Installation
</p>


**Note:** If you are using Command Line terminal, then restart the terminal to use python

**GIT SETUP:**
* Download GIT on your system. Download Link : <a href="https://git-scm.com/downloads">Click Here</a>
* An Exe file will be downloaded, open it.
* A dialog box will appear, keep everyting default, and keep on selecting **‘NEXT’**. 
* The downloading will start and Git will be successfully installed

**Note:** If you are using Command Line terminal, then restart the terminal to use Git

**INSTALL DJANGO AND PACKAGES:**
* Open Command Line Terminal
* First check whether python is successfully installed or not by typing the command   **python –version**  and press Enter. If it shows the python version, then python has been successfully installed in your system
* Now run the following command one by one ( Press Enter after each command)
    - pip install django==3.0
    - pip install django-phonenumber-field
    - pip install phonenumbers
    - pip install email_validator
    - pip install django-crispy-forms
    - pip install jsonfield
    - pip install pillow
    
**CLONING THE DJANGO PROJECT FROM GITUB**

* Go to the Github Repoistory . Github Repo Link : <a href="https://github.com/RahulAgarwal1999/VirtualClassroom-Microsoft_Engage">Click Here</a>
* Click on **CODE** button and copy the **HTTPS** Link of the repo

<p align="center">
    <img src="/readme_images/Github-clone.PNG" alt="Copy the HTTPS Link">
    <br />
    Copy the HTTPS Link
</p>


* Open the Command Line Terminal and cd to the folder you want to clone the project. 
* In the command line enter the command : **git clone <Copied HTTP repo clone link>** and press **Enter**.

    
**RUNNING THE PROJECT**
  
* After the cloning is completed, cd(change directory) to the repository and again cd to the app(mysite) directory (The same level in which manage.py file is present) via the command line
* Then Run the command :  **python manage.py runserver**
    
    <p align="center">
    <img src="/readme_images/commandtorun.PNG" alt="Commands to Run">
    <br />
    Commands to Run
</p>
    
* Copy the http server link generated after running the command and open it in the browser
    
<p align="center">
    <img src="/readme_images/ServerImg.PNG" alt="Server link to run the project">
    <br />
    Server link to run the project
</p>
    
**NOTE:** For copying , select the url and click on right click and copy, otherwise select the link and do CTRL+C. But while using second method, if the server breaks, then again run the previos command, i.e. python manage.py runserver. 
    


### ADMIN CREDENTIALS
    
To Check the Admin Panel in Deployed Site, copy the following url and paste it in the browser :   https://virtual-classroom1.herokuapp.com/admin
<br>
To Check the Admin Panel in Cloned Project, copy the following url and paste it in the browser :   http://127.0.0.1:8000/admin

The django admin login page will open, image shown below :
    
<p align="center">
    <img src="/readme_images/admin-login.PNG" alt="Admin Login Page">
    <br />
    Admin Login Page
</p>

**CREDENTIALS (FOR BOTH DEPLOYED VERSION AND CLONED PROJECT):** <br>
**Username** – admin <br>
**Password** – admin12345  <br>

After Logging in as admin, you can see all the tables used and what data are filled into them, image shown below 

<p align="center">
    <img src="/readme_images/admin-dashboard.PNG" alt="Admin Dashboard Page">
    <br />
    Admin Dashboard Page
</p>


### SAMPLE STUDENT AND FACULTY ACCOUNT CREDENTIALS

There is a already created Student and Faculty Account in both Deployed website and Cloned Project. You can login with this credentials and use.

**Faculty Credentials**  <br>
Email : samplefaculty@gmail.com  <br>
Password : samplefaculty  <br>

**Student Credentials**  <br>
Email : samplestudent@gmail.com  <br>
Password : samplestudent  <br>
<br>
**Note : Even if the following credentials doesn’t work or you want to create your new credentials, you can easily create it on the faculty and student registration page. And also, to get email service, while registering as faculty or student, register with a valid email id(and not with a dummy one), to get registration confirmation mail.**

    
    
### Step By Step Guide
    
<h4>FULL STEP BY STEP GUIDE : <a href="https://drive.google.com/file/d/17EDhcdr8Pf_hSb4CnjD2g08lwcXLPgbX/view?usp=sharing">CLICK HERE</a></h4>
