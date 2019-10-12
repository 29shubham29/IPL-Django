from django.urls import path
from .views import ListMatchesView,ListDeliveriesView, ListDetailMatch, ListDetailDelivery


urlpatterns = [
    path('Matches/', ListMatchesView.as_view(), name="all-matches"),
    path('Deliveries/',ListDeliveriesView.as_view(),name="all-deliveries"),
    path('match/<int:pk>',ListDetailMatch.as_view(),name="match-detail"),
    path('delivery/<int:pk>',ListDetailDelivery.as_view(),name="delivery-detail")
]