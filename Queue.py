import json
import Crower

queuing_tweets = [{"text": "sample texts", "photo": 1},
                  {"text": "sample texts2", "photo": 2}]  # TODO: replace placeholder for images


def write_to_queue():
    with open("queue.json", "w") as write_file:
        json.dump(queuing_tweets, write_file)


write_to_queue()


def read_from_queue():
    with open("queue.json", "r") as read_file:
        return json.load(read_file)


queued_tweets = read_from_queue()

next_tweet = queued_tweets[0].get("text")

queuing_tweets = queued_tweets[1:]

write_to_queue()

Crower.publish(next_tweet)
