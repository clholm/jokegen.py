# Connor Holm and Mick Brege 2017
# jokegen v2
import random
import tweepy

# universal vowel list. 
vowels = ["a", "e", "i", "o", "u"]

# TWITTER AUTH
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

# functions
# returns either "a" or "an" for specific noun
def determine_article(noun):
    article = "a"
    if noun[0] in vowels: 
        article = "an" 
    return article

# fetches a random word from the specified list
# by generating a random number 0 <= n <= 6884 and iterating
# that number of time
def fetch_word(type, iter_num):
    file_name = type + ".txt"
    word = ""
    if iter_num == -1:
        iter_num = random.randrange(0, 6884)
    i = 0
    with open (file_name) as fp: 
        for line in fp:
            if  i == iter_num: 
                split_line = line.split("\n")
                word = str(split_line[0]).lower()
                return word
            else: 
                i += 1
    # if iter_num was larger than the number of 
    # lines in the file, modify it and try again
    if word == "": 
        iter_num = iter_num % (i + 1)
        # tail recurse! 
        return fetch_word(type, iter_num)


# generates a joke
def gen_joke(): 
    # only generate jokes less that 140 chars
    while(True):
        # fetch random words
        adjective = fetch_word("adjectives", -1)
        noun = fetch_word("nouns", -1)
        animal_one = fetch_word("animals", -1)
        animal_two = fetch_word("animals", -1)
        location = fetch_word("locations", -1)
        greeting = fetch_word("greetings", -1)

        # determine articles! 
        article_one = determine_article(animal_one) 
        article_two = determine_article(location) 
        article_three = determine_article(animal_two) 

        # re-roll adjactive and noun if they're too long (fix later)
        joke = article_one + " " + animal_one  + " walks into " + article_two + " " + location + " and " + article_three + " " + animal_two + " says, \"" +  greeting + ", why the " + adjective + " " + noun + "?\""
        if len(joke) <= 140: 
            break
    return joke

# generate lists and then joke
joke = gen_joke()
# tweet joke 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(joke)