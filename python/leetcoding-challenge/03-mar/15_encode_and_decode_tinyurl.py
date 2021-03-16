"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
to the original URL.
"""


class Codec:

    def __init__(self):
        self.longToShort = {}
        self.key = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        if longUrl in self.longToShort:
            return self.longToShort[longUrl]
        else:
            self.key += 1
            shortUrl = "http://tinyurl.com/" + str(self.key)
            self.longToShort[shortUrl] = longUrl

            return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.longToShort[shortUrl] if shortUrl in self.longToShort else shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
