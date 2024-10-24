from django.urls import path
from .views import MemoListView, MemoCreateView

app_name = "memos"

urlpatterns = [
    path("", MemoListView.as_view(), name="memo-list"),
    path("create/", MemoCreateView.as_view(), name="memo-create"),
]