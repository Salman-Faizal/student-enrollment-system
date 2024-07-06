from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
  page_size = 50    # Defining default page-size for paginated results
  page_size_query_param = 'page_size'    # Adding query parameter to dynamically set page-size in API requests
  max_page_size = 100    # Defining maximum allowed page-size to prevent excessive data retrieval
