from django.urls import path

from django.urls import path
from .views import LoginView, SignupView, productsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('signup/', SignupView.as_view(), name='signup'),

    path('products/', productsView.as_view(), name='products'),
]
