import re
import random
import string
import json
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.db.models import Value,CharField
# from mysite.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail, EmailMessage


from django.template.loader import render_to_string
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth
from .models import *



# Landing Page
def landing(request):
    return render(request,'landing.html')

# -----------------------------------
# Faculty Section
# -----------------------------------


# Login View
def facultyLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            detail = User.objects.get(email=email)
            username=detail.username
        except:
            username='Temp'
        user = authenticate(username=username, password=password)
        # Roles
        if user is not None:
            login(request, user)
            return redirect('facultyDashboard')
        else:
            messages.error(request, "You are Not registered")
            return redirect('facultyRegister')
    return render(request,'faculty/facultyLogin.html')

# Register View
def facultyRegister(request):
    if request.method=='POST':
        full_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        dob = request.POST['dob']
        contact = request.POST['contact']
        institute = request.POST['institute']
        state = request.POST['state']
        yearOfStudy = request.POST['yos']
        about = request.POST['about']
        profilePic = request.FILES.get('profilePic')

        print(profilePic)
        # Generating unique username
        num = random.randint(10000000, 99999999)
        str1 = 'EF'
        unique_id = str1 + str(num)

        username=unique_id
        first_name=full_name.split(' ')[0]
        last_name=full_name.split(' ')[1]
        if User.objects.filter(email=email).exists():
            messages.error(request,'You Already have an account. Please Log In')
            return redirect('facultyLogin')
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.is_staff=True;
            user.is_superuser=False;
            user.save()

            u_id = User.objects.get(username=username)

            faculty = FacultyDetails(facultyId=u_id,facultyName=full_name,facultyPhone=contact,facultyGender=gender,facultyDOB = dob,
                            facultyDesc=about,facultyCollege=institute,collegeState=state,experience=yearOfStudy,facultyPic=profilePic)

            faculty.save()
            # u_id = User.objects.get(username=username)
            # addusr = UserDetails(user_id=u_id,number=number)
            # addusr.save()

            # send_mail(
            #             'EZacademy',
            #             'Thank you '+ first_name + ' ' + last_name + ' for showing interest in our website. You have been successfully registered. Feel free to call for any house help and avail our facilities at a rational price !',
            #             '',
            #             [email],
            #             fail_silently = False
            #             )

            messages.success(request,'You are now registered and can log in')
            return redirect('facultyLogin')

    return render(request,'faculty/facultyRegister.html')


# Logout View
@login_required
def facultyLogout(request):
    if request.user.is_active and request.user.is_staff and not request.user.is_superuser:
        auth.logout(request)
        return render(request, 'faculty/facultyLogout.html')
    else:
        return redirect('facultyLogin')

# Dashboard View
@login_required
def facultyDashboard(request):
    if request.user.is_active and request.user.is_staff and not request.user.is_superuser:
        user=request.user
        faculty = FacultyDetails.objects.get(facultyId = user.id)
        classRooms = ClassRoom.objects.filter(classFacultyID=faculty.id)
        unique_id=faculty.facultyId

        # Email Testing
        if request.method=='POST':
            # send_mail(
            #             'Daily Rozgaar',
            #             'Thank you for showing interest in our website. You have been successfully registered. Feel free to call for any house help and avail our facilities at a rational price !',
            #             'rahul.agarwal31101999@gmail.com',
            #             ['adityaverma0198@gmail.com'],
            #             fail_silently = False
            #             )

            role_user_email = 'adityaverma0198@gmail.com'
            mail_subject = "Welcome To VC - Virtual Classroom"
            message = render_to_string('register_successful.html', {
                'user': role_user_email,
                'firstname': user.first_name,
                'lastname': user.last_name,
                'unique_id' : unique_id,
            })

            email = EmailMessage(mail_subject, message, from_email=EMAIL_HOST_USER, to=[role_user_email])
            email.send()

            # End Email Testing


            return redirect(request.path_info)


        # Email Testing Ends


        context={
            'classRooms' : classRooms,
        }
        return render(request,'faculty/facultyDashboard.html',context)
    else:
        return redirect('facultyLogin')


# Profile View
@login_required
def facultyProfile(request):
    if request.user.is_active and request.user.is_staff and not request.user.is_superuser:
        user=request.user
        userDetails = FacultyDetails.objects.get(facultyId = user.pk)

        if request.method=='POST':
            contact = request.POST['contact']
            institute = request.POST['institute']
            state = request.POST['state']
            experience = request.POST['year']
            about = request.POST['about']
            profilePic = request.FILES.get('profilePic')

            userDetails.facultyPhone = contact
            userDetails.facultyCollege = institute
            userDetails.collegeState = state
            userDetails.experience = experience
            userDetails.facultyDesc = about
            userDetails.facultyPic = profilePic

            userDetails.save()
            return redirect(request.path_info)

        context={
            'userDetails' : userDetails,
        }
        return render(request,'faculty/facultyProfile.html',context)
    else:
        return redirect('facultyLogin')


