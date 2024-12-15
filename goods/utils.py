from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from goods.models import Products
# from django.db.models import Q


def q_search(query):
    if query:
        return Products.objects.filter(name__icontains=query)

    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    result = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0.1).order_by("-rank")
    
    return result

    # keywords = [word for word in query.split(' ') if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)
