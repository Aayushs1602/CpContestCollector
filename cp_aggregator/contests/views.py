from rest_framework import viewsets
from .models import Contest
from .serializers import ContestSerializer

class ContestViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing contests.
    """
    queryset = Contest.objects.all().order_by('start_time')
    serializer_class = ContestSerializer
