

class UrlBuilder:
    def __init__(self, base_url):
        self._base_url = base_url

    def url_home_timeline(self, since_id=None):
        url = '{}/statuses/home_timeline.json?'.format(
            self._base_url
        )

        if since_id:
            url = url + 'since_id={}'.format(since_id)

        return url
