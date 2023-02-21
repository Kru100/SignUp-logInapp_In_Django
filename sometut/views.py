
# from models import Personal, Login
from django.shortcuts import render

def HomePage(request):
    return render(request,'home.html')
    



# def Insert(request):
#     if request.method=="POST":
#         if request.POST.get('Institute_id') and request.POST.get('Institute_name') and request.POST.get('Country'): 
#             saverecord=Institute()
#             saverecord.Institute_id=request.POST.get('Institute_id') 
#             saverecord.Institute_namename=request.POST.get('Institute_name')
#             saverecord.Country=request.POST.get('Country')

#             allval=Institute.objects.all()
            
#             for i in allval:
#                 if int(i.Institute_id)==int(request.POST.get('Institute_id')):
#                     messages.warning(request,'Institute already exists....!');
#                     return render(request,'Insert.html')

#             saverecord.save()
#             messages.success(request,'Institute '+saverecord.Institute_name+' is saved succesfully!!')
#             return render(request,'Insert.html')
#     else:
#             return render(request,'I