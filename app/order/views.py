from rest_framework import generics, status
from rest_framework.response import Response


class GetOrderView(generics.GenericAPIView):
    @staticmethod
    def get(self):
        return Response(data={"message": "hello order"}, status=status.HTTP_200_OK)
