import os
import requests

try:
    BEARER_TOKEN = os.environ["TWITTER_BEARER_TOKEN"]
except KeyError:
    raise Exception(
        "If you're an instructor, you probably need to go to the GitHub repo and grab the file at lectures/apis/apis-demo/_secrets.sh"
    )

AUTH_HEADER = {"Authorization": f"Bearer {BEARER_TOKEN}"}
TWITTER_API = "https://api.twitter.com/2"

payload = {
    "query": "python open source",
    "max_results": 10,
    "tweet.fields": "text",
}

res = requests.get(
    f"{TWITTER_API}/tweets/search/recent", params=payload, headers=AUTH_HEADER
)

search_results = res.json()

print(search_results)