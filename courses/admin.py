from django.contrib import admin
from django.contrib import admin
from courses.models import Course,Tag,Prerequisite,Learning,Video,quiz_model
from courses.models import UserCourse,Payment
class TagAdmin(admin.TabularInline):
    model=Tag

class LearningAdmin(admin.TabularInline):
    model=Learning

class PrerequisiteAdmin(admin.TabularInline):
    model=Prerequisite

class QuizAdmin(admin.TabularInline):
    model=quiz_model



class VideoAdmin(admin.TabularInline):
    model=Video

class CourseAdmin(admin.ModelAdmin):
    inlines=[TagAdmin,PrerequisiteAdmin,LearningAdmin,VideoAdmin,QuizAdmin]
    list_display=['name','get_price','get_discount','active']
    list_filter=('discount','active')
    def get_discount(self,course):
        return f'{course.discount}%'
    def get_price(self,course):
        return f'₹{course.price}'
   


admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)

