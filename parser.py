import vk
import os
import json

session = vk.AuthSession(app_id='6730953', user_login='silvalexey@gmail.com', user_password='StarSilver95', scope='friends')
#session = vk.Session(access_token='5ecre7')
api = vk.API(session, v='2.0.2', lang='ru', timeout=10)

num_post = 0
get_posts = []
list_id = open('post_id.json', 'r')

if os.stat("post_id.json").st_size != 0:

    for id in list_id:
        get_posts = api.fave.getPosts(user_id=70879234, offset=num_post, count=1)[1:]

        if get_posts[0]['id'] == int(id):
            print(3)
            num_post = num_post + 1
        else:

            break
else:

    get_posts = api.fave.getPosts(user_id=70879234, offset=0, count=1)[1:]

post = get_posts
list_id.close()


print(get_posts)
#post = [post for post in posts]
print(post)
if os.path.isfile('post_id.json'):
    print(1)
    with open('data.json', 'a') as post_in_data:
        json.dump(post[0], post_in_data)
else:
    print(2)
    with open('data.json', 'w') as post_in_data:
        json.dump(post[0], post_in_data)

file_id = ''
if not os.path.isfile('post_id.json'):
    file_id = open('post_id.json', 'w')
    file_id.write(str(post[0]['id']) + '\n')
else:
    file_id = open('post_id.json', 'a')
    file_id.write(str(post[0]['id']) + '\n')
file_id.close()
