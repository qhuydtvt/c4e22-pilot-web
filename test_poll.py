from poll import Poll
from random import choice
import mlab

# 1. Connect to database
mlab.connect()

#2. Prepare data
q = "Hackathon ăn gì?"
opts = [
  "Pizza",
  "Bánh mỳ hội an",
  "Phở xào",
]

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
c = ""
for _ in range(6):
  c += choice(alphabet)

#3. Create document
p = Poll(question=q, options=opts, code=c)

#4. Save
p.save()
