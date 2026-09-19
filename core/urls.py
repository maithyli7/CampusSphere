from . import auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", auth_views.login_view, name="login"),
    path("logout/", auth_views.logout_view, name="logout"),
    path("student-dashboard/", views.student_dashboard, name="student_dashboard"),
    path("notices/", views.notices, name="notices"),
path("events/", views.events, name="events"),
path("study-materials/", views.study_materials, name="study_materials"),
path("lost-found/", views.lost_found, name="lost_found"),
path("calendar/", views.calendar, name="calendar"),
path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
]