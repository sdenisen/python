from flask.json import jsonify
import json

__author__ = 'sdeni'
import vk_api

def auth_handler():

    return 85870528, True

def main():
    login, password = 'adders@bk.ru', '14zydfhz1!2@'
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    print ("we are successfully log in to vk.com")
    GROUP_TYPES = ['admin', 'editor', 'moder', 'groups', 'publics', 'events']
    for g in GROUP_TYPES:
        all_my_groups = vk_session.method(method='groups.get', values={'filter': g})
        print ("type: %s -> %s" % (g, all_my_groups))

    def getGroupActivity(id):
        group_info = vk_session.method(method='groups.getById', values={'group_id': id, 'fields': ' city, country, place, description, wiki_page, members_count, counters, start_date, finish_date, can_post, can_see_all_posts, activity, status, contacts, links, fixed_post, verified, site, ban_info, cover'})
        print ("group_info: %s" % group_info)

    getGroupActivity(7567360)

    def getNewsFeedBan():
        group_info = vk_session.method(method='newsfeed.getBanned',
                                       values={'extended': 1, 'fields': 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters, screen_name, maiden_name, timezone, occupation,activities, interests, music, movies, tv, books, games, about, quotes'})

        for j in group_info['groups']:
            if 'is_member' in j.keys():
                if j['is_member'] == 1:
                    print (j)
    getNewsFeedBan()

if __name__ == '__main__':
    main()