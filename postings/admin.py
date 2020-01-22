from django.contrib import admin

# Import Model to Register Postings Schema and Create Forms in Admin Portal
from .models import Posting

# Function Explained:
## List_Display Allows for Attribute Selection in Admin Portal
## List_Display_Links Allows Clickable Attributes
## List_Filter Trims Top Right 'Filter' Module to Include Only Selected Attributes
## List_Published Allows Checkbox to Dynamically Unpublish Postings From Frontend
## Search_Fields Allows Selected Attributes as Searchable in Search Field
## Search_Per_Page Limits Results Per Page
class PostingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'location', 'posted_date', 'photographer')
    list_display_links = ('id', 'title')
    list_filter = ('photographer',)
    list_editale = ('is_published')
    search_fields = ('title', 'location', 'posted_date')
    list_per_page = 5

# Registers Postings Form by Passing in Fields;
## 'Posting' Connects to Postgresql 
## 'PostingAdmin' Displays Customized Attributes to Portal 
admin.site.register(Posting, PostingAdmin) 