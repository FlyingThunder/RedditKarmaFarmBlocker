import praw
import time
import prawcore

client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)


with open("redditors.txt", "r") as x:
    y = x.readlines()
    for z in y:
        try:
            z = z.replace("\n","")
            print("user:" + f">{z}<")
            redditor = reddit.redditor(z)
            redditor.block()
        except prawcore.exceptions.BadRequest:
            print("Error 400 - ignore this")
