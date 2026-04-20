from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from health.views import *
from .apirep import routerep

urlpatterns = [

    # API
    path('api/v1/', include(routerep.urls)),

    # ADMIN
    path('admin/', admin.site.urls),

    # HOME PAGES
    path('', Home, name="home"),
    path('patient_home/', User_Home, name="patient_home"),
    path('doctor_home/', Doctor_Home, name="doctor_home"),
    path('admin_home/', Admin_Home, name="admin_home"),

    # BASIC PAGES
    path('about/', About, name="about"),
    path('contact/', Contact, name="contact"),
    path('gallery/', Gallery, name="gallery"),

    # AUTH
    path('login/', Login_User, name="login"),
    path('login_admin/', Login_admin, name="login_admin"),
    path('signup/', Signup_User, name="signup"),
    path('logout/', Logout, name="logout"),
    path('change_password/', Change_Password, name="change_password"),

    # HEART DATA
    path('add_heartdetail/', add_heartdetail, name="add_heartdetail"),
    path('view_search_pat/', view_search_pat, name="view_search_pat"),
    path('profile_doctor/view_search_pat/', view_search_pat, name="view_search_pat"),  # FIXED

    path('predict_desease/<str:pred>/<str:accuracy>/', predict_desease, name="predict_desease"),

    # DOCTOR
    path('view_doctor/', View_Doctor, name="view_doctor"),
    path('add_doctor/', add_doctor, name="add_doctor"),
    path('change_doctor/<int:pid>/', add_doctor, name="change_doctor"),

    # PATIENT
    path('view_patient/', View_Patient, name="view_patient"),

    # PROFILE
    path('edit_profile/', Edit_My_deatail, name="edit_profile"),
    path('profile_doctor/', View_My_Detail, name="profile_doctor"),

    # FEEDBACK
    path('sent_feedback/', sent_feedback, name="sent_feedback"),
    path('view_feedback/', View_Feedback, name="view_feedback"),

    # DELETE ACTIONS
    path('delete_searched/<int:pid>/', delete_searched, name="delete_searched"),
    path('delete_doctor/<int:pid>/', delete_doctor, name="delete_doctor"),
    path('assign_status/<int:pid>/', assign_status, name="assign_status"),
    path('delete_patient/<int:pid>/', delete_patient, name="delete_patient"),
    path('delete_feedback/<int:pid>/', delete_feedback, name="delete_feedback"),
]

# MEDIA FILES
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)