from django.shortcuts import render, redirect
from .forms import AdventureForm
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


# create a new adventure
def adv_create(request):
    if request.method == "POST":
        form = AdventureForm(request.POST)
        if form.is_valid():
            adventure = Adventure(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                created_by=request.user
            )
            adventure.save()
            return redirect("adventures/")
    else:
        form = AdventureForm()
        return render(request, "adv_create.html", {"form": form})