from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class MyPage(PageNumberPagination):
    page_size = 5
    page_size_query_param = "pagesize"
    page_query_param = "page"
    max_page_size = 10

    def get_paginated_response(self, data):
        # data就是分页显示的数据内容
        return Response({
            "counts": self.page.paginator.count,
            "lists": data,
            "page": self.page.number,
            "pages": self.page.paginator.num_pages,
            "pagesize": self.page_size
        })