# Classroom Creation View
@login_required
def facultyClassCreate(request):
    if request.user.is_active and request.user.is_staff and not request.user.is_superuser:
        if request.method=='POST':
            className = request.POST['className']
            facultyName = request.POST['faculty']
            department = request.POST['department']
            academicYear = request.POST['year']
            gmeetLink = request.POST['gmeet']

            # Getting list of days when class will happen
            timetable = ""
            temp = request.POST.getlist('time')

            # monday = request.POST['monday']
            if 'Monday' in temp:
                # Storing Day,start_time and end_time as a list
                list=[]
                list.append('Monday')
                monday_start = request.POST.get('monday_start',0)
                monday_end = request.POST.get('monday_end',0)
                list.append(monday_start)
                list.append(monday_end)
                timetable += str(list)
                timetable += '+'

            # print(monday)

            # tuesday = request.POST.get('tuesday')
            if 'Tuesday' in temp:
                # Storing Day,start_time and end_time as a list
                list=[]
                list.append('Tuesday')
                tuesday_start = request.POST.get('tuesday_start',0)
                tuesday_end = request.POST.get('tuesday_end',0)
                list.append(tuesday_start)
                list.append(tuesday_end)
                timetable += str(list)
                timetable += '+'

            # print(tuesday)

            # wednesday = request.POST['wednesday']
            if 'Wednesday' in temp:
                # Storing Day,start_time and end_time as a list
                list=[]
                list.append('Wednesday')
                wednesday_start = request.POST.get('wednesday_start',0)
                wednesday_end = request.POST.get('wednesday_end',0)
                list.append(wednesday_start)
                list.append(wednesday_end)
                timetable += str(list)
                timetable += '+'


            # thursday = request.POST['thursday']
            if 'Thursday' in temp:
                # Storing Day,start_time and end_time as a list
                list=[]
                list.append('Thursday')
                thursday_start = request.POST.get('thursday_start',0)
                thursday_end = request.POST.get('thursday_end',0)
                list.append(thursday_start)
                list.append(thursday_end)
                timetable += str(list)
                timetable += '+'


            # friday = request.POST['friday']
            if 'Friday' in temp:
                # Storing Day,start_time and end_time as a list
                list=[]
                list.append('Friday')
                friday_start = request.POST.get('friday_start',0)
                friday_end = request.POST.get('friday_end',0)
                list.append(friday_start)
                list.append(friday_end)
                timetable += str(list)
                timetable += '+'

            # saturday = request.POST['saturday']
            if 'Saturday' in temp:
                # Storing Day,start_time and end_time as a list
                list=[]
                list.append('Saturday')
                saturday_start = request.POST.get('saturday_start',0)
                saturday_end = request.POST.get('saturday_end',0)
                list.append(saturday_start)
                list.append(saturday_end)
                timetable += str(list)
                timetable += '+'

            # sunday = request.POST['sunday']
            if 'Sunday' in temp:
                # Storing Day,start_time and end_time as a list
                list=[]
                list.append('Sunday')
                sunday_start = request.POST.get('sunday_start',0)
                sunday_end = request.POST.get('sunday_end',0)
                list.append(sunday_start)
                list.append(sunday_end)
                timetable += str(list)
                timetable += '+'

            timetable = timetable[:-1]
            # Getting faculty details
            user=request.user
            faculty = FacultyDetails.objects.get(facultyId = user.pk)

            # unique class id
            classId = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

            # Testing
            # print('---------Testing-------')
            # print('Timetable : ' + timetable)
            # print(faculty.facultyId)
            # print(user.id)

            # Creating classroom Object
            classCreate = ClassRoom(classId=classId, classname=className, classDepartment= department, academicYear=academicYear,
                                    classFacultyID_id = faculty.pk, classFacultyName=faculty.facultyName, classTimeTable = timetable)

            if gmeetLink is not None:
                classCreate.classLink = gmeetLink

            classCreate.save()
            # End Classroom Created


            # Creating object for ClassroomStudentsList
            # Creating empty dict for the student list
            my_dict = {}
            input = json.dumps(my_dict)

            classroomStudentsList  = ClassroomStudentsList(classId_id = classCreate.pk, studentList = input )
            classroomStudentsList.save()
            # End Creating object for ClassroomStudentsList

            return redirect('facultyDashboard')

        return render(request,'faculty/facultyClassCreate.html')

    else:
        return redirect('facultyLogin')

