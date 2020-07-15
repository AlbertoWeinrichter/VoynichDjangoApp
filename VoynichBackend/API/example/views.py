from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from API.example.tasks import example_task

logger = logging.getLogger(__name__)


class TestTask(APIView):
    permission_classes = ()

    def get(self, request):
        """
        A test celery task
        """
        example_task.delay("test argument")

        return Response({"results": "222"})
