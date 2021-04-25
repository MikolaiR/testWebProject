from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView

from todo.models import Note


class NoteView(ListView):
    model = Note
    context_object_name = "notes"


class NoteCreateView(CreateView):
    model = Note
    fields = "__all__"
    success_url = "list"


def note_delete(request, note_id):
        note = Note.objects.get(pk=note_id)
        note.delete()
        return redirect("todo:note_list")

