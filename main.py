#Made by Ja'Crispy
import tweepy
import requests
import time
import inspirobot

print("----------------------------------------------------------------------------")
print("Starting...")
print("----------------------------------------------------------------------------")


auth = tweepy.OAuthHandler("yourkeyhere", "yourkeysecerethere")
auth.set_access_token("youraccesskeyhere", "youraccesskeysecerethere")
api = tweepy.API(auth)

timeelapsed = 0
tweetcount = 0

while True:
  timeelapsed += 3
  

  response = requests.get(inspirobot.generate())
  
  file = open("quote.png", "wb")
  file.write(response.content)
  file.close()
  
  print()
  media = api.media_upload("quote.png")

  
  if tweetcount == 0:
    timeelapsed = 0
  tweetcount += 1
  
  tweet = "#Memes #meme #satire #motivation #motivationalquote #inspiration #inspirationalquote"
  
  post_result = api.update_status(status=tweet,media_ids=[media.media_id])

  print(f"Time Since Start: {timeelapsed} minutes          Tweet Num: {tweetcount}")
  
  time.sleep(180) #3 minutes = 180, 5 minutes = 300, 10 minutes = 600, 1 hour = 3600
