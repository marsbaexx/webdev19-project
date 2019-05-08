from django.contrib import admin

# Register your models here.
from .models import Found, HelpInfo, HelpType, Author

admin.site.register(HelpType)
admin.site.register(Found)
admin.site.register(HelpInfo)
admin.site.register(Author)
