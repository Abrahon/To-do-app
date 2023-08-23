from django .urls import path
# from . import views
from tasks . views import home, store_task,show_task,edit_task,delete_task,complete_task


urlpatterns = [
    path('',home),
    path('store_new_task/',store_task, name ='store_task'),
    path('show_task/',show_task, name = 'show_task'),
    path('edit_task/<int:id>',edit_task,name ='edit_task'),
    path('delete_task/<int:id>',delete_task,name='delete_task'),
    path('complete_task/<int:id>',complete_task,name='complete_task'),
]
