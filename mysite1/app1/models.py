from django.db import models

# Create your models here.


class signup_db(models.Model):
    
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True, unique=True)
    current_date_time = models.DateTimeField(auto_now=True)


class audio_db1(models.Model):

    email = models.CharField(max_length=255, null=True)
    # signup_db_user = models.ForeignKey(signup_db, null=True, on_delete = models.CASCADE) # this will be user_id inside db
    audio_file = models.FileField(upload_to='Audio_media/')
    current_date_time = models.DateTimeField(auto_now=True)
