from django.shortcuts import render

from inventory.models import Historic

# Create your views here.
def inventory_home(request):
    context = {
        "historic": Historic.objects.filter(creator=request.user.id)
    }

    return render(request, 'inventory_home.html', context)