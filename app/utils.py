

def paginated_response(result, paginated_query):
     return {
            'results': result,
            'total': paginated_query.count(),
        }