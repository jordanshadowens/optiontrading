
class Market:

    def __init__(self, session, base_url, account):
        self.session = session
        self.base_url = base_url
        self.account = account

    def get_optionchain(self, symbol):

        url = self.base_url + "/v1/market/optionchains.json"

        headers = {"Connection": "close"}
        params = {"symbol": symbol, "expiryYear": "2021", "expiryMonth": "08", "expiryDay": "20",
                  "strikePriceNear": "675", "noOfStrikes": "2"}

        response = self.session.get(url, header_auth=True, params=params, headers=headers)

        data = response.json()

        print(data)
