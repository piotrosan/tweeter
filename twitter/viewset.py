import json
import datetime
import twitintegr.settings as settings

from rest_framework import viewsets
from rest_framework.response import Response

from twitter.api import Api
from twitter.url_builder import UrlBuilder
from lib.elastic.elastic import ElasticSearch

from twitter.models import LastSync


class TweetList(viewsets.ViewSet):
    name = 'tweet-list'

    def list(self, request):
        tweet_list = []
        max_value = None
        modify = False
        e = ElasticSearch()

        last_sycn = LastSync.objects.last()
        if last_sycn:
            max_value = last_sycn.tweet_id

        api = Api(
            UrlBuilder,
            settings.CONSUMER_API_KEY,
            settings.CONSUMER_API_SECRET_KEY,
            settings.ACCESS_TOKEN,
            settings.ACCESS_TOKEN_SECRET_KEY
        )

        responses = json.loads(api.get_home_timeline(since_id=max_value))
        if (isinstance(responses, dict) and responses.get('errors', None)) or not responses:
            return Response([])

        for response in responses:
            if not max_value or max_value < int(response['id']):
                max_value = int(response['id'])
                modify = True

            content = {
                'id': response['id'],
                'text': response['text']
            }

            e.index(response['id'], content)
            tweet_list.append(content)

        if modify:
            LastSync.objects.create(
                tweet_id=max_value,
                date=datetime.datetime.now()
            )

        return Response(tweet_list)

