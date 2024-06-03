from django.shortcuts import render
from .models import Details,Contact



def home(request):
  item = Details.objects.first()  # Fetch the first item from the database
  context = {
     'item': item
       }
  print("hai",item)

  return render(request,'index.html',context)
def contact(request):
  if request.method == "POST":
    Name=request.POST.get("name")
    Email=request.POST.get("email")
    PhoneNo=request.POST.get("phoneNo")
    Message=request.POST.get("message")

    contacts = Contact(name=Name,email=Email,phoneNo=PhoneNo,message=Message)
    contacts.save()

  return render(request,"contact.html")
