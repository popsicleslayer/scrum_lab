from django.contrib import admin

# Register your models here.
from jedzonko.models import *
admin.site.register(Plan)
admin.site.register(Recipe)
admin.site.register(RecipePlan)
admin.site.register(Dayname)