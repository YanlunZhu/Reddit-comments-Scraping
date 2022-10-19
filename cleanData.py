correct_comment = [] # list for cleaned comments
correct_title = [] # list for cleaned title
punctuations_list = ['.', ',', '!','?', ';'] # keep some necessary symbols

# # filter words with less than 10 occurrences
for comment in comment_list:
  word_in_text = word_tokenize(comment)
  for word in word_in_text:
    if word not in punctuations_list and word not in vocabs_list:
      word_in_text.remove(word)
  word_in_text.insert(0, '<|comment|>')
  # combine the filtered words to string and remove the additional spaces
  corrected_comment = ' '.join(str(correct_word) for correct_word in word_in_text)
  corrected_comment = re.sub(r'\s+([,:?.!"$;{}=~()%])', r'\1', corrected_comment)
  correct_comment.append(corrected_comment)

for title in title_list_comment:
  # we can also add tags to locate title strucuture, do not need to use at present
  # word_in_text_title = word_tokenize(title)
  # word_in_text_title.insert(0, '<|startoftitle|>')
  # word_in_text_title.append('<|endoftitle|>')
  # corrected_title = ' '.join(str(correct_title) for correct_title in word_in_text_title)
  # corrected_title = re.sub(r"[:]+", '', corrected_title)

  # remove the age in the brackets, reduce the noise
  corrected_title = re.sub(u"\\(.*?\\)", '', title) 
  # remvoe the 'update:' in the title
  # corrected_title = re.sub(r'update', '', corrected_title)
  # some normal clean same as clean in comments 
  corrected_title = re.sub(r'\s+', ' ', corrected_title)
  corrected_title = re.sub(r'\s+([,:?.!"$;{}=~()%])', r'\1', corrected_title)
  correct_title.append(corrected_title)