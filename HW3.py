class SocialMedia:
    def __init__(self, name):
        self.social_media_name = name

    def getName(self):
        return self.social_media_name

class Instagram(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.posts = [];
        self.count = 0;

    def publishNewPost(self, body):
        for char in body:
            if (char.isalnum()) == True:
                self.count+=1
        if (self.count < 2200):
            self.posts.append(body)

    def getPosts(self):
        return self.posts

class Twitter(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.tweets = []
        self.count = 0;

    def createNewTweet(self, body):
        for char in body:
            if (char.isalnum()) == True:
                self.count+=1
        if (self.count < 280):
            self.tweets.append(body)

    def getTweets(self):
        return self.tweets





