from django import forms
from .models import UserTask,leadtask
from django.core.exceptions import ValidationError
class UserTaskForm(forms.ModelForm):

    grt_id=forms.CharField(max_length=100)
    class Meta:
        model=UserTask
        fields=['remotasks_id', 'grt_id', 'name', 'team_lead', 'project', 'able_to_task','trained']

        widgets = {
            'name': forms.TextInput(attrs={'readOnly': 'readOnly'}),
            'team_lead': forms.TextInput(attrs={'readonly':'readonly'}),

        }
    def clean_grt_id(self):
        grt_id= self.cleaned_data.get('grt_id')
        try:
            leadtask_instance= leadtask.objects.get(grt_id1=grt_id)
        except leadtask.DoesNotExist:
            return ValidationError(f"No leadtask found with grt id: {grt_id}")
        
        return leadtask_instance
    

