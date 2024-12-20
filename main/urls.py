from django.urls import path
from main.views import register, login_user, logout_user, show_main, create_shop_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, edit_shop, delete_shop, add_shop_entry_ajax, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-shop-entry', create_shop_entry, name='create_shop_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-shop/<uuid:id>', edit_shop, name='edit_shop'),
    path('delete/<uuid:id>', delete_shop, name='delete_shop'),
    path('add-shop-entry-ajax', add_shop_entry_ajax, name='add_shop_entry_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]