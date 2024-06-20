<br>
<a href="https://ultralytics.com" target="_blank"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# Tinder API Documentation (Updated 2018) 💘

A big thank you to [@rtt](https://gist.github.com/rtt/10403467#file-tinder-api-documentation-md) for their initial compilation of the Tinder API documentation. This document is meant to offer an updated guide for interacting with the Tinder API as of June 2018.

[![Ultralytics Actions](https://github.com/ultralytics/tinder/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/tinder/actions/workflows/format.yml) <a href="https://ultralytics.com/discord"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a>

Please note that this documentation may become outdated over time; always refer to the latest API specifications when developing applications.

## API Details

The following table summarizes the host and protocol details for the Tinder API.

| Detail   | Value            |
| -------- | ---------------- |
| Host     | api.gotinder.com |
| Protocol | SSL              |

## Required Headers

When making API calls, it's essential to include appropriate headers. Here are the headers that you'll need:

| Header       | Example                                       |
| ------------ | --------------------------------------------- |
| X-Auth-Token | See "How to get facebook_token" section below |
| Content-type | application/json                              |
| User-agent   | Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00) |

## Known Endpoints

All endpoints should be appended to the host URL, `https://api.gotinder.com`. Make sure to include the required headers with your requests. The only exception is the `/auth` endpoint, which should not be provided with the `X-Auth-Token` header.

The table below lists various endpoints with their purposes, expected data, and the HTTP method to use.

| Endpoint                                    | Purpose                                                | Data                                                       | Method |
| ------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------- | ------ |
| `/auth`                                     | For authenticating                                     | `{'facebook_token': <token>, 'facebook_id': <id>}`         | POST   |
| `/auth/login/accountkit`                    | For SMS authentication (two-factor)                    | `{'token': <token>, 'id': <id>, 'client_version':'9.0.1'}` | POST   |
| ...                                         | ...                                                    | ...                                                        | ...    |
| `/passport/user/travel`                     | (Tinder Plus Only) Travel to coordinate                | `{"lat": <latitude>, "lon": <longitude>}`                  | POST   |
| `/instagram/authorize`                      | Auth Instagram                                         | `{}`                                                       | GET    |
| ...                                         | ...                                                    | ...                                                        | ...    |
| `/v2/fast-match/preview`                    | Get the thumbnail image shown in the messages-window   | `{}`                                                       | GET    |
| `/giphy/trending?limit=<limit>`             | Get the trending GIFs (Tinder uses Giphy) in chat      | `{}`                                                       | GET    |
| `/giphy/search?limit=<limit>&query=<query>` | Get GIFs based on a search (Tinder uses Giphy) in chat | `{}`                                                       | GET    |

(For the full list of endpoints, please refer to the attached table in the original documentation.)

## Status Codes

Tinder API uses standard HTTP status codes to indicate the success or failure of an API request:

| Status Code | Explanation                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 200         | Everything went okay, and the server returned a result (if any).                                                                   |
| 301         | The server is redirecting you to a different endpoint. This can occur when a domain name changes or an endpoint's name is updated. |
| 400         | The server thinks you made a bad request. This happens when the request is missing information or is otherwise malformed.          |
| 401         | The server thinks you're not authenticated. This happens when incorrect credentials are provided.                                  |
| 404         | The server didn't find the resource you tried to access.                                                                           |

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
];
```

#### Friends' Pingtimes (Unavailable)

The `friends_pingtimes()` function used to return the time since each Facebook friend last used Tinder. However, Tinder's change to a constant `ping_time` has made this feature obsolete.

#### Facebook Friends (Unavailable)

This feature used to allow you to access profile information and ID of your Facebook friends on Tinder. With the ID, you could call `api.get_person(id)` to get more detailed information. This feature is no longer available.

# 🤝 Contribute

We welcome contributions from the community! Whether you're fixing bugs, adding new features, or improving documentation, your input is invaluable. Take a look at our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to get started. Also, we'd love to hear about your experience with Ultralytics products. Please consider filling out our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge 🙏 and thank you to all of our contributors!

<!-- Ultralytics contributors -->

<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

# ©️ License

Ultralytics is excited to offer two different licensing options to meet your needs:

- **AGPL-3.0 License**: Perfect for students and hobbyists, this [OSI-approved](https://opensource.org/licenses/) open-source license encourages collaborative learning and knowledge sharing. Please refer to the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for detailed terms.
- **Enterprise License**: Ideal for commercial use, this license allows for the integration of Ultralytics software and AI models into commercial products without the open-source requirements of AGPL-3.0. For use cases that involve commercial applications, please contact us via [Ultralytics Licensing](https://ultralytics.com/license).

# 📬 Contact Us

For bug reports, feature requests, and contributions, head to [GitHub Issues](https://github.com/ultralytics/velocity/issues). For questions and discussions about this project and other Ultralytics endeavors, join us on [Discord](https://ultralytics.com/discord)!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
