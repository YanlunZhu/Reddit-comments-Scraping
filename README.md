# Reddit-comments-Scraping
Scrape the comments from subreddit and use GPT-2 analysis
The file do not need to use GPU. This file is only for:

1. Scrape data from Reddit
2. Clean data
3. Create a database
No GPT-2 application in this file.

I use Python PRAW package to scrape the Reddit's comments. There are some tutorials about how to apply PRAW API and get credentials from Reddit which are all in each section. You can find them below to see the detail.

To start:

1. Install PRAW API
2. Get credentials from Reddit
3. Identify you own subreddit (optional)

# Get Credentials:
https://www.reddit.com/prefs/apps

Before you can use any one of these with PRAW, you must first register an application of the appropriate type on Reddit.
If your application does not require a user context, it is read-only.
more info: https://github.com/reddit-archive/reddit/wiki/API#rules

In order to create an authorized Reddit instance, pieces of information are required for script applications (OAuth Configuration Options):

1. Client ID

2. Client secret

3. User agent

4. Your Reddit username, and

5. Your Reddit password (recommend upload txt file to protect your own password)

# Get Submissions in Subreddit:
**1. limit parameter**

Without **limit** parameter PRAW should yield as many results as it can with a single request. 

For most endpoints this results in 100 itmes per request. If you want to retrieve as many as possible pass in **limit=none**

Now that you have a Subreddit instance, you can iterate through some of its submissions, each bound to an instance of Submission. There are several sorts that you can iterate through:

*   controversial
*   gilded
*   hot
*   new
*   rising
*   top

Each of these methods will immediately return a ListingGenerator, which is to be iterated through.

***2. The replace_more method***

Each replacement requires one network request, and its response may yield additional **MoreComments** instances. As a result, by default, replace_more() only replaces at most 32 **MoreComments** instances – all other instances are simply removed. The maximum number of instances to replace can be configured via the ***limit*** parameter. Additionally a ***threshold*** parameter can be set to only perform replacement of **MoreComments** instances that represent a minimum number of comments; it defaults to 0, meaning all **MoreComments** instances will be replaced up to limit.

# Filter words with few occurrences
This block should run after scrape comments

filter the words with 10 occurrences

# Scrape comments
This block include:

*   After remove the few occurrences, we will get cleaned comment dataset
*   Add the <|comment|> tag into the datapoint (since csv document contain starting and end tags automatically)

# Title scrape: for further research
This block is for title scrape, whcih include more title cleaning, finally get csv document.

We can use this document to tech GPT-2 learn the structure of title, after fine-tuned, gerenate comments based on the gerenated titles.

This means we should scrape enough data from the Reddit like: three years comments and titles. Depend on the limitation of time and resources of GPU it need further research.

# Extra clean
Some extra clean for data cleaning include:


1.   remove stopwords
2.   spell correction

This block will take plenty of time.
