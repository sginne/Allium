import urllib,json
class work_horse:
    def url_request(self,url):
        with urllib.request.urlopen(url) as request:
            return request.read()
    def json_loads(self,json_string):
        return json.loads(json_string)