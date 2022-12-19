from yt_dlp import YoutubeDL

YOUTUBE_URL: str = 'http://www.youtube.com/watch?v='


def ytdlp_bytime(movie_id: str, start_time: int, end_time: int):

    def dowload_ranges(info_dict, self):
        duration_opt = [{
            'start_time': start_time,
            'end_time': end_time
        }]
        return duration_opt

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'download_ranges': download_ranges
    }

    movieURL: str = YOUTUBE_URL + movie_id

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(movieURL)
