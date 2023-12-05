# Tinder API Documentation (Updated 2018) 📱

Hello Tinder API enthusiasts! Big thanks to [@rtt](https://gist.github.com/rtt/10403467#file-tinder-api-documentation-md) for the initial documentation. This guide provides a refreshed overview of Tinder's API as of June 2018. Let's dive in!

## API Details

Host: api.gotinder.com
Protocol: SSL

## Required Headers 📝

| Header          | Example                                   |
| ----------------| ------------------------------------------|
| X-Auth-Token    | See "How to get facebook_token" below     |
| Content-type    | application/json                          |
| User-agent      | Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00) |

## Known Endpoints 🌐

- Note: Append endpoints to the host URL.
- Note: Send curls with the specified headers. `/auth` is the exception (does not require X-Auth-Token).

| Endpoint                      | Purpose                                     | Data                                                | Method |
| ----------------------------- | ------------------------------------------- | --------------------------------------------------- | ------ |
| `/auth`                       | For authenticating                          | {'facebook_token': YOUR_TOKEN, 'facebook_id': YOUR_ID} | POST   |
| ...                           | ...                                         | ...                                                 | ...    |
| `/like/_id/super`             | ~Super Like~ someone                        | {}                                                  | POST   |
| `/v2/fast-match/preview`      | Get matches thumbnail image                 | {}                                                  | GET    |
| ...                           | ...                                         | ...                                                 | ...    |

For a complete list of endpoints, please refer to the original documentation above.

## Status Codes 💡

| Status Code | Explanation                                                                 |
| ------------| --------------------------------------------------------------------------- |
| 200         | OK: The server returned a result, if any.                                  |
| 301         | Moved Permanently: Redirecting to a different endpoint.                    |
| 400         | Bad Request: API requirements not met (e.g., missing information).         |
| 401         | Unauthorized: Wrong or missing credentials for API access.                 |
| 404         | Not Found: The requested resource could not be found.                      |

## Config File Setup 🔧

### Facebook Access Token and User ID

Add your Facebook credentials to your config file. `fb_auth_token.py` will retrieve your `facebook_access_token` and `fb_user_id`. These are imperative for generating your `tinder_auth_token`, which provides access to your Tinder account.

### SMS Authentication

SMS authentication is simple. Run `phone_auth_token.py`, enter your phone number, then provide the code received via SMS. Due to SMS rate limits, it's best to use your token (valid for 24 hours) rather than request a new one each time. Update `tinder_config_ex.py` with your token.

Programmatic retrieval of the `facebook_token` is now possible with the tools provided by [philliperemy](https://github.com/philipperemy/Deep-Learning-Tinder/blob/master/tinder_token.py) and [gloriamacia](https://github.com/gloriamacia). They've also added a Jupyter notebook to simplify the process further.

## Key Features 📊

### Match Info:

Creates a local dictionary per match with details like messages, age, photos, message count, and more.

```javascript
{
  "123456": {
    ...
  },
  "56789": {
    ...
  }
}
```

### Sorting:

Sort your matches by attributes such as "age", "message_count", and "gender".

```javascript
[
  ("123456789123456789", {
    ...
  })
]
```

## Deprecated Features ⚠️

**Note**: Certain features, such as sorting by `ping_time`, are no longer available due to changes by Tinder.

## Further Details

To get additional information not covered here, please check the tables and code snippets in the original documentation provided above.

Happy swiping, and may your API calls be ever in your favor! 🚀
