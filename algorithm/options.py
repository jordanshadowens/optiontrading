from market.market import Market

class Options:

    def __init__(self, session, account, base_url):
        self.session = session
        self.account = account
        self.base_url = base_url

    def start_script(self):
        market = Market(self.session, self.base_url, self.account)
        market.get_optionchain('TSLA')
