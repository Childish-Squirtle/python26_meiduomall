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
            "counts": self.page.paginator.count,#总数量
            "lists": data,#用户数据
            "page": self.page.number,#当前页数
            "pages": self.page.paginator.num_pages,#总页数
            "pagesize": self.page_size#页容量
        })