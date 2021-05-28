class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while (steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while (steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       # You are in "leetcode.com". Visit "google.com"
# b = [leetcode] f = [] cur = google.com
browserHistory.visit("facebook.com");     # You are in "google.com". Visit "facebook.com"
# b = [leetcode,google] f = [] cur = facebook.com
browserHistory.visit("youtube.com");      # You are in "facebook.com". Visit "youtube.com"
# b = [leetcode,google,face] f = [] cur = youtube
browserHistory.back(1);                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# b = [leetcode,google] f = [youtube] cur = face
browserHistory.back(1);                   # You are in "facebook.com", move back to "google.com" return "google.com"
# b = [leetcode] f = [youtube,face] cur = google
browserHistory.forward(1);                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
# b = [leetcode,google] f = [youtube] cur = face
browserHistory.visit("linkedin.com");     # You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                # You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
