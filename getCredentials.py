# access to google cloud
from google.colab import drive
drive.mount('/content/drive')

# run this code after you upload yoour own password text
with open('/content/drive/MyDrive/pw.txt', 'r', encoding='cp1252') as f:
  pw = f.read()

# Log In to App: 
reddit = praw.Reddit(client_id='get from first register', 
            client_secret='get from first register', 
            user_agent='define a name',
            username='your Reddit''s name',
            password=pw,
            check_for_async=False)