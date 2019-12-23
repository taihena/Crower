import json
import Crower

# queuing_tweets = [{"text": "sample texts", "photo": 1},
                 # {"text": "sample texts2", "photo": 2}]  # TODO: replace placeholder for images


def write_to_queue(queuing_tweets):
    with open("queue.json", "w") as write_file:
        json.dump(queuing_tweets, write_file)


def read_from_queue():
    with open("queue.json", "r") as read_file:
        return json.load(read_file)


def update_queue():
    queued_tweets = read_from_queue()
    next_tweet = queued_tweets[0].get("text")

    write_to_queue(queued_tweets[1:])
    Crower.publish(next_tweet) # TODO: move publish to Crower.py


update_queue() # TODO: here for testing