def comment_clean(text):
      """
  clean the link, emojis, special characters, newlines
  """
  # remove html link in the comments
  pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
  text = pattern.sub('', text)
  # remove the emoji in the comments
  emoji = re.compile("["
                        u"\U0001F600-\U0001FFFF"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        "]+", flags=re.UNICODE)
  text = emoji.sub(r'', text)
  
  # remove special characters
  # The formatted text after removing not necessary punctuations.
  # In the above regex expression, I am providing necessary set of punctuations that are frequent in this particular dataset.
  text = re.sub(r"[^a-zA-Z0-9:$-,%.?!]+", ' ', text)
  
  # remove newlines and tabs
  text = re.sub(r'\n', '', text)
  text = re.sub(r'\t','', text)
  
  pattern = re.compile(r'\s+') 
  text = re.sub(pattern, ' ', text)

  # Pattern matching for all case alphabets
  Pattern_alpha = re.compile(r"([A-Za-z])\1{1,}", re.DOTALL)
  # Limiting all the  repeatation to two characters.
  text = Pattern_alpha.sub(r"\1\1", text) 
  
  # Pattern matching for all the punctuations that can occur
  Pattern_Punct = re.compile(r'([.,/#!$%^&*?;:{}=_`~()+-])\1{1,}')
  # Limiting punctuations in previously formatted string to only one.
  Combined_Formatted = Pattern_Punct.sub(r'\1', text)
  # The below statement is replacing repeatation of spaces that occur more than two times with that of one occurrence.
  text = re.sub(' {2,}',' ', Combined_Formatted)
  
  return text


# contraction map
CONTRACTION_MAP = {
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have",
}

def change_contraction(text, contraction_map=CONTRACTION_MAP):
  list_of_tokens = text.split(' ')
  for word in list_of_tokens: 
    # Check if the found word is in the dictionary "Contraction Map" as a key
    if word in CONTRACTION_MAP: 
      # If Word appears in both dictionary and list_of_tokens, replace Word with key value
      list_of_tokens = [item.replace(word, CONTRACTION_MAP[word]) for item in list_of_tokens]
                
  # Convert a list of tokens to a string
  comment = ' '.join(str(e) for e in list_of_tokens) 
  
  return comment