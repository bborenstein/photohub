from django.contrib import admin

# Import Model to Register Photographers Schema and Create Forms in Admin Portal
from .models import Photographer

# Function Explained:
## List_Display Allows for Attribute Selection in Admin Portal
## List_Display_Links Allows Clickable Attributes
## Search_Fields Allows Selected Attributes as Searchable in Search Field
## Search_Per_Page Limits Results Per Page
class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'telegram', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

# Registers Form by Passing in Fields;
## 'Photographer' Connects to postgresql
## 'PhotographerAdmin' Displays Customized Attributes to Portal 
admin.site.register(Photographer, PhotographerAdmin) 