# Faculty Subject
@login_required
def facultySubject(request,pk):
    if request.user.is_active and request.user.is_staff and not request.user.is_superuser:
        id=pk
        classDetails = ClassRoom.objects.get(classId=id)
        if request.method=='POST':
            if 'postAnnouncement' in request.POST:
                announcementHeading = request.POST['announcementHeading']
                announcementDescription = request.POST['announcementDescription']

                # print('-------Testing---------')
                # print(announcementDescription)

                temp = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                announcementId = 'AN' + temp
                newAnnouncement = Announcement(announcementId = announcementId, classId_id = classDetails.pk ,announcementHeading = announcementHeading,
                                                announcementDescription = announcementDescription)

                newAnnouncement.save()

                return redirect(request.path_info)

            if 'postAssignment' in request.POST:
                assignmentHeading = request.POST['assignmentHeading']
                assignmentDescription = request.POST['assignmentDescription']
                assignmentLink = request.POST['assignmentLink']
                dueDate = request.POST['dueDate']

                temp = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                assignmentId = 'AS' + temp

                newAssignment = Assignment(assignmentId = assignmentId, classId_id = classDetails.pk ,assignmentHeading = assignmentHeading,
                                                assignmentDescription = assignmentDescription, assignmentLink = assignmentLink, assignmentDueTime = dueDate)

                newAssignment.save()
                return redirect(request.path_info)

            if 'linkSubmit' in request.POST:
                meetLink = request.POST['meetLink']

                # Saving the changes
                classDetails = ClassRoom.objects.get(classId=id)
                classDetails.classLink = meetLink
                classDetails.save()

                return redirect(request.path_info)

            return redirect(request.path_info)

        announcements = Announcement.objects.filter(classId = classDetails.pk).annotate(type=Value('announcement', CharField()))
        assignments = Assignment.objects.filter(classId = classDetails.pk).annotate(type=Value('assignment', CharField()))

        all_items = list(assignments) + list(announcements)

        all_items_feed = sorted(all_items, key=lambda obj: obj.publishedTime,reverse=True)
        # print(all_items_feed)

        context={
            'class':classDetails,
            'announcements' : announcements,
            'all_items_feed' : all_items_feed
        }
        return render(request,'faculty/facultySubject.html',context)
    else:
        return redirect('facultyLogin')


# -----------------------------------
# Student Section
# -----------------------------------


# Login View
def studentLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            detail = User.objects.get(email=email)
            username=detail.username
        except:
            username='Temp'

        print('Username', username)

        user = authenticate(username=username, password=password)
        # Roles
        if user is not None:
            login(request, user)
            return redirect('studentDashboard')
        else:
            messages.error(request, "You are Not registered")
            return redirect('studentRegister')
    return render(request,'student/studentLogin.html')

# Register View
def studentRegister(request):
    if request.method=='POST':
        full_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        dob = request.POST['dob']
        contact = request.POST['contact']
        institute = request.POST['institute']
        state = request.POST['state']
        yearOfStudy = request.POST['yos']
        about = request.POST['about']
        profilePic = request.FILES.get('profilePic')

        print(profilePic)
        # Generating unique username
        num = random.randint(10000000, 99999999)
        str1 = 'ES'
        unique_id = str1 + str(num)

        username=unique_id
        first_name=full_name.split(' ')[0]
        last_name=full_name.split(' ')[1]
        if User.objects.filter(email=email).exists():
            messages.error(request,'You Already have an account. Please Log In')
            return redirect('studentLogin')
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.is_staff=False;
            user.is_superuser=False;
            user.save()

            u_id = User.objects.get(username=username)

            student = StudentDetails(studentId=u_id,studentName=full_name,studentPhone=contact,studentGender=gender,studentDOB = dob,
                            studentDesc=about,studentCollege=institute,collegeState=state,yearOfStudy=yearOfStudy,studentPic=profilePic)

            student.save()

            # Creating StudentClassroomList object
            my_dict={}
            input = json.dumps(my_dict)
            studentClassroomList = StudentClassroomList(studentId_id = user.pk, classList = input)
            studentClassroomList.save()
            # End Creating StudentClassroomList object


            # u_id = User.objects.get(username=username)
            # addusr = UserDetails(user_id=u_id,number=number)
            # addusr.save()

            # send_mail(
            #             'EZacademy',
            #             'Thank you '+ first_name + ' ' + last_name + ' for showing interest in our website. You have been successfully registered. Feel free to call for any house help and avail our facilities at a rational price !',
            #             '',
            #             [email],
            #             fail_silently = False
            #             )

            messages.success(request,'You are now registered and can log in')
            return redirect('studentLogin')
    return render(request,'student/studentRegister.html')

