from django.urls import path

from API.user.views.user import Login, UserAutocomplete, UserView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('user/<username>/', UserView.as_view(), name='user_detail'),
    path('user_autocomplete/', UserAutocomplete.as_view(), name='user_autocomplete'),
]
