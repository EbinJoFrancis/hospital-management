from django.db import models

# Create your models here.

class doctorss(models.Model):
   doc_name=models.CharField(max_length=250)
   doc_degree=models.CharField(max_length=250)
   doc_specialised=models.CharField(max_length=2500)
   doc_language=models.CharField(max_length=2500)
   doc_image=models.CharField(max_length=2500)
   
  
class Apodoc(models.Model):
   doc_name=models.CharField(max_length=250)
   doc_degree=models.CharField(max_length=250)
   doc_specialised=models.CharField(max_length=2500)
   doc_language=models.CharField(max_length=2500)
   doc_image=models.CharField(max_length=2500)