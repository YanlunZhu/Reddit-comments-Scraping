# read-only reddit instances
# assume you have a praw. Reddit instance bound to variable 'reddit'
# obtain submission instance from a subreddit
subreddit = reddit.subreddit('subreddit''s name').top('all', limit=100)

title_list = []
title_list_comment = [] # every comment's title
comment_list = [] # every comments

# get the submission's ID which comes after comments/ in the URL
# reference is the submission's ID during the all time top submissiom
for reference in subreddit:
  # print(submission.title)
  # we can scrape the body of the top-level comments in the thread
  submission = reddit.submission(reference)
  # 'threshold' parameter can be set to only perform replacement of MoreComment
  # instance that represent a minimum number of comments
  submission.comments.replace_more(threshold=10, limit=None)
  # collect the submission title
  # title_list.append(submission.title)

  for top_level_comment in submission.comments:
    # remove the length of comment less than 30 words
    if len(word_tokenize(top_level_comment.body)) > 30 and len(word_tokenize(top_level_comment.body)) <= 1000:
      # convert uppercase letters to lowercase letters
      title_clean = submission.title.lower()
      title_clean = unidecode.unidecode(title_clean)
      title_clean = comment_clean(title_clean)
      title_clean = change_contraction(title_clean, contraction_map=CONTRACTION_MAP)

      # Remove accented characters from text using unidecode
      # data clean, more detail in each function
      top_level_comment_clean = top_level_comment.body.lower()
      top_level_comment_clean = unidecode.unidecode(top_level_comment_clean)
      top_level_comment_clean = comment_clean(top_level_comment_clean)
      top_level_comment_clean = change_contraction(top_level_comment_clean, contraction_map=CONTRACTION_MAP)
      # top_level_comment_clean = remove_stopwords(top_level_comment_clean)
      
      comment_list.append(top_level_comment_clean)
      # comment_author.append(top_level_comment.author)
      title_list_comment.append(title_clean)

# convert list to dataframe by pandas