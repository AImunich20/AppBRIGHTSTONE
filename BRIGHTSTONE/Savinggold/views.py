from django.shortcuts import render, redirect
from .models import Saver

def savinggold_page(request):

    print("VIEW WORKING")   # เพิ่มบรรทัดนี้

    if request.method == "POST":

        print("POST DETECTED")

        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        phone = request.POST.get("phone")

        print("DATA:", first, last, phone)

        Saver.objects.create(
            first_name=first,
            last_name=last,
            phone=phone
        )

        return redirect('/savinggold/')

    savers = Saver.objects.all()

    return render(request, "savinggold.html", {"savers": savers, "active_menu": "savinggold"})