# Logout View
@login_required
def studentLogout(request):
    if request.user.is_active and not request.user.is_staff and not request.user.is_superuser:
        auth.logout(request)
        return render(request, 'student/studentLogout.html')
    else:
        return redirect('studentLogin')


# Dashboard View
@login_required
def studentDashboard(request):
    if request.user.is_active and not request.user.is_staff and not request.user.is_superuser:

        # Getting user details
        user = request.user
        student = StudentDetails.objects.get(studentId = user.pk)

        # Getting classroom list joined by student
        classRoomList = StudentClassroomList.objects.get(studentId_id = user.pk)
        dict = json.loads(classRoomList.classList)
        temp = [*dict]
        classList =[]
        for x in temp:
            temp = ClassRoom.objects.get(classId = x)
            classList.append(temp)
        # ends

        if request.method == 'POST':
            if 'classJoin' in request.POST:
                classId = request.POST['classJoinCode']

                # datetime object containing current date and time
                now = datetime.now()
                # dd/mm/YY H:M:S format
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                try:
                    getClass = ClassRoom.objects.get(classId = classId)
                    print('----Class Link Valid-------')
                except:
                    # message.alert(request,"No such class exist")
                    print('----Class Link Invalid--------')
                    return redirect(request.path_info)


                try:
                    list = StudentClassroomList.objects.get(studentId = user.pk)
                    my_dict = json.loads(list.classList)
                    if classId in my_dict.keys():
                        print('----student already in classroom -------')
                        return redirect('studentSubject',pk=classId)
                    else:
                        print('----student not in classroom-------')
                        # classroom  added in student list of StudentClassroomList
                        my_dict[classId] = dt_string
                        input = json.dumps(my_dict)
                        list.classList = input
                        list.save()
                        # ends

                        # student addid in classroom list of ClassroomStudentsList
                        studentId_str = str(student.studentId)
                        classroomStudentsList = ClassroomStudentsList.objects.get(classId = classId)
                        studentList = classroomStudentsList.studentList
                        print(studentList)
                        my_dict = json.loads(studentList)
                        my_dict[studentId_str] = dt_string
                        input = json.dumps(my_dict)
                        classroomStudentsList.studentList = input
                        classroomStudentsList.save()
                        # ends

                        return redirect('studentSubject',pk=classId)
                    return redirect(request.path_info)

                except(StudentClassroomList.DoesNotExist):
                    my_dict={}
                    my_dict[classId] = dt_string
                    input = json.dumps(my_dict)
                    list = StudentClassroomList(studentId_id = user.pk,classList = input)
                    list.save()
                    return redirect('studentSubject',pk=classId)

                return redirect(request.path_info)    # classJoin post ends
            return redirect(request.path_info)   #  post ends

        context={
            'classList' : classList,
        }
        return render(request,'student/studentDashboard.html',context)

    else:
        return redirect('studentLogin')

# Profile View
@login_required
def studentProfile(request):
    if request.user.is_active and not request.user.is_staff and not request.user.is_superuser:
        user=request.user
        userDetails = StudentDetails.objects.get(studentId = user.pk)

        if request.method=='POST':
            contact = request.POST['contact']
            institute = request.POST['institute']
            state = request.POST['state']
            yos = request.POST['year']
            about = request.POST['about']
            profilePic = request.FILES.get('profilePic')

            userDetails.studentPhone = contact
            userDetails.studentCollege = institute
            userDetails.collegeState = state
            userDetails.yearOfStudy = yos
            userDetails.studentDesc = about
            userDetails.studentPic = profilePic

            userDetails.save()
            return redirect(request.path_info)


        context={
            'userDetails' : userDetails,
        }
        return render(request,'student/studentProfile.html',context)
    else:
        return redirect('studentLogin')

# Student Subject View
@login_required
def studentSubject(request,pk):
    if request.user.is_active and not request.user.is_staff and not request.user.is_superuser:
        id=pk
        classDetails = ClassRoom.objects.get(classId=id)
        announcements = Announcement.objects.filter(classId = id)
        context={
            'class' : classDetails,
            'announcements' : announcements,
        }
        return render(request,'student/studentSubject.html',context)
    else:
        return redirect('studentLogin')

# Assignment View
@login_required
def studentAssignment(request):
    if request.user.is_active and not request.user.is_staff and not request.user.is_superuser:
        return render(request,'student/studentAssignment.html')
    else:
        return redirect('studentLogin')
