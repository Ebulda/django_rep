from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.products_view),
    path('products/create_products/', views.product_create),
    path('products/<int:prod_id>/', views.product_detail_view),
    path('category/', views.category_view),
    path('create_categories/', views.category_create),
    path('create_reviews/<int:product_id>/', views.review_create),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
