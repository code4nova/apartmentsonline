from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from models import *

class ComplexUserInline(admin.StackedInline):
    model = ApartmentComplexUser
    can_delete = False
    verbose_name_plural = 'Complex Users'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ComplexUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ApartmentComplex)
admin.site.register(ApartmentBuilding)
admin.site.register(ApartmentContact)
