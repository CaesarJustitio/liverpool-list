from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, increase_amount, decrease_amount, delete_item, edit_item, get_item_json, add_item_ajax


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase_amount/<int:item_id>/', increase_amount, name='increase_amount'),
    path('decrease_amount/<int:item_id>/', decrease_amount, name='decrease_amount'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
]