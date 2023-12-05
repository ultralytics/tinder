# Tinder API Documentation (Updated 2018) 💘

A big thank you to [@rtt](https://gist.github.com/rtt/10403467#file-tinder-api-documentation-md) for their initial compilation of the Tinder API documentation. This document is meant to offer an updated guide for interacting with the Tinder API as of June 2018.

Please note that this documentation may become outdated over time; always refer to the latest API specifications when developing applications.

## API Details

The following table summarizes the host and protocol details for the Tinder API.

| Detail   | Value               |
|----------|---------------------|
| Host     | api.gotinder.com    |
| Protocol | SSL                 |

## Required Headers

When making API calls, it's essential to include appropriate headers. Here are the headers that you'll need:

| Header         | Example                                                  |
|----------------|----------------------------------------------------------|
| X-Auth-Token   | See "How to get facebook_token" section below            |
| Content-type   | application/json                                         |
| User-agent     | Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)            |

## Known Endpoints

All endpoints should be appended to the host URL, `https://api.gotinder.com`. Make sure to include the required headers with your requests. The only exception is the `/auth` endpoint, which should not be provided with the `X-Auth-Token` header.

The table below lists various endpoints with their purposes, expected data, and the HTTP method to use.

| Endpoint                                 | Purpose                                                  | Data                                                                            | Method |
|------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------|--------|
| `/auth`                                  | For authenticating                                       | `{'facebook_token': <token>, 'facebook_id': <id>}`                              | POST   |
| `/auth/login/accountkit`                 | For SMS authentication (two-factor)                      | `{'token': <token>, 'id': <id>, 'client_version':'9.0.1'}`                     | POST   |
| ...                                      | ...                                                      | ...                                                                             | ...    |
| `/passport/user/travel`                  | (Tinder Plus Only) Travel to coordinate                  | `{"lat": <latitude>, "lon": <longitude>}`                                      | POST   |
| `/instagram/authorize`                   | Auth Instagram                                           | `{}`                                                                            | GET    |
| ...                                      | ...                                                      | ...                                                                             | ...    |
| `/v2/fast-match/preview`                 | Get the thumbnail image shown in the messages-window     | `{}`                                                                            | GET    |
| `/giphy/trending?limit=<limit>`          | Get the trending GIFs (Tinder uses Giphy) in chat        | `{}`                                                                            | GET    |
| `/giphy/search?limit=<limit>&query=<query>` | Get GIFs based on a search (Tinder uses Giphy) in chat | `{}`                                                                            | GET    |

(For the full list of endpoints, please refer to the attached table in the original documentation.)

## Status Codes

Tinder API uses standard HTTP status codes to indicate the success or failure of an API request:

| Status Code | Explanation                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 200         | Everything went okay, and the server returned a result (if any).                                                                             |
| 301         | The server is redirecting you to a different endpoint. This can occur when a domain name changes or an endpoint's name is updated.            |
| 400         | The server thinks you made a bad request. This happens when the request is missing information or is otherwise malformed.                     |
| 401         | The server thinks you're not authenticated. This happens when incorrect credentials are provided.                                             |
| 404         | The server didn't find the resource you tried to access.                                                                                     |

## Config File

### Facebook Access Token and User ID

To authenticate using your Facebook account, include your Facebook username and password in the config file. The `fb_auth_token.py` module will programmatically retrieve your `facebook_access_token` and `fb_user_id`, which are then used to generate a `tinder_auth_token` via `tinder_api.py`, granting you access to your Tinder data. Happy swiping! 🎉

### SMS Authentication

SMS authentication is straightforward. Run `phone_auth_token.py` and input your phone number when prompted. Enter the code you receive via SMS to retrieve your token. Keep in mind that there is a rate limit for the number of SMS you can receive in an hour. It's advised to use your token within its lifetime (24 hours) instead of requesting a new one each time.

To proceed, add your token to `tinder_config_ex.py` as the value for `tinder_token`. You're now prepared to start using the API!

## Key Features

#### Match Info 📊

This feature creates a local dictionary for each of your matches containing keys like message count, age, name, photos, and more. For example:

```javascript
{
  '123456': {
    // Detailed info about the match would go here.
  },
  // More matches would follow.
}
```

#### Sorting 🔍

Sort your matches by attributes such as "age", "message_count", and "gender". Here's a sample structure:

```javascript
[
  // Tuple with match ID and corresponding match info.
]
```

#### Friends' Pingtimes (Unavailable)

The `friends_pingtimes()` function used to return the time since each Facebook friend last used Tinder. However, Tinder's change to a constant `ping_time` has made this feature obsolete.

#### Facebook Friends (Unavailable)

This feature used to allow you to access profile information and ID of your Facebook friends on Tinder. With the ID, you could call `api.get_person(id)` to get more detailed information. This feature is no longer available.

## Note on Licensing

All Ultralytics repositories are under the AGPL-3.0 license. Ensure any code or documentation you use or reference is compliant with this license.

Please reference the original documentation for a more in-depth understanding of Tinder's API. The aim of this document is to provide clarity and updates where necessary, without altering the core information provided.

Happy Developing! 🚀
