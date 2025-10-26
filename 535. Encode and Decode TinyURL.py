import random
import string

class Codec:
    def __init__(self):
        self.url_map = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        while key in self.url_map:
            key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[key] = longUrl
        return self.base + key

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.split("/")[-1]
        return self.url_map.get(key, "")
