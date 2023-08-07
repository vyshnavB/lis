from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from distutils.command.upload import upload
from itertools import product
from django.shortcuts import reverse
from pyexpat import model
from autoslug import AutoSlugField
from unicodedata import category
from venv import create
from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericRelation




class company(models.Model):
    category_name=models.CharField(max_length=255,blank=True)  
    company_name=models.CharField(max_length=255,blank=True)  
    description=models.CharField(max_length=255,blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    company_image = models.FileField(upload_to='posts/', blank=True,null=True,)
 



    