from .models import Book
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet #Use readonly for get and retrieve method only
from .serializers import BookSerializer

class BookModelViewSet(ModelViewSet):
    serializer_class  = BookSerializer
    queryset = Book.objects.all()