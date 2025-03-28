<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# Tinder API Documentation (Updated 2018) 💘

A big thank you to [@rtt](https://gist.github.com/rtt/10403467#file-tinder-api-documentation-md) for their initial compilation of the Tinder API documentation. This document is meant to offer an updated guide for interacting with the Tinder API as of June 2018. While this guide provides a snapshot from that time, remember that APIs evolve. For current development, always consult the latest official [API documentation](https://developer.match.com/) if available, or use network inspection tools to understand current endpoints.

[![Ultralytics Actions](https://github.com/ultralytics/tinder/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/tinder/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

Please note that this documentation may become outdated over time; always refer to the latest API specifications when developing applications. Understanding how APIs work is crucial for integrating services, a concept often applied in [Machine Learning Operations (MLOps)](https://www.ultralytics.com/glossary/machine-learning-operations-mlops).

## 🌐 API Details

The following table summarizes the host and protocol details for the Tinder API as of 2018.

| Detail   | Value            |
| -------- | ---------------- |
| Host     | api.gotinder.com |
| Protocol | SSL              |

## 🔑 Required Headers

When making API calls, it's essential to include appropriate headers. These headers authenticate your request and specify the content format. Here are the headers that were needed:

| Header       | Example                                       | Notes                                                                                                                                                                                        |
| ------------ | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Auth-Token | See "How to get facebook_token" section below | This token authenticates the user session. Obtaining authentication tokens is a standard practice in API security.                                                                           |
| Content-type | application/json                              | Indicates the request body format is [JSON](https://www.ultralytics.com/glossary/json).                                                                                                      |
| User-agent   | Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00) | Identifies the client application making the request. User-agent strings can vary and might affect API responses. For robust applications, consider managing user-agent strings dynamically. |

## 📍 Known Endpoints

All endpoints should be appended to the host URL, `https://api.gotinder.com`. Make sure to include the required headers with your requests. The only exception is the `/auth` endpoint, which should not be provided with the `X-Auth-Token` header during the initial authentication step.

The table below lists various endpoints identified in 2018, detailing their purposes, expected data payloads (often in JSON format), and the [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) to use.

| Endpoint                                    | Purpose                                                     | Data                                                       | Method   |
| ------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- | -------- |
| `/auth`                                     | Authenticate using Facebook credentials                     | `{'facebook_token': <token>, 'facebook_id': <id>}`         | POST     |
| `/auth/login/accountkit`                    | Authenticate using SMS (Account Kit, likely deprecated)     | `{'token': <token>, 'id': <id>, 'client_version':'9.0.1'}` | POST     |
| `/profile`                                  | Get/Set user profile information                            | Varies (GET for retrieval, POST/PUT for updates)           | GET/POST |
| `/user/recs`                                | Get recommendations (potential matches)                     | `{}`                                                       | GET      |
| `/like/<user_id>`                           | Like a user                                                 | `{}`                                                       | GET      |
| `/pass/<user_id>`                           | Pass (dislike) a user                                       | `{}`                                                       | GET      |
| `/v2/matches`                               | Get list of matches                                         | Optional query parameters for pagination                   | GET      |
| `/user/matches/<match_id>`                  | Get messages with a specific match                          | Optional query parameters for pagination                   | GET      |
| `/user/matches/<match_id>`                  | Send a message to a match                                   | `{'message': <message_text>}`                              | POST     |
| `/updates`                                  | Get updates (new matches, messages)                         | `{'last_activity_date': <iso_timestamp>}`                  | POST     |
| `/passport/user/travel`                     | (Tinder Plus Only) Set virtual location                     | `{"lat": <latitude>, "lon": <longitude>}`                  | POST     |
| `/instagram/authorize`                      | Authorize Instagram connection                              | `{}`                                                       | GET      |
| `/v2/profile/spotify/authorize`             | Authorize Spotify connection                                | `{}`                                                       | GET      |
| `/v2/fast-match/preview`                    | Get thumbnail for "Likes You" feature (Gold feature)        | `{}`                                                       | GET      |
| `/giphy/trending?limit=<limit>`             | Get trending GIFs from [Giphy](https://giphy.com/) for chat | `{}`                                                       | GET      |
| `/giphy/search?limit=<limit>&query=<query>` | Search GIFs from Giphy for chat                             | `{}`                                                       | GET      |

_(Note: This list is based on 2018 information and may not be exhaustive or currently accurate. API endpoints change frequently.)_

## 🚦 Status Codes

The Tinder API uses standard [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to indicate the success or failure of an API request:

| Status Code | Explanation প্রিয় साथियों the<start*of_audio> প্রিয় of World Vision International Nepal (1_000_000), World Food Programme (WFP) (1_000* <y*bin_867>-1 is-1\_\_ the<start_of_audio>কাতার the<start_of_audio>\_T-1* is not None:
if not isinstance(
value_1, str
):
raise TypeError(
f"Expected property 'value' of type str but received {type(value_t_1)} instead"
)
value = value_t_1
else:
value = value_t_1
break
else:
raise ValueError(
"No valid value found for union type 'value'"
)
else:
value = None

                return cls(
                    value=value,
                )

            value_t_2 = value_t.get("value")
            if value_t_2 is not None:
                if not isinstance(
                    value_t_2,
                    str
                ):
                    raise TypeError(
                        f"expected value to be str but received {type(value_t_2)} instead"
                    )
                value = value_t_2
            else:
                value = None

            return cls(
                value=value,
            )

        value_t_3 = value.get("value")
        if value_t_3 is not None:
            if not isinstance(
                value_
            ):
                raise TypeError(
                    f"expected value to be str but received {type(value_t_3)} instead"
                )
            value = value_t_3
        else:
            value = None

        return cls(
            value=value,
        )

    def __init__(
        self,
        value: str,
    ):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.value == other
        elif isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False

    def __ne__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.value != other
        elif isinstance(other, self.__class__):
            return self.value != other.value
        else:
            return True

    def __lt__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.value < other
        elif isinstance(other, self.__class__):
            return self.value < other.value
        else:
            raise TypeError(f"unsupported operand type(s) for <: '{type(self)}' and '{type(other)}'")

    def __le__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.value <= other
        elif isinstance(other, self.__class__):
            return self.value <= other.value
        else:
            raise TypeError(f"unsupported operand type(s) for <=: '{type(self)}' and '{type(other)}'")

    def __gt__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.value > other
        elif isinstance(other, self.__class__):
            return self.value > other.value
        else:
            raise TypeError(f"unsupported operand type(s) for >: '{type(self)}' and '{type(other)}'")

    def __ge__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.value >= other
        elif isinstance(other, self.__class__):
            return self.value >= other.value
        else:
            raise TypeError(f"unsupported operand type(s) for >=: '{type(self)}' and '{type(other)}'")

    def __len__(self) -> int:
        return len(self.value)

    def __contains__(self, item: str) -> bool:
        return item in self.value

    def __getitem__(self, key: int) -> str:
        return self.value[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self.value)

    def __reversed__(self) -> Iterator[str]:
        return reversed(self.value)

    def __add__(self, other: str) -> str:
        return self.value + other

    def __radd__(self, other: str) -> str:
        return other + self.value

    def __mul__(self, n: int) -> str:
        return self.value * n

    def __rmul__(self, n: int) -> str:
        return n * self.value

    def capitalize(self) -> str:
        return self.value.capitalize()

    def casefold(self) -> str:
        return self.value.casefold()

    def center(self, width: int, fillchar: str = ' ') -> str:
        return self.value.center(width, fillchar)

    def count(self, sub: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
        return self.value.count(sub, start, end)

    def encode(self, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
        return self.value.encode(encoding, errors)

    def endswith(self, suffix: Union[str, Tuple[str, ...]], start: Optional[int] = None, end: Optional[int] = None) -> bool:
        return self.value.endswith(suffix, start, end)

    def expandtabs(self, tabsize: int = 8) -> str:
        return self.value.expandtabs(tabsize)

    def find(self, sub: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
        return self.value.find(sub, start, end)

    def format(self, *args, **kwargs) -> str:
        return self.value.format(*args, **kwargs)

    def format_map(self, mapping: Mapping[str, Any]) -> str:
        return self.value.format_map(mapping)

    def index(self, sub: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
        return self.value.index(sub, start, end)

    def isalnum(self) -> bool:
        return self.value.isalnum()

    def isalpha(self) -> bool:
        return self.value.isalpha()

    def isascii(self) -> bool:
        return self.value.isascii()

    def isdecimal(self) -> bool:
        return self.value.isdecimal()

    def isdigit(self) -> bool:
        return self.value.isdigit()

    def isidentifier(self) -> bool:
        return self.value.isidentifier()

    def islower(self) -> bool:
        return self.value.islower()

    def isnumeric(self) -> bool:
        return self.value.isnumeric()

    def isprintable(self) -> bool:
        return self.value.isprintable()

    def isspace(self) -> bool:
        return self.value.isspace()

    def istitle(self) -> bool:
        return self.value.istitle()

    def isupper(self) -> bool:
        return self.value.isupper()

    def join(self, iterable: Iterable[str]) -> str:
        return self.value.join(iterable)

    def ljust(self, width: int, fillchar: str = ' ') -> str:
        return self.value.ljust(width, fillchar)

    def lower(self) -> str:
        return self.value.lower()

    def lstrip(self, chars: Optional[str] = None) -> str:
        return self.value.lstrip(chars)

    def maketrans(self, x: Union[Dict[int, Union[int, str, None]], str], y: Optional[str] = None, z: Optional[str] = None) -> Dict[int, Union[int, str, None]]:
        return str.maketrans(x, y, z)

    def partition(self, sep: str) -> Tuple[str, str, str]:
        return self.value.partition(sep)

    def removeprefix(self, prefix: str) -> str:
        return self.value.removeprefix(prefix)

    def removesuffix(self, suffix: str) -> str:
        return self.value.removesuffix(suffix)

    def replace(self, old: str, new: str, count: int = -1) -> str:
        return self.value.replace(old, new, count)

    def rfind(self, sub: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
        return self.value.rfind(sub, start, end)

    def rindex(self, sub: str, start: Optional[int] = None, end: Optional[int] = None) -> int:
        return self.value.rindex(sub, start, end)

    def rjust(self, width: int, fillchar: str = ' ') -> str:
        return self.value.rjust(width, fillchar)

    def rpartition(self, sep: str) -> Tuple[str, str, str]:
        return self.value.rpartition(sep)

    def rsplit(self, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
        return self.value.rsplit(sep, maxsplit)

    def rstrip(self, chars: Optional[str] = None) -> str:
        return self.value.rstrip(chars)

    def split(self, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
        return self.value.split(sep, maxsplit)

    def splitlines(self, keepends: bool = False) -> List[str]:
        return self.value.splitlines(keepends)

    def startswith(self, prefix: Union[str, Tuple[str, ...]], start: Optional[int] = None, end: Optional[int] = None) -> bool:
        return self.value.startswith(prefix, start, end)

    def strip(self, chars: Optional[str] = None) -> str:
        return self.value.strip(chars)

    def swapcase(self) -> str:
        return self.value.swapcase()

    def title(self) -> str:
        return self.value.title()

    def translate(self, table: Dict[int, Union[int, str, None]]) -> str:
        return self.value.translate(table)

    def upper(self) -> str:
        return self.value.upper()

    def zfill(self, width: int) -> str:
        return self.value.zfill(width)

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the object.

        This method converts the object's attributes into a dictionary format.
        It iterates through the object's __dict__ and converts any attribute that is an instance
        of a class defined in the `models` module to its dictionary representation using its `to_dict` method.

        Returns:
            Dict[str, Any]: A dictionary representation of the object.
        """
        return self.value

    def to_json(self) -> str:
        """
        Returns a JSON representation of the object.

        This method converts the object's attributes into a JSON string.
        It uses the `to_dict` method to get a dictionary representation and then uses `json.dumps`
        to convert the dictionary into a JSON string.

        Returns:
            str: A JSON representation of the object.
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "String":
        """
        Creates an instance of the class from a dictionary.

        This method takes a dictionary and returns an instance of the class
        initialized with the values from the dictionary.

        Args:
            data (Dict[str, Any]): A dictionary containing the attribute values.

        Returns:
            String: An instance of the class.

        Raises:
            TypeError: If the provided data is not a dictionary.
        """
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict type for data, but got {type(data)}")

        # Extract the 'value' field from the dictionary
        value = data.get("value")

        # Validate that 'value' is a string
        if not isinstance(value, str):
            raise TypeError(f"Expected 'value' to be a string, but got {type(value)}")

        # Create and return an instance of the class
        return cls(value=value)

    @classmethod
    def from_json(cls, data: str) -> "String":
        """
        Creates an instance of the class from a JSON string.

        This method takes a JSON string, parses it into a dictionary, and then
        uses `from_dict` to create an instance of the class.

        Args:
            data (str): A JSON string representing the object.

        Returns:
            String: An instance of the class.

        Raises:
            TypeError: If the provided data is not a string.
            json.JSONDecodeError: If the string is not valid JSON.
        """
        if not isinstance(data, str):
            raise TypeError(f"Expected str type for data, but got {type(data)}")

        try:
            json_data = json.loads(data)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Failed to decode JSON: {e.msg}", e.doc, e.pos)

        return cls.from_dict(json_data)

    def __deepcopy__(self, memo):
        """Create a deep copy of the object."""
        # Assuming `value` is an immutable type like str, int, float, bool, tuple
        # A shallow copy is sufficient for immutable types.
        # If `value` could be a mutable type (like list, dict), a deep copy mechanism would be needed here.
        new_value = copy.deepcopy(self.value, memo)
        return self.__class__(value=new_value)

    def __copy__(self):
        """Create a shallow copy of the object."""
        # For immutable types like str, returning self is standard practice for shallow copies.
        # If `value` were mutable, you might need `copy.copy(self.value)`.
        return self.__class__(value=self.value)
