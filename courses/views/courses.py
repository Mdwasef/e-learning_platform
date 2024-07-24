# from django.http import HttpResponse
# from django.shortcuts import render,redirect,get_object_or_404
# from courses.models import Course, Video,quiz_model,UserCourse
# from courses import models
# from django.contrib.auth.decorators import login_required


# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags


# from django.shortcuts import redirect, render
# from django.contrib import messages


# from io import BytesIO
# from reportlab.pdfgen import canvas

# from django.contrib.staticfiles import finders


# @login_required(login_url='login')
# def my_courses(request):
#     user=request.user
#     user_courses=UserCourse.objects.filter(user=user)
#     context={
#         'user_courses':user_courses
#     }
#     return render(request,'courses/my_courses.html',context=context)



# def coursepage(request,slug):
#     # print(request.user.is_authenticated)
#     print(request.user)
#     course=Course.objects.get(slug=slug)
#     serial_number=request.GET.get('lecture')
#     print(serial_number,course)
#     videos=course.video_set.all().order_by("serial_number")
#     if serial_number is None:
#         serial_number=1
#     video=Video.objects.get(serial_number=serial_number,course=course)
#     if video.is_preview is False:
#     # print("preview ", video.is_preview)
#         if((request.user.is_authenticated is False)):
#             return redirect("login")
#         else:
#             user=request.user
#             try:
#                 user_course=UserCourse.objects.get(user=user,course=course)
#                 # error="already enrolled in this course"
#             except:
#                 return redirect('checkout',slug=course.slug)
#     #u enroll to watch all videos

#     context={
#         "course":course,
#         "video":video,
#         'videos':videos,
#         'slug':slug,
#     }
#     return render(request,template_name='courses/course_page.html',context=context)


# #quiz


# def home_quiz(request,slug):
#     content=quiz_model.objects.all()
#     print(content)
#     return render(request,'courses/home_quiz.html')



# def quiz_questions(request,slug):
#     course = get_object_or_404(Course, slug=slug)
#     questions = course.questions.all()
#     # content=quiz_model.objects.all()
#     context={
#          'course': course,
#         'questions': questions,
#     }
#     return render(request,'courses/quiz.html',context)




# # def quizpart(request,slug):
# #     # content=quiz_model.objects.all()
# #     course = get_object_or_404(Course, slug=slug)
# #     questions = course.questions.all()
# #     n=questions.count()
# #     # n=len(content)
# #     # print(n)
# #     if request.method=="POST":
# #         score=0
# #         for question in questions:
# #             ans=request.POST.get(f'answer_{question.id}')
# #             print(ans)
# #             correct_answer=question.answer
# #             if(ans==correct_answer):
# #                 score+=1
# #         # print(score)
# #         print(score)        
# #         percentage=(score*100)/n
# #         print(percentage)
# #         context={
# #             'score':score,
# #             'total_question':n,
# #             'percentage':percentage,
# #         }   
# #         return render(request, 'courses/score.html', context)        
# #     # return render(request,'courses/score.html',context=context)
# #     return render(request, 'courses/quiz.html', {'course': course, 'questions': questions})

# def score(request):
#     pass




# def quizpart(request, slug):
#     course = get_object_or_404(Course, slug=slug)
#     questions = course.questions.all()
#     n = questions.count()

#     if request.method == "POST":
#         score = 0
#         for question in questions:
#             ans = request.POST.get(f'answer_{question.id}')
#             correct_answer = question.answer
#             if ans == correct_answer:
#                 score += 1

#         percentage = (score * 100) / n

#         if percentage >= 70.0:
#             # Send certificate email
#             user_email = request.user.email  # Assuming user is logged in
#             send_certificate_email(user_email, score,percentage,n)
#             messages.success(request, 'Congratulations! Certificate sent to your email.')
#         else:
#             messages.error(request, 'Sorry, you did not pass the quiz.')

#         context = {
#             'score': score,
#             'total_question': n,
#             'percentage': percentage,
#         }
#         return render(request, 'courses/score.html', context)

#     return render(request, 'courses/quiz.html', {'course': course, 'questions': questions})


# def generate_certificate(score):
#     buffer = BytesIO()
#     p = canvas.Canvas(buffer)
#     p.drawString(100, 750, "Course Completion Certificate")
#     p.drawString(100, 730, f"Score: {score}")
#     # Customize further based on your certificate design
#     p.showPage()
#     p.save()
#     buffer.seek(0)
#     return buffer


# def send_certificate_email(email, score,percentage,n):
#     subject = 'Course Completion Certificate'
#     context = {
#         'score': score,
#         'percentage':percentage,
#         'n':n,
         
#     }
#     html_content = render_to_string('courses/certificate_email.html', context)
#     text_content = strip_tags(html_content)  # Strip HTML tags for plain text email
#     email = EmailMessage(subject, text_content, to=[email])
#     # email.attach_file('path/to/certificate.pdf')  # Attach the certificate PDF file
#     # email.attach_file('static/certificate.pdf')  # Attach the certificate PDF file
#     # email.send()
#     file_path = finders.find('certificate.pdf')
#     if file_path:
#         email.attach_file(file_path)  # Attach the certificate PDF file
#     else:
#         print("Certificate file not found.")
    
