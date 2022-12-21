import httpx
from config_bot import BOT_TOKEN, CONNECT_LINK, admin_hemen, admin_kris


class TelegramClient:
    def __init__(self, token:str = BOT_TOKEN, base_url:str = CONNECT_LINK):
        self.token = token
        self.base_url = base_url
    
    def prepare_url(self, method: str):
        result_url = f"{self.base_url}/bot{self.token}/"
        if method is not None:
            result_url += method
        return result_url
    
    
    def post(self, method: str = None, params: dict = None, body: dict = None):
        url = self.prepare_url(method)
        with httpx.Client() as client:
            resp = client.post(url, params=params, data=body)
            return resp.json()

if __name__ == "__main__":
    telegram_client = TelegramClient(token=BOT_TOKEN, base_url=CONNECT_LINK)
    my_params = {'chat_id': admin_hemen, "text": "test message"}
    print(telegram_client.post(method="sendMessage", params=my_params))
    my_params = {'chat_id': admin_kris, "text": "test message"}
    print(telegram_client.post(method="sendMessage", params=my_params))