from django.shortcuts import render

def show_main(request):
    context = {
                "application_name": "SeoulnSound",
                "self_name": "Azzahra Salsabila",
                "pbp_class": "PBP A",
                "product_name": "Hot Souce",
                "price": 300000,
                "description": "The 1st Full Album by NCT Dream",
                "rating": "5/5"
    }

    return render(request, "main.html", context)