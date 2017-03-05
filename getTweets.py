from sys import argv
import time


from api import getAPI


RequestDelay = 5
RequestMax = 5



def main():
    try:
        arg1 = argv[1]
        api = getAPI()
        tweetResults = []

        tweetindex = api.user_timeline(screen_name=arg1, count=1)[0].id
        time.sleep(RequestDelay)
        for requests in range(RequestMax):
            tweets = api.user_timeline(screen_name=arg1, include_retweets=False,
                    max_id=tweetindex)
            for tweet in tweets:
                tweetResults.append(tweet.text)
                tweetindex = tweet.id
            time.sleep(RequestDelay)

        print(tweetResults)
        print(len(tweetResults))


    except IndexError:
        print("Missing Twitter Handle")
    except Exception as e:
        print("program failure. Error: {}".format(e))

if __name__=='__main__':
    main()





