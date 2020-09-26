from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from common import views
from common.views import *

from common.views.sigungu_eupmyundong_view import SigunguList, EupmyundongList, SidoEupmyundongList
#
# router = DefaultRouter()
# router.register(r'member-test', MemberViewSet, basename='member-test')

urlpatterns = [
	path('member', MemberListView.as_view(), name='member_list'),
	path('member/login', views.member_login, name='login'),
	path('member/overlap', views.member_overlap, name='member_overlap'),
	path('member/overlap/nick-name', views.nick_name_overlap, name='nick_name_overlap'),
	path('member/id/<id_member>', MemberDetail.as_view(), name='member_detail'),
	path('member/info', views.member_info, name='member_touch'),
	path('member/addr/id/<id_member>', views.member_addr, name='member_addr'),
	path('member/addr/create', views.member_addr_create, name='member_addr_create'),
	path('member/addr/select', views.member_addr_dis_update, name='member_addr_dis_update'),
	path('test', views.test, name='test'),
	path('wishlist', views.wishlist_list, name='wishlist_list'),
	path('wishlist/<id_member>', views.wishlist_detail, name='wishlist_detail'),
	path('product/selling/<id_member>', views.selling_product_list, name='selling_product_list'),
	path('review/seller', views.seller_review, name='seller_review_list'),
	path('review/shopper', views.shopper_review, name='shopper_review_list'),
	path('member/upload', views.member_upload_file, name='member_upload_file'),
	path('sigungu/<str:sido>', SigunguList.as_view(), name='sigungu'),
	path('eupmyundong/<str:sido>/<str:sigungu>', EupmyundongList.as_view(), name='eupmyundong'),
	path('eupmyundong/<str:sido>', SidoEupmyundongList.as_view(), name='sido_eupmyundong_list'),
]

# urlpatterns += router.urls

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
	                      document_root=settings.MEDIA_ROOT)
