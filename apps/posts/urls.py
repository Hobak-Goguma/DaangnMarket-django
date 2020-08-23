from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from posts import views

urlpatterns = [
    # path('product/<title>', views.product_thumbnail, name='product_thumbnail'),
    path('upload', views.upload_file, name='imagetest'),
    path('product/<int:id_product>', views.product_thumbnail, name='productThumbnail'),
    path('company', views.company_list, name='company_list'),
    path('company/<int:id_company>', views.company_detail, name='company_detail'),
    path('company/search', views.location_search_company, name='location_search_company'),
    path('product/search', views.location_search, name='location_search'),
    path('product/search/category', views.product_category, name='product_category'),
    path('product/<int:id_product>', views.product_detail, name='prduct_detail'),
    path('product', views.product_list, name='prduct_list'),
    path('product/<id_product>', views.product_detail, name='prduct_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)