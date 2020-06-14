from googleapiclient.discovery import build

kumar_api = 'AIzaSyDgET9XthaNo24ZxAE7HIhAGouaeaU5Wl4'
api_key = "AIzaSyDs3np7cQSrWdAt_NEpJ9_3fHVB7q3S554"
final = build('youtube', 'v3', developerKey=kumar_api)


class YouTubeData:
    def __init__(self, search=None):
        self.search = search

    def get_channel_details(self, videoId):
        snippet = final.search().list(q=videoId, part="snippet", type='video', maxResults=9).execute()
        stuffs_for_frontend = []

        for item in snippet['items']:
            video_info = {
                'channelId': item['snippet']['channelId'],
                'id': item['id']['videoId'],
                'video_title': item['snippet']['title'],
                'video_description': item['snippet']['description'],
                'video_image': item['snippet']['thumbnails']['high']['url']
            }
            stuffs_for_frontend.append(video_info)
        return stuffs_for_frontend

    def get_uploads(self, channel_id):
        content = final.channels().list(id=channel_id, part="contentDetails", maxResults=9).execute()
        return content

    def get_playlists(self, uploadids=None):
        playlist = final.playlistItems().list(playlistId='UUCktnahuRFYIBtNnKT5IYyg', part="snippet",
                                              maxResults=50).execute()
        total_res = []
        for i, j in playlist['pageInfo'].items():
            print(i, j)
            total_res.append(j)
        return total_res

    def get_videoDetails(self, videoId):
        videoInfo = final.videos().list(id=videoId, part='snippet').execute()
        video_info = []
        for v in videoInfo['items']:

            video = {
                'id': v['id'],
                'publishedDate': v['snippet']['publishedAt'],
                'video_title': v['snippet']['title'],
                'video_description': v['snippet']['description']
            }
            video_info.append(video)
        return video_info

    def get_statistics(self, videoId):
        stats = final.videos().list(id=videoId, part='statistics').execute()
        ldc = []
        for i in stats['items']:
            statistics = {
                'viewCount': i['statistics']['viewCount'],
                'likeCount': i['statistics'].get('likeCount'),
                'dislikeCount': i['statistics'].get('dislikeCount'),
                'commentCount': i['statistics'].get('commentCount'),
                'favoriteCount': i['statistics'].get('favoriteCount')
            }
            ldc.append(statistics)
        return ldc

    def get_channel_stats(self, channelId):
        content = final.channels().list(id=channelId, part="statistics").execute()
        uploads = []
        for upload in content['items']:
            dic = {
                'totalViewCount': upload['statistics']['viewCount'],
                'totalSubscribers': upload['statistics']['subscriberCount'],
                'totalVideo': upload['statistics']['videoCount']
            }
            uploads.append(dic)
        return uploads
