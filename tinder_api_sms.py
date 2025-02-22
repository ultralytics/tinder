# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

import json

import config
import requests

headers = {
    "app_version": "6.9.4",
    "platform": "ios",
    "content-type": "application/json",
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
    "X-Auth-Token": config.tinder_token,
}


def get_recommendations():
    """Returns a list of users that you can swipe on."""
    try:
        r = requests.get("https://api.gotinder.com/user/recs", headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong with getting recommendations:", e)


def get_updates(last_activity_date=""):
    """
    Returns all updates since the given activity date.

    The last activity date is defaulted at the beginning of time.
    Format for last_activity_date: "2017-07-09T10:28:13.392Z"
    """
    try:
        url = f"{config.host}/updates"
        r = requests.post(url, headers=headers, data=json.dumps({"last_activity_date": last_activity_date}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong with getting updates:", e)


def get_self():
    """Returns your own profile data."""
    try:
        url = f"{config.host}/profile"
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your data:", e)


def change_preferences(**kwargs):
    """
    ex: change_preferences(age_filter_min=30, gender=0)
    kwargs: a dictionary - whose keys become separate keyword arguments and the values become values of these arguments
    age_filter_min: 18..46
    age_filter_max: 22..55
    age_filter_min <= age_filter_max - 4
    gender: 0 == seeking males, 1 == seeking females
    distance_filter: 1..100
    discoverable: true | false
    {"photo_optimizer_enabled":false}.
    """
    try:
        url = f"{config.host}/profile"
        r = requests.post(url, headers=headers, data=json.dumps(kwargs))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not change your preferences:", e)


def get_meta():
    """
    Returns meta data on yourself.

    Including the following keys:
    ['globals', 'client_resources', 'versions', 'purchases',
    'status', 'groups', 'products', 'rating', 'tutorials',
    'travel', 'notifications', 'user']
    """
    try:
        url = f"{config.host}/meta"
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your metadata:", e)


def update_location(lat, lon):
    """
    Updates your location to the given float inputs
    Note: Requires a passport / Tinder Plus.
    """
    try:
        url = f"{config.host}/passport/user/travel"
        r = requests.post(url, headers=headers, data=json.dumps({"lat": lat, "lon": lon}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not update your location:", e)


def reset_real_location():
    """Resets the user's real location by sending a POST request to the server."""
    try:
        url = f"{config.host}/passport/user/reset"
        r = requests.post(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not update your location:", e)


def get_recs_v2():
    """This works more consistently then the normal get_recommendations because it seeems to check new location."""
    try:
        url = f"{config.host}/v2/recs/core?locale=en-US"
        r = requests.get(url, headers=headers)
        return r.json()
    except Exception:
        print("excepted")


def set_webprofileusername(username):
    """Sets the username for the webprofile: https://www.gotinder.com/@YOURUSERNAME."""
    try:
        url = f"{config.host}/profile/username"
        r = requests.put(url, headers=headers, data=json.dumps({"username": username}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not set webprofile username:", e)


def reset_webprofileusername(username):
    """Resets the username for the webprofile."""
    try:
        url = f"{config.host}/profile/username"
        r = requests.delete(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not delete webprofile username:", e)


def get_person(id):
    """Gets a user's profile via their id."""
    try:
        url = f"{config.host}/user/{id}"
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get that person:", e)


def send_msg(match_id, msg):
    """Sends a message to a user match specified by match_id."""
    try:
        url = f"{config.host}/user/matches/{match_id}"
        r = requests.post(url, headers=headers, data=json.dumps({"message": msg}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not send your message:", e)


def superlike(person_id):
    """Send a superlike to a user identified by person_id and return the server's JSON response."""
    try:
        url = f"{config.host}/like/{person_id}/super"
        r = requests.post(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not superlike:", e)


def like(person_id):
    """Send a GET request to like a user identified by person_id and return the server's JSON response."""
    try:
        url = f"{config.host}/like/{person_id}"
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not like:", e)


def dislike(person_id):
    """Send a 'dislike' request to the server for the provided person_id and return the server's JSON response."""
    try:
        url = f"{config.host}/pass/{person_id}"
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not dislike:", e)


def report(person_id, cause, explanation=""):
    """
    There are three options for cause:
        0 : Other and requires an explanation
        1 : Feels like spam and no explanation
        4 : Inappropriate Photos and no explanation.
    """
    try:
        url = f"{config.host}/report/{person_id}"
        r = requests.post(url, headers=headers, data={"cause": cause, "text": explanation})
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not report:", e)


def match_info(match_id):
    """Fetch and return match info from the server using the provided match ID."""
    try:
        url = f"{config.host}/matches/{match_id}"
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your match info:", e)


def all_matches():
    """Fetches all match data from the server."""
    try:
        url = f"{config.host}/v2/matches"
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get your match info:", e)


# def see_friends():
#     try:
#         url = config.host + '/group/friends'
#         r = requests.get(url, headers=headers)
#         return r.json()['results']
#     except requests.exceptions.RequestException as e:
#         print("Something went wrong. Could not get your Facebook friends:", e)
