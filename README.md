Tweetbot Workflow for Alfred 2.0
===

A workflow for Alfred 2.0 which lets the user control Tweetbot.

![](http://c.4su.re/M9w7/alfred-tweetbot-workflow.png)

The workflow is written in Python and uses the [Tweetbot URL scheme](http://tapbots.com/blog/development/tweetbot-url-scheme).

Currently, the following commands are supported. Parameters in brackets are optional and parameters in square brackets are required. When an account name can be specified and none is specified, the current account will be used.

- **t (message)** Posts a new tweet.
- **tt (account name)** Shows the timeline of specified account.
- **tu [screen name]** Shows the user profile of the user with the specified screen name.
- **tmm (account name)** Shows the mentions for the specified account. (Note: This command is 'tmm' because by default OS X will replace 'tm' with ™)
- **tr (account name)** Shows the retweets which appears in the accounts timeline.
- **tdm (account name)** Shows the direct messages that the account has received.
- **tl (account name)** Shows the lists that the account owns.
- **tf (account name)** Shows the tweets the account has marked as favorited.
- **ts (account name)** Searches using the specified account. (Note: Sadly this doesn't seem to work with the 'query' parameter on OS X)
- **tfo [screen name]** Follows the user with the specified screen name.
- **tun [screen name]** Unfollows the user with the specified screen name.

About
===
This workflow is developed by [@simonbs](http://twitter.com/simonbs).