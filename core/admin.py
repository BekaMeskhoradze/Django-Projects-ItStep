from django.contrib import admin

from core.models import Student, Course, Lecturer

@admin.action(description='Mark selected as inactive')
def make_not_active(modeladmin,request,queryset):
    queryset.update(is_active=False)

@admin.action(description='Mark selected as active')
def make_is_active(modeladmin,request,queryset):
    queryset.update(is_active=True)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'get_courses', 'grade', 'is_active', 'total_price')
    list_display_links = ('first_name', 'last_name')
    list_editable = ('grade',)
    search_fields = ('first_name', 'last_name')
    list_per_page = 7
    actions = (make_is_active, make_not_active)

    @admin.display(description='Total price')
    def total_price(self,obj):
        return sum(course.price for course in obj.courses.all())

    def get_courses(self, obj):
        return ', '.join([course.name for course in obj.courses.all()])
    get_courses.short_description = 'Courses'

    fieldsets = (
        ('📘 Basic Information', {
            'fields': ('first_name', 'last_name', 'age', 'email', 'is_active')
        }),
        ('📚 Courses', {
            'fields': ('courses',),
            'description': 'Select the courses this student is enrolled in.'
        }),
        ('📊 Academic Details', {
            'fields': ('grade',),
            'description': 'Enter the student\'s grade.'
        }),
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'lecturer', 'start_date', 'end_date', 'duration', 'is_active', 'price')
    list_editable = ('lecturer',)
    search_fields = ('name',)
    list_per_page = 5
    actions = (make_is_active, make_not_active)

    fieldsets = (
        ('📘 Basic Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('⏳ Time and Status', {
            'fields': ('start_date', 'end_date', 'duration', 'is_active')
        }),
        ('👨‍🏫 Lecturer', {
            'fields': ('lecturer',)
        }),
    )

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_active')
    list_display_links = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    list_per_page = 7
    actions = (make_is_active, make_not_active)

    fieldsets = (
        ('📘 Basic Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('🟢 Status', {
            'fields' : ('is_active',)
        })
    )


