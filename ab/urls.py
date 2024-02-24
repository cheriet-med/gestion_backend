from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

#pro_list = ProViewSet.as_view({'get': 'list'})
#pro_detail = ProViewSet.as_view({'get': 'retrieve'})

router = DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path('personel/', views.PersonelGlobal.as_view()),
    path('personeldetail/<int:pk>/', views.PersonelDetail.as_view()),

    path('avancement/', views.AvancementGlobal.as_view()),
    path('avencementdetail/<int:pk>/', views.AvancementDetail.as_view()),

    path('absance/', views.AbsanceGlobal.as_view()),
    path('absancedetail/<int:pk>/', views.AbsanceDetail.as_view()),

    path('sanction/', views.SanctionGlobal.as_view()),
    path('sanctiondetail/<int:pk>/', views.SanctionDetail.as_view()),

    path('randement/', views.RandementGlobal.as_view()),
    path('randementdetail/<int:pk>/', views.RandementDetail.as_view()),

    path('conge/', views.CongeGlobal.as_view()),
    path('congedetail/<int:pk>/', views.CongeDetail.as_view()),

]