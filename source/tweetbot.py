##
# By @simonbs
# http://simonbs.dk/
##

import webbrowser
import string

# Show timeline
def show_timeline(query = ""):
  open_url(url_with_screenname_and_resource(query, "timeline"))
  
# Show mentions
def show_mentions(query = ""):
  open_url(url_with_screenname_and_resource(query, "mentions"))
  
# Show retweets
def show_retweets(query = ""):
  open_url(url_with_screenname_and_resource(query, "retweets"))

# Show direct messages
def show_direct_messages(query = ""):
  open_url(url_with_screenname_and_resource(query, "direct_messages"))
  
# Show lists
def show_lists(query = ""):
  open_url(url_with_screenname_and_resource(query, "lists"))
  
# Show favorites
def show_favorites(query = ""):
  open_url(url_with_screenname_and_resource(query, "favorites"))
  
# Show search
def show_search(query = ""):
  open_url(url_with_screenname_and_resource(query, "search"))
  
# Show a user profile
def show_user_profile(query = ""):
  open_url(url_with_args("tweetbot:///user_profile/<0>", query))
  
# Follow a user
def follow_user(query = ""):
  open_url(url_with_args("tweetbot:///follow/<0>", query))
  
# Unfollow a user
def unfollow_user(query = ""):
  open_url(url_with_args("tweetbot:///unfollow/<0>", query))
  
# Post a tweet
def post_tweet(query = ""):
  args = arguments(query)
  if len(args) == 0:
    url = "tweetbot:///post"
  elif len(args) > 0:
    url = url_with_args("tweetbot:///post?text=<0>", query)
  open_url(url)
  
# Create URL with screen name and resource
def url_with_screenname_and_resource(screenname, resource):
  url = "tweetbot://"
  if screenname is not "":
    url = "%s<0>" % (url)
  url = "%s/%s" % (url, resource)
  return url_with_args(url, screenname)

# Create URL with arguments
def url_with_args(url, args):
  if type(args) is str or type(args) is unicode:
    args = [ args ]
  i = 0
  while i < len(args):
    url = url.replace(("<%s>" % (i)), args[i])
    i += 1
  return url
  
# Retrieve arguments from query
def arguments(query):
  if query == "":
    return []
  return query.split(" ")

# Opens a URL
def open_url(url):
  if url is not None:
    webbrowser.open(url)