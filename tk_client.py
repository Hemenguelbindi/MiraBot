import httpx
from configurations.config import CONNECT_LINK


if __name__ == "__main__":
    with httpx.Client() as client:
        r = client.post(CONNECT_LINK+"sample")
        print(r.status_code)

