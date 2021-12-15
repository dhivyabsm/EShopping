from .import views
from django.urls import path,re_path

urlpatterns=[
    path('user/',views.UserListCreateAPIView.as_view()),
    re_path('user/(?P<id>\d+)/$',views.UserPPDAPIView.as_view()),
    path('item/',views.ItemListCreateAPIView.as_view()),
    re_path('item/(?P<id>\d+)/$',views.ItemPPDAPIView.as_view()),
    path('purchase/',views.PurchaseListCreateAPIView.as_view()),
    re_path('purchase/(?P<id>\d+)/$',views.PurchasePPDAPIView.as_view()),
    path('cart/',views.CartListCreateAPIView.as_view()),
    re_path('cart/(?P<id>\d+)/$',views.CartPPDAPIView.as_view()),
]