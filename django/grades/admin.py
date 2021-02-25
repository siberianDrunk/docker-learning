from django.contrib import admin
from grades.models import Grade, Direction

class GradeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grade, GradeAdmin)

class DirectionAdmin(admin.ModelAdmin):
    pass
admin.site.register (Direction, DirectionAdmin)
