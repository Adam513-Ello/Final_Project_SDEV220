from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('success/', views.success_page, name='success_page'),
    path('member_data/', views.member_data, name='member_data'),
    path('logout/', views.logout_view, name='logout'),
    path('redeem_item/<int:item_id>/', views.redeem_item, name='redeem_item'),
    path('purchase_item/<int:item_id>/', views.purchase_item, name='purchase_item'),
]
