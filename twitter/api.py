import requests
from requests_oauthlib import OAuth1
from builtins import all, AssertionError, getattr


class Api:

    def __init__(self,
                 url_builder,
                 consumer_key=None,
                 consumer_secret=None,
                 access_token_key=None,
                 access_token_secret=None,
                 base_url=None):

        if not all([
            access_token_key, access_token_secret,
            consumer_key, consumer_secret
        ]):
            raise AssertionError

        self._url_builder = url_builder(
            base_url or 'https://api.twitter.com/1.1'
        )
        self._auth = OAuth1(
            consumer_key, consumer_secret,
            access_token_key, access_token_secret
        )
        self._session = requests.Session()

    def get_home_timeline(self, since_id=None):
        return self._session.get(
            self._url_builder.url_home_timeline(since_id),
            auth=self._auth
        ).content.decode('utf-8')
