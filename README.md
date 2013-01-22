Tweetbot Workflow for Alfred 2.0
===

A workflow for Alfred 2.0 which lets the user control Tweetbot.

![](http://f.cl.ly/items/010S1v0F091z300H1U3j/alfred-tweetbot-workflow.png)

The workflow is written in Python and uses the [Tweetbot URL scheme](http://tapbots.com/blog/development/tweetbot-url-scheme).

Currently, the following commands are supported. Parameters in brackets are optional and parameters in square brackets are required. When an account name can be specified and none is specified, the current account will be used.
If two commands are seperated ”|” it’s because there are several ways to write the command and you should just choose one of them. E.g. ”tb rt” and ”tb retweets” is the same.

- **tb n|new|tweet (message)** Posts a new tweet.
- **tb t|timeline (account name)** Shows the timeline of specified account.
- **tb user [screen name]** Shows the user profile of the user with the specified screen name.
- **tb m|mentions (account name)** Shows the mentions for the specified account.
- **tb rt|retweets (account name)** Shows the retweets which appears in the accounts timeline.
- **tb dm|directmessages|messages (account name)** Shows the direct messages that the account has received.
- **tb l|lists (account name)** Shows the lists that the account owns.
- **tb favs|favorites (account name)** Shows the tweets the account has marked as favorited.
- **tb s|search (account name)** Searches using the specified account. (Note: Sadly this doesn't seem to work with the 'query' parameter on OS X)
- **tb f|follow [screen name]** Follows the user with the specified screen name.
- **t u|unfollow [screen name]** Unfollows the user with the specified screen name.

You think the commands are hard to remember? Don’t worry. They will be autocompleted when you write ”tb”. I have chosen that the commands should not be written out. E.g. ”tb retweets” and ”

About
===
This workflow is developed by [@simonbs](http://twitter.com/simonbs).