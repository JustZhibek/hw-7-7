from django.contrib import admin
from django.urls import path
from product import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.CategoryAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/categories/<int:id>/', views.CategoryAPIView.as_view({'get': 'retrieve',
                                                                       'put': 'update',
                                                                       'delete': 'destroy'})),
    path('api/v1/products/', views.ProductsAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/<int:id>/', views.ProductsAPIView.as_view({'get': 'retrieve',
                                                                     'put': 'update',
                                                                     'delete': 'destroy'})),
    path('api/v1/reviews/', views.ReviewsAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews/<int:id>/', views.ReviewsAPIView.as_view({'get': 'retrieve',
                                                                   'put': 'update',
                                                                   'delete': 'destroy'})),
    path('api/v1/products/reviews/', views.ProductsReviewsAPIView.as_view()),
    path('api/v1/users/', include('users.urls'))

]