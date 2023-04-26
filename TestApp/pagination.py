from rest_framework import pagination
from rest_framework.response import Response

# class Page(pagination.PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 10


# class Cursor(pagination.CursorPagination):
#     page_size = 1


class Limit(pagination.LimitOffsetPagination):
    pass


class Custom(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'

    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()     # type: ignore
        response['previous'] = self.get_previous_link()     # type: ignore
        return response
