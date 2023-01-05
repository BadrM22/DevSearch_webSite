from django.db import models
import uuid


class Project(models.Model):
    
    id = models.UUIDField(
        default=uuid.uuid4,primary_key=True,unique=True,editable=False
        )
    
    title = models.CharField(verbose_name='Title',max_length=150)
    
    featured_image = models.ImageField(default="default.jpg",null=True,blank=True)
    
    description = models.TextField(verbose_name="Description",null=True,blank=True)
    
    tags = models.ManyToManyField('Tag',blank=True)

    vote_total = models.IntegerField(verbose_name="Votes",default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(verbose_name="Ratio",default=0,null=True,blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    demo_link = models.URLField(max_length=2000,null=True,blank=True)
    
    source_link = models.URLField(max_length=2000,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title
    


class Review(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,primary_key=True,unique=True,editable=False
        )
    
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    
    body = models.TextField(verbose_name="Review",max_length=300,null=True,blank=True)
    
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )
    value = models.CharField(verbose_name='Vote',max_length=45,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=150)
    id = models.UUIDField(
        default=uuid.uuid4,primary_key=True,unique=True,editable=False
        )
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name