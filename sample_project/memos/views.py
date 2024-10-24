from .models import Memo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .tasks import create_ai_comment

class MemoListView(ListView):
    model = Memo

    def get_queryset(self):
        return Memo.objects.all().order_by('-created_at')

class MemoCreateView(CreateView):
    model = Memo
    fields = ['content']
    success_url = reverse_lazy('memos:memo-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        create_ai_comment.delay_on_commit(self.object.id)
        return response