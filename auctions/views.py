from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from .models import User, Listing, Category, Comment, Bid
from django.contrib import messages
    
def index(request):
    active_listings = Listing.objects.filter(is_active=True) 
    return render(request, "auctions/index.html", {
        "listings": active_listings,
    })

def create_listing(request):
    if request.method == 'GET':
        all_catg = Category.objects.all()
        return render(request, "auctions/create.html",{
            "category": all_catg,
        })
    else:
        # Fetch the data from the form 
        title = request.POST['title'] 
        description = request.POST['description'] 
        imageUrl = request.POST['imageUrl'] 
        starting_bid = request.POST['starting_bid'] 
        category = request.POST['category']

        # Getting the category from the Database
        catg_data = Category.objects.get(categoryName=category)
        curr_user = request.user

        new_listing = Listing(
            title=title,
            description=description,
            image_url=imageUrl,
            starting_bid=float(starting_bid),
            owner=curr_user,
            category=catg_data,
        )
        new_listing.save()

        return HttpResponseRedirect(reverse(index))        

def place_bid(request, listing_id):
    list_data = Listing.objects.get(id=listing_id)

    if request.method == "POST":
        bid_amount = request.POST["bid_amount"]

        # Validate bid amount 
        try:
            bid_amount = float(bid_amount)
            min_bid = list_data.highest_bid.bid if list_data.highest_bid else list_data.starting_bid

            if bid_amount < min_bid:
                messages.error(request, f"Your bid must be at least {min_bid}.")
                return HttpResponseRedirect(reverse("listings", args=(listing_id,)))
        except ValueError:
            messages.error(request, "Invalid bid amount.")
            return HttpResponseRedirect(reverse("listings", args=(listing_id,)))
        
        # Create and save new bid
        bid = Bid.objects.create(
            bid=bid_amount,
            bidder=request.user,
        )

        list_data.highest_bid = bid
        list_data.save()

        messages.success(request, "Your bid has been placed successfully!")
        return HttpResponseRedirect(reverse("listings", args=(listing_id,)))
    return HttpResponseRedirect(reverse("listings", args=(listing_id,)))

def category_view(request):
    all_catg = Category.objects.all()
    return render(request, "auctions/category.html", {
        "categories": all_catg,
    })

def category_page(request, category_id):
    catg_data = Category.objects.get(id=category_id)
    list_data = Listing.objects.filter(category=catg_data, is_active=True)
    return render(request, "auctions/category_view.html", {"category": catg_data, "listings": list_data})

# Listing function for individual list item 
def listings(request, id):
    list_data = Listing.objects.get(pk=id)
    watchlisted = request.user in list_data.watchlist.all()
    all_comments = Comment.objects.filter(listing=list_data)

    # Closing the bidding 
    is_owner = list_data.owner.username == request.user.username
    return render(request, "auctions/listing_detail.html", {
        "listing": list_data,
        "watchlisted": watchlisted,
        "comments": all_comments,
        "is_owner": is_owner,
    })


def close_auction(request, listing_id):
    list_data = Listing.objects.get(id=listing_id)
    list_data.is_active = False
    list_data.save()
    messages.success(request, "Congratulations! Your auction is closed.")
    return HttpResponseRedirect(reverse("listings", args=(listing_id,)))


def watchlist(request):
    curr_user = request.user
    get_listings = curr_user.list_items.all()
    return render(request, "auctions/watchlist.html", {
        "listings": get_listings,
    })

def add_comment(request, id):
    curr_user = request.user
    list_data = Listing.objects.get(pk=id)
    comment = request.POST["new_comment"]
    c = Comment(
        author=curr_user,
        listing=list_data,
        comment=comment
    )
    c.save()
    return HttpResponseRedirect(reverse("listings", args=(id,)))

def remove_watchlist(request, id):
    list_data = Listing.objects.get(pk=id)
    curr_user = request.user
    list_data.watchlist.remove(curr_user)
    return HttpResponseRedirect(reverse("listings", args=(id,)))

def add_watchlist(request, id):
    list_data = Listing.objects.get(pk=id)
    curr_user = request.user
    list_data.watchlist.add(curr_user)
    return HttpResponseRedirect(reverse("listings", args=(id,)))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
