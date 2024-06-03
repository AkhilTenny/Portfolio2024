from django.db import models

# Create your models here.

class Details(models.Model):
  name =models.CharField(max_length=50)
  photo1 =models.ImageField(upload_to="details")
  photo2 =models.ImageField(upload_to="details")
  photo3 =models.ImageField(upload_to="details")
  banner =models.ImageField(upload_to="details",default="true")
  bio =models.CharField(max_length=100)
  biography =models.CharField(max_length=100)
  bioSub =models.CharField(max_length=200)
  email =models.CharField(max_length=50)
  location =models.CharField(max_length=60)
  gitHub =models.CharField(max_length=60)
  linkedIn =models.CharField(max_length=60)
  instagram =models.CharField(max_length=60)
  skillSub =models.CharField(max_length=200)
  skill1 =models.CharField(max_length=60,default="true")
  skill2 =models.CharField(max_length=60,default="true")
  skill3 =models.CharField(max_length=60,default="true")
  skill4 =models.CharField(max_length=60,default="true")
  skill5 =models.CharField(max_length=60,default="true")
  skill6 =models.CharField(max_length=60,default="true")
  skill7 =models.CharField(max_length=60,default="true")
  skill8 =models.CharField(max_length=60,default="true")
  workscreenshot1 =  models.ImageField(upload_to="details")
  workscreenshot2 =  models.ImageField(upload_to="details")
  workscreenshot3 =  models.ImageField(upload_to="details")
  workscreenshot5 =  models.ImageField(upload_to="details")
  work1 =models.CharField(max_length=60)
  work2 =models.CharField(max_length=60)
  work3 =models.CharField(max_length=60)
  work4  =models.CharField(max_length=60)

class Contact(models.Model):
  name=models.CharField(max_length=20)
  email=models.CharField(max_length=20)
  phoneNo=models.ImageField()
  message=models.CharField(max_length=200)
  

  def __str__(self):
      return self.name


