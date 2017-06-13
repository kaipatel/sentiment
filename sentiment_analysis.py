import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time
import numpy as np


fig = plt.figure("Sentiment Analysis")
ax1 = fig.add_subplot(1, 1, 1, axisbg='#232323')
fig.patch.set_facecolor('#232323')
ax1.tick_params(colors='w')
ax1.spines['bottom'].set_color('w')
ax1.spines['left'].set_color('w')

track = str(input("Please enter the name (excluding extension) of the .json file: "))
track_file = track +'.json'

fig.suptitle("Sentiment Analysis of: " + track, fontsize = 20, fontweight='bold', color='w')

yar = []
total = []
created = []
sid = SentimentIntensityAnalyzer()
#ss = sid.polarity_scores(sentence)


def animate(i):

  compound_total = 0

  with open(track_file, 'r') as f:

    line = f.readline()
    for line in f:
      tweet = json.loads(line)
      #print(sid.polarity_scores(tweet['text']))
      try:
        total.append(sid.polarity_scores(tweet['text'])['compound'])
        created_at = tweet['created_at']
        tweet_time = time.mktime(time.strptime(created_at,"%a %b %d %H:%M:%S +0000 %Y"))
      except:
        pass


  created.append(tweet_time)


  for each in total:
    compound_total += each

  yar.append(compound_total)

  print (yar[len(yar)-1], ", ", created[len(created)-1])
  #print(len(yar), " ", len(created))
  ax1.clear()
  ax1.plot(created, yar, color='r', linestyle='--', label="Live Data")
  plt.plot(np.unique(created), np.poly1d(np.polyfit(created, yar, 25))(np.unique(created)), color='#42f442', linewidth='2.0', label="General Trend")
  plt.grid(color='w')
  plt.legend()

ani = animation.FuncAnimation(fig, animate, interval=1000/401)
plt.show()
