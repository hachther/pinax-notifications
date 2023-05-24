from django.urls import path

from .views import NoticeSettingsView, NoticeSettingView

app_name = "pinax_notifications"

urlpatterns = [
    path("settings/", NoticeSettingsView.as_view(), name="notice_settings"),
    path("setting/<uuid:key>/", NoticeSettingView.as_view(), name="notice_setting"),
]
