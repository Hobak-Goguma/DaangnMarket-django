from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter

from posts import views
from posts.views.product_category_list import ProductCategoryList
from posts.views.product_my_list_views import ProductMyList
from posts.views.recommend_product_list_views import RecommendProductListViewSet

router = DefaultRouter()
router.register('recommend', RecommendProductListViewSet)

urlpatterns = [
    # path('product/<title>', views.product_thumbnail, name='product_thumbnail'),
    # path('product/<int:id_product>', views.product_thumbnail, name='productThumbnail'),
    path('product/upload/', views.product_upload_file, name='product_upload'),
    path('company/', views.company_list, name='company_list'),
    path('company/<int:id_company>/', views.company_detail, name='company_detail'),
    path('company/upload/', views.company_upload_file, name='company_upload'),
    path('company/search/', views.location_search_company, name='location_search_company'),
    path('product/', views.product_list, name='prduct_list'),
    path('product/search/', views.location_search_product, name='location_search_product'),
    path('product/search/category/', views.product_category_search, name='product_category_search'),
    path('product/my-list/', ProductMyList.as_view(), name='my_product'),
    path('product/<int:id_product>/', views.product_detail, name='prduct_detail'),
    path('product/category-list/', ProductCategoryList.as_view(), name='ProductCategoryList'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
