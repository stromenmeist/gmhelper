from django.shortcuts import render
from .models import Adventure, Milestone


# list all available adventures
def adv_index(request):
    adventures = Adventure.objects.all()
    context = {
        "adventures": adventures
    }
    return render(request, "adv_index.html", context)


# display all information of a single adventure
def adv_detail(request, pk):
    adventure = Adventure.objects.get(pk=pk)
    milestones = Milestone.objects.filter(adventure=pk)
    context = {
        "adventure": adventure,
        "milestones": milestones,
    }
    return render(request, "adv_detail.html", context)
