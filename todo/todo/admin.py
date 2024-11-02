# from django.contrib import admin
# from todo.models import TODOO

# admin.site.register(TODOO)


from django.contrib import admin
from todo.models import TODOO

@admin.register(TODOO)
class TODOOAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the TODOO model. This class customizes the
    display of the TODOO model in the Django admin interface, allowing the 
    administrator to view, search, and filter tasks easily.
    
    Attributes:
        - list_display: Specifies fields to display in the list view.
        - list_filter: Enables filtering by specified fields.
        - search_fields: Allows searching by title and user username.
        - ordering: Default ordering by the 'date' field.
    """
    
    # Display these fields in the admin list view for easy access
    list_display = ('srno', 'title', 'status', 'user', 'date')
    
    # Filters to narrow down tasks by completion status and user
    list_filter = ('status', 'user')
    
    # Enables search functionality by title and user
    search_fields = ('title', 'user__username')
    
    # Default ordering by date, showing the most recent tasks first
    ordering = ('-date',)
