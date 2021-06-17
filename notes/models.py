from django.db import models
 



import datetime

from django.db import models
from django.utils import timezone
import os

# Create your models here.


class AIUser(models.Model):
    """
    AIUser User models

    """
    
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #userid = models.PositiveIntegerField(primary_key=True)
    
    def _str_(self):
      """
       str method
       Returns
      -----------
       str
         username
      """
      return self.username
   

    
    def authenticate(self,username,password):
        """
        authenticate method
        Parameters
        ----------
        username : str
         user name
        password : str
           password  
         Returns
         -----------
          bool
           true if authentication is successful and false if it fails.
         """

        check = None
        error_username = self._validate_username(username)
        error_password = self._validate_password(password)
        if error_username == None and error_password == None:
           check = True
        else :
           check = False              
        return check,error_username,error_password

    def _validate_username(self,username):
        error_username = None
        if self.username != username:
           error_username = "InValid UserName" 

        return error_username

    def _validate_password(self, password):
        error_password = None
        if self.password != password: 
           error_password = "InValid Password"
        return error_password   
    
class Profile(models.Model):
   fname = models.CharField(max_length = 100)
   lname = models.CharField(max_length = 100)
   country = models.CharField(max_length = 100,null=True)
   #picture = models.ImageField(upload_to = 'pictures')
   userid = models.ForeignKey(AIUser, on_delete=models.CASCADE)
   class Meta:
      db_table = "profile"
     
        

        
class WcDaData(models.Model):
    data_id = models.AutoField(primary_key=True)
    intent = models.ForeignKey('WcDaIntents', models.DO_NOTHING)
    disease = models.ForeignKey('WcDaDiseases', models.DO_NOTHING)
    source = models.ForeignKey('WcDataSource', models.DO_NOTHING)
    link = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wc_da_data'


class WcDaDiseases(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=250)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wc_da_diseases'


class WcDaIntents(models.Model):
    intent_id = models.AutoField(primary_key=True)
    intent_name = models.CharField(max_length=250)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wc_da_intents'


class WcDataSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=250)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wc_data_source'    
        
class DiseaseList(models.Model):
    disease_name = models.CharField(max_length=255)
    no_of_studies = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'disease_list'        
            


          
        