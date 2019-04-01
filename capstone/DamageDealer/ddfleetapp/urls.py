from django.urls import path
from . import views

urlpatterns = [
    path('', views.DmgDealerHome.as_view(), name='home'),
    path('fleet/new', views.DmgDealerCreateFleet.as_view(), name='dd_new'),
    path('fleet/<int:pk>/', views.DmgDealerFleetDetails.as_view(), name='dd_detail'),
    path('fleet/ddfleets', views.DmgDealerFleetList.as_view(), name='dd_list'),
    path('fleet/<int:pk>/delete/', views.DmgDealerDeleteFleet.as_view(), name='dd_delete'),
    path('fleet/<int:pk>/edit/', views.DmgDealerEditFleet.as_view(), name='dd_edit'),
    path('fleet/<int:pk>/edit/addcard', views.add_cards, name='dd_add'),
    path('fleet/<int:pk>/edit/cardstoadd', views.postdata, name='dd_addcard'),
    path('fleet/<int:pk>/edit/cardnum', views.DmgDealerCardAmount.as_view(), name='dd_cardnum'),
    path('fleet/<int:pk>/edit/carddelete', views.DmgDealerDeleteCard.as_view(), name='dd_carddel'),
    path('fleet/<int:pk>/print', views.DmgDealerPrintDetails.as_view(), name='dd_print'),
]