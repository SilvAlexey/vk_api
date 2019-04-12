import vk

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Root(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    MainApp().run()


'''
session = vk.AuthSession(app_id='6730953', user_login='silvalexey@gmail.com', user_password='StarSilver95', scope='friends')
#session = vk.Session(access_token='5ecre7')
api = vk.API(session, v='2.0.2', lang='ru', timeout=10)
get_posts = api.fave.getPosts(user_id=70879234, offset=200, count=2)

posts = get_posts[1:]
print(get_posts)
[print(post) for post in posts]
'''