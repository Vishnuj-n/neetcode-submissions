class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        self.time[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""

        arr = self.time[key]
        l, h = 0, len(arr) - 1
        ans = ""

        while l <= h:
            mid = (l + h) // 2
            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                l = mid + 1
            else:
                h = mid - 1

        return ans