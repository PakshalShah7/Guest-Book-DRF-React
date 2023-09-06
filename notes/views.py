from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializers import NoteSerializer


class NotesViewset(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
