from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Caesar Justitio',
        'class': 'PBP E',
        'appname': 'Liverpoolist',
        'position1': 'Goalkeeper',
        'position2': 'Defender',
        'position3': 'Midfielder',
        'position4': 'Attacker',
    }

    return render(request, "main.html", context)