#     email.send()




# @login_required(login_url='login')
# def profile(request):
#     user = request.user
#     first_name = user.first_name.upper()
#     last_name = user.last_name.upper()
#     email = user.email

#     print(f"First Name: {first_name}")
#     print(f"Last Name: {last_name}")
#     print(f"Email: {email}")

#     user_courses = UserCourse.objects.filter(user=user)
#     context = {
#         'user_courses': user_courses,
#         'first_name': first_name,
#         'last_name': last_name,
#         'email': email
#     }
#     return render(request, 'courses/profile.html', context=context)
# # You can apply similar logic in other views where you need to access user details. For exam    




# from django.http import HttpResponse
# from django.shortcuts import render,redirect,get_object_or_404
# from courses.models import Course, Video,quiz_model,UserCourse
# from courses import models
# from django.contrib.auth.decorators import login_required


# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags


# from django.shortcuts import redirect, render
# from django.contrib import messages


# from io import BytesIO
# from reportlab.pdfgen import canvas

# from django.contrib.staticfiles import finders


# @login_required(login_url='login')
# def my_courses(request):
#     user=request.user
#     user_courses=UserCourse.objects.filter(user=user)
#     context={
#         'user_courses':user_courses
#     }
#     return render(request,'courses/my_courses.html',context=context)



# def coursepage(request,slug):
#     # print(request.user.is_authenticated)
#     print(request.user)
#     course=Course.objects.get(slug=slug)
#     serial_number=request.GET.get('lecture')
#     print(serial_number,course)
#     videos=course.video_set.all().order_by("serial_number")
#     if serial_number is None:
#         serial_number=1
#     video=Video.objects.get(serial_number=serial_number,course=course)
#     if video.is_preview is False:
#     # print("preview ", video.is_preview)
#         if((request.user.is_authenticated is False)):
#             return redirect("login")
#         else:
#             user=request.user
#             try:
#                 user_course=UserCourse.objects.get(user=user,course=course)
#                 # error="already enrolled in this course"
#             except:
#                 return redirect('checkout',slug=course.slug)
#     #u enroll to watch all videos

#     context={
#         "course":course,
#         "video":video,
#         'videos':videos,
#         'slug':slug,
#     }
#     return render(request,template_name='courses/course_page.html',context=context)


# #quiz


# def home_quiz(request,slug):
#     content=quiz_model.objects.all()
#     print(content)
#     return render(request,'courses/home_quiz.html')



# def quiz_questions(request,slug):
#     course = get_object_or_404(Course, slug=slug)
#     questions = course.questions.all()
#     # content=quiz_model.objects.all()
#     context={
#          'course': course,
#         'questions': questions,
#     }
#     return render(request,'courses/quiz.html',context)




# # def quizpart(request,slug):
# #     # content=quiz_model.objects.all()
# #     course = get_object_or_404(Course, slug=slug)
# #     questions = course.questions.all()
# #     n=questions.count()
# #     # n=len(content)
# #     # print(n)
# #     if request.method=="POST":
# #         score=0
# #         for question in questions:
# #             ans=request.POST.get(f'answer_{question.id}')
# #             print(ans)
# #             correct_answer=question.answer
# #             if(ans==correct_answer):
# #                 score+=1
# #         # print(score)
# #         print(score)        
# #         percentage=(score*100)/n
# #         print(percentage)
# #         context={
# #             'score':score,
# #             'total_question':n,
# #             'percentage':percentage,
# #         }   
# #         return render(request, 'courses/score.html', context)        
# #     # return render(request,'courses/score.html',context=context)
# #     return render(request, 'courses/quiz.html', {'course': course, 'questions': questions})

# def score(request):
#     pass




# def quizpart(request, slug):
#     course = get_object_or_404(Course, slug=slug)
#     questions = course.questions.all()
#     n = questions.count()

#     if request.method == "POST":
#         score = 0
#         for question in questions:
#             ans = request.POST.get(f'answer_{question.id}')
#             correct_answer = question.answer
#             if ans == correct_answer:
#                 score += 1

#         percentage = (score * 100) / n

#         if percentage >= 70.0:
#             # Send certificate email
#             user_email = request.user.email  # Assuming user is logged in
#             send_certificate_email(user_email, score,percentage,n)
#             messages.success(request, 'Congratulations! Certificate sent to your email.')
#         else:
#             messages.error(request, 'Sorry, you did not pass the quiz.')

#         context = {
#             'score': score,
#             'total_question': n,
#             'percentage': percentage,
#         }
#         return render(request, 'courses/score.html', context)

#     return render(request, 'courses/quiz.html', {'course': course, 'questions': questions})


