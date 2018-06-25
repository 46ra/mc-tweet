import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import utter
import twitter
import datetime

with open('tokens.txt') as f:
    tokens = f.read().strip().splitlines()

auth = twitter.OAuth(
    consumer_key=tokens[0],
    consumer_secret=tokens[1],
    token=tokens[2],
    token_secret=tokens[3]
    )

twitter = twitter.Twitter(auth=auth)

while True:
    try:
        status = utter.main()
        break
    except:
        continue

if len(status) > 140:
    status = status[:139] + "…"
twitter.statuses.update(status=status)
print(f"succeeded: {datetime.datetime.now()}")
