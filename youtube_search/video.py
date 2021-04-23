import requests
import json
import re


def find_substr(input_string):
    strings = {
        'title': r'<meta name="title" content="(.+?)">',
        'description': r'<meta name="description" content="(.+?)">',
        'keywords': r'<meta name="keywords" content="(.+?)">',
        'img_link': r'<link rel="image_src" href="(.+?)">',
        'publish_date': r'"publishDate":"(.+?)"'
    }
    data = {}
    for key in strings:
        result = re.findall(strings[key], input_string)
        try:
            data[key] = result[0].replace('<', '').replace('>', '')
        except IndexError:
            data[key] = ''
    return data


def get_videos_links(params):
    params['key'] = 'AIzaSyAmVfqK9tJKNKcV9ochOOSetUyb_cGKo6Y'
    params['maxResults'] = str(params['maxResults'])
    params['publishedAfter'] = '2021-04-01T00:00:00Z',  # Must be deleted
    if params['location_radius']:
        params['type'] = 'video'
        params['location_radius'] = str(params['location_radius']) + 'km'
    for key, value in params.copy().items():
        if not value:
            del (params[key])

    print(params)
    url = 'https://youtube.googleapis.com/youtube/v3/search'
    r = requests.get(url, params=params)
    resp_dict = json.loads(r.text)
    try:
        videos = [item['id']['videoId'] for item in resp_dict['items']]
    except KeyError:
        print('Wrong response')
        return []
    return videos


def get_detail(video_id):
    url = f'https://www.youtube.com/watch?v={video_id}'
    print(url)
    r = requests.get(url)
    html_doc = r.text
    return html_doc


def get_videos(params):
    video_data = []
    video_links = get_videos_links(params)
    for link in video_links:
        html_doc = get_detail(link)
        video_dic = find_substr(html_doc)
        video_dic['link'] = link
        video_data.append(video_dic)
    return video_data
