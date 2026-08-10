import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.timestamp = 0  # Decreasing timestamp for recency
        self.user_tweets = defaultdict(list)   # userId -> list of [timestamp, tweetId]
        self.user_follows = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store tweet with a timestamp (using negative for max-heap behavior)
        self.user_tweets[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        # Ensure the user sees their own tweets
        self.user_follows[userId].add(userId)

        for followeeId in self.user_follows[userId]:
            tweets = self.user_tweets[followeeId]
            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]
                # Push latest tweet of each followee onto the heap
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])

        while heap and len(feed) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx >= 0:
                next_time, next_tweetId = self.user_tweets[user][idx]
                heapq.heappush(heap, [next_time, next_tweetId, user, idx - 1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId] and followerId != followeeId:
            self.user_follows[followerId].remove(followeeId)
