import praw  
# praw stands for => python reddit API wrapper
# like telegram apps, you need keys for reddit apps too
# go to reddit.com/prefs/apps  => from there create your app

reddit = praw.Reddit(client_id="your c id",
                     client_secret="your c s",
                     user_agent="myBot/0.0.1")