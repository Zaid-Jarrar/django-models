from django.contrib import admin
from .models import Snack
# Register your models here.
#anything that appears on the admin can be modified here 
@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display = ['name', 'purchaser', 'description']
    search_fields = ('name', )

#OR 

# register the model with the admin
# admin.site.register(Snack)