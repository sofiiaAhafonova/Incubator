from django.urls import path
from django.conf import settings # new
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile'),
    path('edit_profile/<int:pk>/', login_required(views.ProfileUpdateView.as_view()), name='edit_profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)