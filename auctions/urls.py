from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("create/", views.create_listing, name="create"),
    path('category/', views.category_view, name='category_view'),
    path("listings/<int:id>/", views.listings, name="listings"),
    path("remove_watchlist/<int:id>/", views.remove_watchlist, name="remove_watchlist"),
    path("add_watchlist/<int:id>/", views.add_watchlist, name="add_watchlist"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("add_comment/<int:id>/", views.add_comment, name="add_comment"),
    path("bid/<int:listing_id>/", views.place_bid, name="place_bid"),
    path("close_auction/<int:listing_id>/", views.close_auction, name="close_auction"),
    path("category/<int:category_id>", views.category_page, name="category_page"),
]
