
class StockSpanner:

    def __init__(self):
        self.array = []

    def next(self, price: int) -> int:
        stack = self.array
        span = 1
        quote = price
        while stack and stack[-1][0] <= quote:
            prevQuote,prevSpan = stack.pop()
            span += prevSpan
        self.array.append((quote,span))
        return span

# We have to get the amount of days the newest quote has spanned
# were a span is the consective days that the quote is less than or equal
# to the current quote.
# Each loop checks if the quote is bigger than the one ontop of the stack
# This condenses the stack to store the numbers that bigger than the
# previous entries and how many it has spanned.
# If a smaller number gets added, it means the span has broke and it is added
# to the top of the stack.
# O(n), O(1) space
S = StockSpanner()
S.next(100)
S.next(80)
S.next(60)
S.next(70)
S.next(60)
S.next(75)
S.next(85)
# output = [null,1,1,1,2,1,4,6]
