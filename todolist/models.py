# from cProfile import label
# from email.policy import default
import datetime
from django.db import models
from django.utils import timezone

# Create your app's models here.
ITEM_SIZES = (
    ('I','Inprocces'),
    ('F','Finished'),
    ('C','Canceled'),
)

class Todo(models.Model):
    task_category = models.CharField(max_length=50)
    task_label = models.CharField(max_length=50)
    task_name = models.CharField(max_length=150)
    task_status = models.CharField(choices=ITEM_SIZES,max_length=1)
    task_description = models.CharField(max_length=500,help_text="""Ensure you provide some description of the ingredients""")
    task_duration = models.DurationField()
    task_repeatation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_key = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.task_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

    #  __str__() methods:
    # not only for your own convenience when dealing with 
    # the interactive prompt, but also because 
    # objects’ representations are used
    # throughout Django’s automatically-generated admin.

    # Verbose field names
    # Each field type, except for ForeignKey, ManyToManyField and OneToOneField, 
    # takes an optional first positional argument – a verbose name. If the verbose
    # name isn’t given, Django will automatically create it using the field’s 
    # attribute name, converting underscores to spaces.
    # ForeignKey, ManyToManyField and OneToOneField require the first argument to 
    # be a model class, so use the verbose_name keyword argument:

    # 1- Many-to-one relationships
    # To define a many-to-one relationship, use django.db.models.ForeignKey. 
    # You use it just like any other Field type: by including it as a class 
    # attribute of your model.
    # ex: poll = models.ForeignKey( Poll, on_delete = models.CASCADE,
    # verbose_name = "the related poll" )

    # 2- Many-to-many relationships
    # To define a many-to-many relationship, use ManyToManyField. 
    # You use it just like any other Field type: by including it as a class 
    # attribute of your model.
    # ex: sites = models.ManyToManyField( Site, verbose_name = "list of sites" )

    # 3- One-to-one relationships
    # To define a one-to-one relationship, use OneToOneField. You use it just like 
    # any other Field type: by including it as a class attribute of your model.
    # ex: place = models.OneToOneField( Place, on_delete = models.CASCADE,
    # verbose_name = "related place" )
    
    

    
