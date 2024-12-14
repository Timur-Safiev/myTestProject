from django.db.models import Q

from goods.models import Products

def q_search(query):
    if query:
        return Products.objects.filter(name__icontains=query)
    
    keywords = [word for word in query.split(' ') if len(word) > 2]
    
    q_objects = Q()
    
    for token in keywords:
        q_objects |= Q(name__icontains=token)
        
    return Products.objects.filter(q_objects)
