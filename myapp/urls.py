from . import views
from django.urls import path
from django.conf.urls import handler404, handler500

handler404 = 'myapp.views.custom_404'
handler500 = 'myapp.views.custom_500'

urlpatterns = [
    path("",views.index,name="index"),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout"),
    path("create",views.create,name="create"),
    path("profile/<int:id>",views.profile,name='profile'),
    path("profile/edit/<int:id>",views.profileedit,name='profileedit'),
    path("post/<int:id>",views.post,name="post"),
    path("post/edit/<int:id>",views.editpost,name="editpost"),
    path("post/delete/<int:id>", views.deletepost, name="deletepost"),

    
    
]
