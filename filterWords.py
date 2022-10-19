def read_corpus(filename):
    with open(filename, encoding='utf8') as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words += re.findall(r'\w+', line.lower())

    return words

# total words in the text file
words = read_corpus("file name")
print(f"There are {len(words)} total words in the corpus")

# how many unique words in the text file
vocabs = set(words)
print(f"There are {len(vocabs)} unique words in the vocabulary")

# filter the words less than 10 occurrences
word_counts = Counter(words)
vocabs_list = []
for words in vocabs:    
  if word_counts[words] >= 10:
    vocabs_list.append(words)
print('The rest of vocabulary:', len(vocabs_list))

# calculate the average length of comments, remind to change the file name
# can be used after filtering
average_list = []
with open ('Raw comments.csv') as f:
  for line in f.readlines():
    average_list.append(len(line))

print(min(average_list), max(average_list), np.mean(average_list), np.median(average_list))