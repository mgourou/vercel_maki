# import requests
from django.shortcuts import render, redirect , reverse
from .models import Plat , LoadingPage , Ingredient
from django.http import JsonResponse
from django.core.mail import send_mail , EmailMessage

# Create your views here.
def homeFR(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            'Contact Form Submission',
            f'Nom: {name}\nEmail: {email}\nSujet: {subject}\nMessage: {message}',
            email,  # sender's email address
            ['molemgay@gmail.com'],  # recipient's email address
        )

        return redirect(reverse('homeFR') + "?success=true")

    return render(request, 'app/homeFR.html')
def homeNL(request):
    return render(request, 'app/homeNL.html')
def homeEN(request):
    return render(request, 'app/homeEN.html')
    

def productsFR(request):
    plats = Plat.objects.all()
    ingredients = Ingredient.objects.all()
    # Liste des types de plats
    types_plats = ["Entree-froide", "Entree-chaude", "Donburi", "California-Rolls", "Makis", "Hosomaki", "Temaki", "Sandwich", "Box", "Dessert"]
    
    # Créez un dictionnaire pour stocker les plats de chaque type
    plats_par_type = {}
    
    # Parcourez chaque type de plat et récupérez les plats correspondants
    for type_plat in types_plats:
        plats_par_type[type_plat] = Plat.objects.filter(type_plat=type_plat)
    context = locals()
    return render(request, 'app/productsFR.html', context)
def productsNL(request):
    return render(request, 'app/productsNL.html')
def productsEN(request):
    return render(request, 'app/productsEN.html')

def show_plat(request,id):
    plat = Plat.objects.get(id=id)
    return render(request,'app/plat_detail.html',{'plat' : plat})


def error404(request,exception):
    return render(request, 'app/error-404.html',status=404)

def loading_page(request):
    loading_data = LoadingPage.objects.first()  # Récupérez les données de la page de chargement
    return render(request, 'app/loading_page.html', {'loading_data': loading_data})
    # place_id = "ChIJoVmdX7I3wkcRHx5uyF1Ga_E"
    # api_key = "AIzaSyDPyqh98eWbEtS7lTTZalGgOUwYQS9Ik94"
    
    
    # url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,reviews&key={api_key}"
    # response = requests.get(url)
    # data = response.json()

    # reviews = data.get("result", {}).get("reviews", [])
    
    # return JsonResponse(reviews, safe=False)