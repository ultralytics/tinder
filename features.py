# coding=utf-8

import random
from datetime import date, datetime
from time import sleep

import config
import tinder_api as api
from tqdm import tqdm

"""
This file collects important data on your matches,
allows you to sort them by last_activity_date, age,
gender, message count, and their average successRate.
"""


def get_match_info():
    matches = api.get_updates()["matches"]
    now = datetime.utcnow()
    match_info = {}
    n = len(matches)
    print("\nDownloading match info...", end="")
    for i, match in enumerate(matches[:n]):
        try:
            person = match["person"]
            if "bio" not in person:
                person["bio"] = ""

            match_info[i] = {
                "name": person["name"],
                "person_id": person["_id"],  # This ID for looking up person
                "match_id": match["id"],  # This ID for messaging
                "message_count": match["message_count"],
                "photos": get_photos(person),
                "bio": person["bio"],
                "gender": person["gender"],
                "avg_successRate": get_avg_successRate(person),
                "messages": match["messages"],
                "age": calculate_age(match["person"]["birth_date"]),
                "distance": 0,  # api.get_person(person_id)['results']['distance_mi'], # very slow
                "last_activity_date": match["last_activity_date"],
            }
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            # continue
    print(" %g matches... Done." % n)
    return match_info


def get_match_id_by_name(name):
    """Returns a list_of_ids that have the same name as your input."""
    global match_info
    list_of_ids = [match_info[match]["match_id"] for match in match_info if match_info[match]["name"] == name]
    if list_of_ids:
        return list_of_ids
    return {"error": f"No matches by name of {name}"}


def get_photos(person):
    """Returns a list of photo urls."""
    photos = person["photos"]
    return [photo["url"] for photo in photos]


def calculate_age(birthday_string):
    """Converts from '1997-03-25T22:49:41.151Z' to an integer (age)"""
    birthyear = int(birthday_string[:4])
    birthmonth = int(birthday_string[5:7])
    birthday = int(birthday_string[8:10])
    today = date.today()
    return today.year - birthyear - ((today.month, today.day) < (birthmonth, birthday))


def get_avg_successRate(person):
    """SuccessRate is determined by Tinder for their 'Smart Photos' feature."""
    photos = person["photos"]
    curr_avg = 0
    for photo in photos:
        try:
            photo_successRate = photo["successRate"]
            curr_avg += photo_successRate
        except Exception:
            return -1
    return curr_avg / len(photos)


def sort_by_value(sortType):
    """
    Sort options are:
        'age', 'message_count', 'gender'
    """
    global match_info
    return sorted(match_info.items(), key=lambda x: x[1][sortType], reverse=True)


def see_friends_profiles(name=None):
    friends = api.see_friends()
    if name is None:
        return friends
    name = name.title()  # upcases first character of each word
    result_dict = {friend["name"]: friend for friend in friends if name in friend["name"]}
    return result_dict or "No friends by that name"


def convert_from_datetime(difference):
    secs = difference.seconds
    days = difference.days
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d days, %d hrs %02d min %02d sec" % (days, h, m, s)


def get_last_activity_date(now, ping_time):
    ping_time = ping_time[: len(ping_time) - 5]
    datetime_ping = datetime.strptime(ping_time, "%Y-%m-%dT%H:%M:%S")
    difference = now - datetime_ping
    return convert_from_datetime(difference)


def how_long_has_it_been():
    global match_info
    now = datetime.utcnow()
    times = {}
    for person in match_info:
        name = match_info[person]["name"]
        ping_time = match_info[person]["last_activity_date"]
        since = get_last_activity_date(now, ping_time)
        times[name] = since
        print(name, "----->", since)
    return times


def pause():
    """
    In order to appear as a real Tinder user using the app...

    When making many API calls, it is important to pause a...
    realistic amount of time between actions to not make Tinder...
    suspicious!
    """
    nap_length = 3 * random.random()
    print("Napping for %f seconds..." % nap_length)
    sleep(nap_length)


if __name__ == "__main__":
    if api.authverif() == True:
        print("Gathering Data on your matches...")
        match_info = get_match_info()
    else:
        print("Something went wrong. You were not authorized.")
