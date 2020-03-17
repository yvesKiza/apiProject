from django.urls import path
from heart import views

urlpatterns = [
    path('hospitals/', views.hospital_list),
    path('hospitals/<int:pk>/', views.hospital_detail),
      path('predict/', views.predict.as_view())
]