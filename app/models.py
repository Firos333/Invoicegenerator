

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# # Create your models here.

# class client_details(models.Model):
#     name = models.CharField(max_length=100, blank=False, null=False)
#     email = models.EmailField(max_length = 254,blank=False, null=True) 
#     taluk = models.CharField(max_length=100,blank=False, null=True)
#     phone = models.BigIntegerField(blank=False, null=False)

#     address_line1 = models.CharField(max_length=200,blank=True, null=True)
#     address_line2 = models.CharField(max_length=200,blank=True, null=True)
#     city = models.CharField(max_length=200,blank=True, null=True)
#     district = models.CharField(max_length=100,blank=True, null=True)
#     state = models.CharField(max_length=100,blank=True, null=True)
#     pin = models.CharField(max_length=100,blank=True, null=True)
  

#     education = models.CharField(max_length=100,blank=True, null=True)
    
  
#     # latitude =models.CharField(max_length=100,blank=True, null=True)
#     # longitude =models.CharField(max_length=100,blank=True, null=True)

#     is_exp = models.CharField(max_length=10,blank=True, null=True)
#     is_smartphone = models.CharField(max_length=10,blank=True, null=True)
#     is_banking = models.CharField(max_length=10,blank=True, null=True)


#     is_approved = models.BooleanField(default=False)
#     is_declined = models.BooleanField(default=False)
#     created_date = models.DateField(default=now, editable=False)
    
#     def __str__(self):
#         return self.name
  
# class Taluk(models.Model):
#     name = models.CharField(max_length=100)
#     count= models.IntegerField(default=0)
#     district = models.ForeignKey("District", on_delete=models.CASCADE,)
#     def __unicode__(self):
#         return u'%s' % (self.name)

#     def __str__(self):
#         return self.name

# class District(models.Model):
#     name = models.CharField(max_length=50)
#     def __unicode__(self):
#         return u'%s' % (self.name)

#     def __str__(self):
#         return self.name