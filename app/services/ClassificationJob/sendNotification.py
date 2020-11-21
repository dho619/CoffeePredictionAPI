from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushResponseError,
    PushServerError,
)
from requests.exceptions import ConnectionError, HTTPError

def send_push_message(message, token, extra=None):
    try:
        response = PushClient().publish(
            PushMessage(to=token,
                        body=message,
                        data=extra))
        return response
    except Exception as e:
        print(e)
