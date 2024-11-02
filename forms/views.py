from django.shortcuts import render, redirect
from .forms import UserTaskForm
from .models import UserTask, leadtask
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.

def task_view(request):
    current_time=timezone.now()
    if request.method=='POST':
        form=UserTaskForm(request.POST)
        submitted_grt_id= request.POST.get('grt_id')
        print(submitted_grt_id)
        if form.is_valid():
            user_task=form.save(commit=False)
            user_task.grt_id=form.cleaned_data['grt_id']
            user_task.save()
            print('form subnitted successfully')
            
        else:
            print(form.errors)
    else:
        form=UserTaskForm()

    return render(request, 'render.html', {
        'form':form,
        'current_time':current_time,
        'current_date':current_time.date(),
    })

def team_member_details(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method=='GET':
            grt_id = request.GET.get('id')
            try:
                member = leadtask.objects.get(grt_id1=grt_id)  # Query based on team_id
                data = {
                    'name': member.name1,
                    'team_lead': member.team_lead1,
                }
                return JsonResponse(data)
            except leadtask.DoesNotExist:
                return JsonResponse({'error': 'Member not found'}, status=404)
            except Exception as e:
                print(f"Errro {e}")
                return JsonResponse({'error': 'An error occured'}, status=500)


        return JsonResponse({'error': 'Invalid request'}, status=400)

