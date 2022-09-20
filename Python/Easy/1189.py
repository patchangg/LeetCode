from collections import Counter

def maxNumberOfBalloons(text):
    c = Counter(text)
    return min(c["b"], c["a"], c["l"]//2, c["o"]//2, c["n"])

text = "nlaebolko"
maxBalloons = maxNumberOfBalloons(text)
print(maxBalloons)
