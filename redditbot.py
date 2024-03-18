import praw  
# praw stands for => python reddit API wrapper
# like telegram apps, you need keys for reddit apps too
# go to reddit.com/prefs/apps  => from there create your app

# build the instance
reddit = praw.Reddit(client_id="your c id",
                     client_secret="your c s",
                     user_agent="myBot/0.0.1")

# login to reddit
reddit.user.me()

# get data from reddit
sub_reddit = reddit.subreddit("learnPython")
for submission in sub_reddit.hot(limit=5):
    print(submission.title)
    if not submission.stickied:
        print(f"title: {submission.title}")
        print(f"score: {submission.score}")


# posting to reddit
reddit.post( title= "blah blah",
    selftext = "blaaaaaaahhhh")

reddit.random_subreddit("random things")

reddit.comment()
reddit.delete()
reddit.get()
reddit.inbox.messages()
reddit.inbox.all()
reddit.live.info()

ids = ["3rgnbke2rai6hen7ciytwcxadi", "sw7bubeycai6hey4ciytwamw3a", "t8jnufucss07"]
for thread in reddit.live.info(ids):
        print(thread.title)

# can you see how much python is amazing? 
        
reddit.redditors.new()
reddit.multireddit.create()

reddit.request()

reddit.submission()

reddit.user.blocked()
reddit.user.friends()
reddit.user.contributor_subreddits()
reddit.user.karma()
reddit.user.moderator_subreddits()

for subreddit in reddit.user.moderator_subreddits(limit=None):
        print(str(subreddit))



# just like that :) / Uncle Bamdad