##
# By @simonbs
# http://simonbs.dk/
##

import tweetbot
import json
import string
from Feedback import Feedback

# Creates feedback for a query
def tweetbot_helper(query = ""):
  feedback = Feedback()
  args = string.split(query, " ")
  if args[0] == "n" or args[0] == "new" or args[0] == "tweet":
    item = build_post_tweet_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "t" or args[0] == "timeline":
    item = build_show_timeline_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "m" or args[0] == "mentions":
    item = build_show_mentions_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "rt" or args[0] == "retweets":
    item = build_show_retweets_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "dm" or args[0] == "directmessages" or args[0] == "messages":
    item = build_show_direct_messages_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "l" or args[0] == "lists":
    item = build_show_lists_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "favs" or args[0] == "favorites":
    item = build_show_favorites_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "s" or args[0] == "search":
    item = build_show_search_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "user":
    item = build_show_user_profile_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "f" or args[0] == "follow":
    item = build_follow_item(args)
    feedback.add_item(item["title"], "", item["args"])
  elif args[0] == "u" or args[0] == "unfollow":
    item = build_unfollow_item(args)
    feedback.add_item(item["title"], "", item["args"])
  else:
    feedback.add_item("Post tweet", "", "", "no", "n")
    feedback.add_item("Show timeline", "", "", "no", "t")
    feedback.add_item("Show mentions", "", "", "no", "m")
    feedback.add_item("Show retweets", "", "", "no", "rt")
    feedback.add_item("Show direct messages", "", "", "no", "dm")
    feedback.add_item("Show lists", "", "", "no", "l")
    feedback.add_item("Show favorites", "", "", "no", "favs")
    feedback.add_item("Show search", "", "", "no", "s")
    feedback.add_item("Show user profile", "", "", "no", "user ")
    feedback.add_item("Follow", "", "", "no", "f ")
    feedback.add_item("Unfollow", "", "", "no", "u ")
  return feedback
 
# Runs a command, taking a JSON string which uses single quotes as input.
def run_command(query):
  print query
  args = json.loads(query.replace("'", "\""))
  print args
  command = args["command"]
  if command == "post_tweet":
    tweetbot.post_tweet(args["contents"])
  elif command == "show_timeline":
    tweetbot.show_timeline(args["user"])
  elif command == "show_mentions":
    tweetbot.show_mentions(args["user"])
  elif command == "show_retweets":
    tweetbot.show_retweets(args["user"])
  elif command == "show_direct_messages":
    tweetbot.show_direct_messages(args["user"])
  elif command == "show_lists":
    tweetbot.show_lists(args["user"])
  elif command == "show_favorites":
    tweetbot.show_favorites(args["user"])
  elif command == "show_search":
    tweetbot.show_search(args["user"])
  elif command == "show_user_profile":
    tweetbot.show_user_profile(args["user_profile"])
  elif command == "follow":
    tweetbot.follow_user(args["follow"])
  elif command == "unfollow":
    tweetbot.unfollow_user(args["unfollow"])
    
# Builds a feedback item for posting a tweet
def build_post_tweet_item(args):
  if len(args) == 1 or args[1] == "":
    contents = ""
    out_args = { }
    title = "Post tweet"
  else:
    contents = " ".join(args[1:])
    title = "Post tweet with contents"
  out_args = { "command": "post_tweet", "contents": contents }
  return { "title": title, "args": json_args(out_args) }
    
# Builds a feedback item for showing the timeline
def build_show_timeline_item(args):
  return build_simple_user_item("show_timeline", "Show timeline", args)
    
# Builds a feedback item for showing mentions
def build_show_mentions_item(args):
  return build_simple_user_item("show_mentions", "Show mentions", args)
  
# Builds a feedback item for showing retweets
def build_show_retweets_item(args):
  return build_simple_user_item("show_retweets", "Show retweets", args)
  
# Builds a feedback item for showing direct messages
def build_show_direct_messages_item(args):
  return build_simple_user_item("show_direct_messages", "Show direct messages", args)
  
# Builds a feedback item for showing lists
def build_show_lists_item(args):
  return build_simple_user_item("show_lists", "Show lists", args)
  
# Builds a feedback item for showing favorites
def build_show_favorites_item(args):
  return build_simple_user_item("show_favorites", "Show favorites", args)
  
# Builds a feedback item for showing search
def build_show_search_item(args):
  return build_simple_user_item("show_search", "Show search", args)

# Builds a feedback item for showing a user profile
def build_show_user_profile_item(args):
  if len(args) == 1 or args[1] == "":
    user_profile = "..."
    out_args = { }
  else:
    user_profile = " ".join(args[1:])
    out_args = { "command": "show_user_profile", "user_profile": user_profile }
  title = "Show profile for '%s'" % (user_profile)
  return { "title": title, "args": json_args(out_args) }
  
# Builds a feedback item for following a user
def build_follow_item(args):
  if len(args) == 1 or args[1] == "":
    follow = "..."
    out_args = { }
  else:
    follow = " ".join(args[1:])
    out_args = { "command": "follow", "follow": follow }
  title = "Follow '%s'" % (follow)
  return { "title": title, "args": json_args(out_args) }

# Builds a feedback item for unfollowing a user
def build_unfollow_item(args):
  if len(args) == 1 or args[1] == "":
    unfollow = "..."
    out_args = { }
  else:
    unfollow = " ".join(args[1:])
    out_args = { "command": "unfollow", "unfollow": unfollow }
  title = "Unfollow '%s'" % (unfollow)
  return { "title": title, "args": json_args(out_args) }
  
# Builds a simple feedback item with a command and a title.
# Appends the user to the title if necessary and adds the user as argument.
def build_simple_user_item(command, base_title, args):
  if len(args) == 1 or args[1] == "":
    user = "..."
  else:
    user = " ".join(args[1:])
  out_args = { "command": command, "user": user }
  if len(args) == 1:
    title = base_title
  else:
    title = "%s for '%s'" % (base_title, user)
  return { "title": title, "args": json_args(out_args) }
  
# Creates single quoted JSON arguments from a list.
# Single quotes are used instead of double quotes because for some reason
# it doesn't work with double quotes through Alfred.
def json_args(args):
  return json.dumps(args).replace("\"", "'")
  
if __name__ == "__main__":
  tweetbot_helper("user")