# def generate_certificate(score):
#     buffer = BytesIO()
#     p = canvas.Canvas(buffer)
#     p.drawString(100, 750, "Course Completion Certificate")
#     p.drawString(100, 730, f"Score: {score}")
#     # Customize further based on your certificate design
#     p.showPage()
#     p.save()
#     buffer.seek(0)
#     return buffer


# def send_certificate_email(email, score,percentage,n):
#     subject = 'Course Completion Certificate'
#     context = {
#         'score': score,
#         'percentage':percentage,
#         'n':n,
         
#     }
#     html_content = render_to_string('courses/certificate_email.html', context)
#     text_content = strip_tags(html_content)  # Strip HTML tags for plain text email
#     email = EmailMessage(subject, text_content, to=[email])
#     # email.attach_file('path/to/certificate.pdf')  # Attach the certificate PDF file
#     # email.attach_file('static/certificate.pdf')  # Attach the certificate PDF file
#     # email.send()
#     file_path = finders.find('certificate.pdf')
#     if file_path:
#         email.attach_file(file_path)  # Attach the certificate PDF file
#     else:
#         print("Certificate file not found.")
    
#     email.send()




# @login_required(login_url='login')
# def profile(request):
#     user = request.user
#     first_name = user.first_name.upper()
#     last_name = user.last_name.upper()
#     email = user.email

#     print(f"First Name: {first_name}")
#     print(f"Last Name: {last_name}")
#     print(f"Email: {email}")

#     user_courses = UserCourse.objects.filter(user=user)
#     context = {
#         'user_courses': user_courses,
#         'first_name': first_name,
#         'last_name': last_name,
#         'email': email
#     }
#     return render(request, 'courses/profile.html', context=context)
# # You can apply similar logic in other views where you need to access user details. For exam    





import os
import io
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from courses.models import Course, Video, quiz_model, UserCourse

@login_required(login_url='login')
def my_courses(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)
    context = {
        'user_courses': user_courses
    }
    return render(request, 'courses/my_courses.html', context=context)

def coursepage(request, slug):
    course = get_object_or_404(Course, slug=slug)
    serial_number = request.GET.get('lecture', 1)
    videos = course.video_set.all().order_by("serial_number")
    video = get_object_or_404(Video, serial_number=serial_number, course=course)
    if not video.is_preview and not request.user.is_authenticated:
        return redirect("login")
    if not video.is_preview:
        user_course = UserCourse.objects.filter(user=request.user, course=course).first()
        if not user_course:
            return redirect('checkout', slug=course.slug)
    context = {
        "course": course,
        "video": video,
        'videos': videos,
        'slug': slug,
    }
    return render(request, 'courses/course_page.html', context=context)

def home_quiz(request, slug):
    content = quiz_model.objects.all()
    return render(request, 'courses/home_quiz.html')

def quiz_questions(request, slug):
    course = get_object_or_404(Course, slug=slug)
    questions = course.questions.all()
    context = {
        'course': course,
        'questions': questions,
    }
    return render(request, 'courses/quiz.html', context)

def quizpart(request, slug):
    course = get_object_or_404(Course, slug=slug)
    questions = course.questions.all()
    n = questions.count()

    if request.method == "POST":
        score = sum(1 for question in questions if request.POST.get(f'answer_{question.id}') == question.answer)
        percentage = (score * 100) / n

        if percentage >= 70.0:
            send_certificate_email(request.user.email, score, percentage, n)
            messages.success(request, 'Congratulations! Certificate sent to your email.')
        else:
            messages.error(request, 'Sorry, you did not pass the quiz.')

        context = {
            'score': score,
            'total_question': n,
            'percentage': percentage,
        }
        return render(request, 'courses/score.html', context)

    return render(request, 'courses/quiz.html', {'course': course, 'questions': questions})

def generate_certificate(score, user_name):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    # p.drawString(300, 900, "Course Completion Certificate")
    # p.drawString(300, 800, f"Name: {user_name}")
    # p.drawString(300, 910, f"Score: {score}")
    p.drawString(100, 750, "Course Completion Certificate")
    p.drawString(100, 730, f"Name: {user_name}")
    p.drawString(100, 710, f"Score: {score}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

def send_certificate_email(email, score, percentage, n):
    user_name = email.split('@')[0]  # Use part of the email as the user name
    subject = 'Course Completion Certificate'
    context = {
        'score': score,
        'percentage': percentage,
        'n': n,
    }
    html_content = render_to_string('courses/certificate_email.html', context)
    text_content = strip_tags(html_content)
    email_message = EmailMessage(subject, text_content, to=[email])
    certificate_buffer = generate_certificate(score, user_name)
    email_message.attach('certificate.pdf', certificate_buffer.getvalue(), 'application/pdf')
    email_message.send()
    print(f"Certificate sent to {email}")

@login_required(login_url='login')
def profile(request):
    user = request.user
    first_name = user.first_name.upper()
    last_name = user.last_name.upper()
    email = user.email
    user_courses = UserCourse.objects.filter(user=user)
    context = {
        'user_courses': user_courses,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    return render(request, 'courses/profile.html', context=context)
