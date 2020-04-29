from app_config import Cesar
from guizero import App, Text, TextBox, PushButton


class Application(App):

    def __init__(self):
        self.app = App(title="Cesar's Challenge", width=600, height=200)
        self.message = Text(self.app, text="Welcome to Cesar's Cryptography Challenge", width='fill')
        self.url_label = Text(self.app, text='URL: ')
        self.url = TextBox(self.app, text='Insert an URL here...', width='fill')
        self.token_label = Text(self.app, text='Token: ')
        self.token = TextBox(self.app, text='Insert your token here...', width='fill')
        self.bt_request = PushButton(self.app, text='Make a Request!', command=self.make_request)
        self.run_app()

    def run_app(self):
        self.app.display()

    def make_request(self):
        url = self.url.value
        token = self.token.value
        cs = Cesar()
        try:
            cs.request(url, token)
            cs.post_request('answer.json')
        except RuntimeError:
            print('Error')



"""""
if __name__ == App:
    app = Application()
"""""

app = Application()
