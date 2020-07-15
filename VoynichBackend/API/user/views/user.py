import logging

from django.shortcuts import get_object_or_404
from haystack.query import SearchQuerySet
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from API.user.models.user import User
from API.user.serializers.user import UserSerializer

logger = logging.getLogger(__name__)


class UserAutocomplete(APIView):
    permission_classes = ()

    def get(self, request):
        """
        A string of more than 2 characters will return the 5 closest results
        """
        search_term = request.query_params.get('search_term')
        sqs = SearchQuerySet().autocomplete(username=search_term)
        results = [result.object for result in sqs]

        print(results[:5])

        return Response({"results": results})


class UserView(APIView):
    """
    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, username):
        """
        View individual user
        """
        user = get_object_or_404(User, username=username)
        serialized_user = UserSerializer(user).data
        return Response(serialized_user)

    @staticmethod
    def delete(request, user_id):
        """
        Delete user
        """
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def post(request):
        """
        Update avatar S3 url, avatar or email
        """
        data = request.data.get('data')
        try:
            allowed = ["username", "email", "avatar", "avatar_cropped"]
            for k, v in data.items():
                if k in allowed:
                    request.user.__setattr__(k, v)

            request.user.save()
            return Response(status=status.HTTP_200_OK)

        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        Login a user user
        """
        user = request.user
        return Response(UserSerializer(user).data)
