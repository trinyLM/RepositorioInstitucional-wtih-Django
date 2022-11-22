from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'info': {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'prev': self.get_previous_link()
            },

            'results': data
        })
