
class Codec:
    def __init__(self):
        self.longToShort = {}
        self.shortToLong = {}
        self.alphabetAndNumbers = "abcdefghijklmnopqrstuvwxyz0123456789"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.longToShort:
            code = "".join(choices(self.alphabetAndNumbers,k=8))
            if code not in self.shortToLong:
                self.shortToLong[code] = longUrl
                self.longToShort[longUrl] = code
        return 'https://tinyurl.com/' + self.longToShort[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortToLong[shortUrl[-8:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# turns longUrl into a random Code consisting of 8 random letters and numbers
# store the url and code into a hash table so it can't be reused and is unique
# to decode, look for the code in the hashtable to get the original url
