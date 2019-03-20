'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]

We will continue to work with this data throughout the week, so make sure to complete it!

https://api.slack.com/methods/conversations.open

'''
import json
import os

from pprint import pprint
import secrets
from slackclient import SlackClient


#slack_token = os.environ.get("SLACK_LEGACY_TK")
#slack_token = os.environ["SLACK_LEGACY_TK"]

slack_token = secrets.sl_secrets_tk
sc = SlackClient(slack_token)

r = sc.api_call(
    "channels.history",
    channel = "CGUDWETHR",
    count = "100"
)

# r = sc.api_call(
#     "chat.postMessage",
#     channel = "CGKALBXC6",
#     text = "did it work?",
#     username = "Testing",
#     as_user = "false"
#
# )
#pprint(r)

messages = r["messages"]


list_=[]
count = 0
for i in messages:
    if i["text"].startswith("<http"):
        #print(messages[count]["text"])
        dict_link = messages[count]["text"]
        try:
            #print(messages[count]["attachments"][0]["title"])
            dict_desc = messages[count]["attachments"][0]["title"]
        except KeyError as ke:
            #print("")
            dict_desc = ""
        #print(messages[count]["ts"])
        dict_ts = messages[count]["ts"]
        list_.append({"link":dict_link,"description":dict_desc,"date_added":dict_ts, "read":False,"rating":0, "comments":["a list of strings", "with comments"], "starrred":False})

    count += 1

pprint(list_)

with open('mydata.json', 'w') as outfile:
    # json.dump(list_, outfile)
    json_string = json.dumps(list_)
    outfile.write(json_string)
