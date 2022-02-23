import urllib,json
class work_horse:
    def url_request(self,url):
        try:
            with urllib.request.urlopen(url) as request:
                return request.read()
        except:
            return None
        finally:
            pass
    def json_loads(self,json_string):
        return json.loads(json_string)
