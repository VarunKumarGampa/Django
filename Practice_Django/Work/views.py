from django.shortcuts import render

# Create your views here.
def Work(request):
  return render(request,'Work/mywork.html')