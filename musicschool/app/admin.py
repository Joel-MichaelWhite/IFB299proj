from django.contrib import admin
from .models import Students, Admins, Teachers, Instruments, InstrumentHire, TeachingSchedule, Contract, TeacherFeedback

admin.site.register(Students)
admin.site.register(Admins)
admin.site.register(Teachers)
admin.site.register(Instruments)
admin.site.register(InstrumentHire)
admin.site.register(TeachingSchedule)
admin.site.register(Contract)
admin.site.register(TeacherFeedback)