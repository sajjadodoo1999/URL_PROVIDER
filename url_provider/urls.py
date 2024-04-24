from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_function, name='index'),
    path('login/', views.login_function, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_description/', views.add_description, name='add_description'),
    path('edit_description/<str:pk>', views.edit_description, name='edit_description'),
    path('delete_description/<str:pk>', views.delete_description, name='delete_description'),
    # path('hadith_text/<str:pk>', views.hadith_text, name='hadith_text'),
    path('logout/', views.logout_function, name='logout'),
    path('status/<str:pk>', views.status, name='status'),
    # path('download_pdf/<str:pk>',views.download_pdf,name='download_pdf'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)