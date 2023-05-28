from django.contrib import admin
from . models import doctorss,Apodoc

#TO DELETE GROUP,USER
from  django.contrib.auth.models  import  Group 
from  django.contrib.auth.models  import  User



# Register your models here.
class DoctorsAdmin(admin.ModelAdmin):
   listdisplay=('doc_name','doc_degree','doc_specialised', 'doc_language','doc_image')

class docAdmin(admin.ModelAdmin):
   listdisplay=('doc_name','doc_degree','doc_specialised', 'doc_language','doc_image')



admin.site.register(doctorss,DoctorsAdmin)
admin.site.register(Apodoc,docAdmin)



#TO ADD TITLE IN DJANGO ADMIN PAGE
admin.site.site_header  =  "APOLLO HOSPITAL DB"  
admin.site.site_title  =  "APOLLO HOSPITAL"
admin.site.index_title  =  "APOLLO HOSPITAL"

#TO DELETE GROUP,USER
admin.site.unregister(Group)
admin.site.unregister(User)