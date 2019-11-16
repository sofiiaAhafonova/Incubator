from django.urls import path, include
from forum import views
from django.contrib.auth.decorators import login_required
from django.conf import settings # new
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('forum/', views.PostListView.as_view(), name='forum'),
    path('create_post/', login_required(views.CreatePostView.as_view()), name='create_post'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)