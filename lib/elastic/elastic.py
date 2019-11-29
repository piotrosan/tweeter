from elasticsearch import Elasticsearch


class ElasticSearch:

    def __init__(self, host=None, port=None):
        self._es = Elasticsearch([{
            'host': 'elastic',
            'port': '9200'
        }])

    def index(self, tweet_id, content):
        return self._es.index(index='tw', doc_type='tweet', id=tweet_id, body=content)
