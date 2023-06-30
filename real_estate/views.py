from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


def real_estate_index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'real_estate/index.html', context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "real_estate/listing.html", context)


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/real_estate")

    context = {
        "form": form
    }
    return render(request, "real_estate/listing_create.html", context)


def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/real_estate")

    context = {
        "form": form
    }
    return render(request, "real_estate/listing_update.html", context)


def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/real_estate")