##
# By @simonbs
# http://simonbs.dk/
##

import sys
import webbrowser
import string

def show_timeline(query = ""):
  open_url(url_with_screenname_and_resource(query, "timeline"))
  
def show_mentions(query = ""):
  open_url(url_with_screenname_and_resource(query, "mentions"))
  
def show_retweets(query = ""):
  open_url(url_with_screenname_and_resource(query, "retweets"))

def show_direct_messages(query = ""):
  open_url(url_with_screenname_and_resource(query, "direct_messages"))
  
def show_lists(query = ""):
  open_url(url_with_screenname_and_resource(query, "lists"))
  
def show_favorites(query = ""):
  open_url(url_with_screenname_and_resource(query, "favorites"))
  
def show_search(query = ""):
  open_url(url_with_screenname_and_resource(query, "search"))
  
def show_user_profile(query = ""):
  open_url(url_with_args("tweetbot:///user_profile/<0>", query))
  
def follow_user(query = ""):
  open_url(url_with_args("tweetbot:///follow/<0>", query))
  
def unfollow_user(query = ""):
  open_url(url_with_args("tweetbot:///unfollow/<0>", query))
  
def post_tweet(query = ""):
  args = arguments(query)
  if len(args) == 0:
    url = "tweetbot:///post"
  elif len(args) > 0:
    url = url_with_args("tweetbot:///post?text=<0>", query)
  open_url(url)
  
def url_with_screenname_and_resource(screenname, resource):
  url = "tweetbot://"
  if screenname is not "":
    url = "%s<0>" % (url)
  url = "%s/%s" % (url, resource)
  return url_with_args(url, screenname)

def url_with_args(url, args):
  if type(args) is str:
    args = [ args ]
  i = 0
  while i < len(args):
    url = url.replace(("<%s>" % (i)), args[i])
    i += 1
  return url
  
def arguments(query):
  if query == "":
    return []
  return query.split(" ")
  
def open_url(url):
  if url is not None:
    webbrowser.open(url)
