import json
import requests

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import views
from rest_framework.response import Response

API_URL = 'https://api.stackexchange.com/2.2/search/advanced'
API_KEY = 'U4DMV*8nvpm3EOpvf69Rxw(('
API_FILTER = '!9Z(-x.0nI'
API_SITE = 'stackoverflow'


@method_decorator(cache_page(60 * 60 * 24), name='dispatch')    # 1 day
class SearchView(views.APIView):
    def get(self, request):
        url_params = request.GET.urlencode()
        data = requests.get(
            '{0}?key={1}&filter={2}&site={3}&{4}'.format(
                API_URL, API_KEY, API_FILTER, API_SITE, url_params
            )
        )
        return Response(json.loads(data.content))
