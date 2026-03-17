from django.shortcuts import render, redirect
from .models import Saver

def savinggold_page(request):

    if request.method == "POST":

        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        phone = request.POST.get("phone")
        national_id = request.POST.get("national_id")
        birth_date = request.POST.get("birth_date")

        # 🔥 กัน user กด submit ว่าง
        if not all([first, last, phone, national_id, birth_date]):
            return render(request, "savinggold.html", {
                "error": "กรอกข้อมูลให้ครบ",
                "savers": Saver.objects.all()
            })

        # 🔥 กัน national_id ซ้ำ
        if Saver.objects.filter(national_id=national_id).exists():
            return render(request, "savinggold.html", {
                "error": "เลขบัตรประชาชนนี้มีอยู่แล้ว",
                "savers": Saver.objects.all()
            })

        Saver.objects.create(
            first_name=first,
            last_name=last,
            phone=phone,
            national_id=national_id,
            birth_date=birth_date
        )

        return redirect('/savinggold/')

    savers = Saver.objects.all()

    return render(request, "savinggold.html", {
        "savers": savers,
        "active_menu": "savinggold"
    })

def search(request):
    return render(request, "savinggold/search.html", {
        "active_menu": "search"
    })

def saleexport(request):
    return render(request, "savinggold/saleexport.html", {
        "active_menu": "saleexport"
    })