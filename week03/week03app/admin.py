from django.contrib import admin
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]

admin.site.register(Person,PersonAdmin)