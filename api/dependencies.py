from owm.client import OWMClient


def get_api_key(api_key: str = "key") -> OWMClient:
    own_client = OWMClient(api_key)
    return own_client
