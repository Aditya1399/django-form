from django.db import models

# Create your models here.

class leadtask(models.Model):
    grt_id1=models.CharField(max_length=100,unique=True)
    team_lead1=models.CharField(max_length=255)
    name1=models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.grt_id1} - {self.team_lead1} - {self.name1}"

class UserTask(models.Model):
    remotasks_id= models.CharField(max_length=50)
    grt_id=models.ForeignKey(leadtask,on_delete=models.CASCADE)
    name=models.CharField(max_length=255, blank=True) #allow blank initially
    team_lead=models.CharField(max_length=255, blank=True) #allow blank initially
    choices = [
    ('bulba', 'BULBA'),
    ('flamingo', 'FLAMINGO'),
    ('constellation', 'CONSTELLATION')
    ]
    project=models.CharField(max_length=20, choices=choices)
    
    able_to_task=models.BooleanField(default=False)
    trained=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    

    def __str__(self) -> str:
        return f"{self.remotasks_id} - {self.grt_id}"
    
