import vk


class VKpost_main:
    session = vk.AuthSession(app_id='6730953', user_login='silvalexey@gmail.com', user_password='StarSilver95',
                             scope='friends')
    api = vk.API(session, v='2.0.2', lang='ru', timeout=10)
    posts = api.fave.getPosts(user_id=70879234, count=2)

    def getPost(self):
        print(self.posts)