from yt_dlp import YoutubeDL


def movie(movie_url: str, start_time: int, end_time: int):

    def set_download_ranges(info_dict, self):
        duration_opt = [{
            'start_time': start_time,
            'end_time': end_time
        }]
        return duration_opt

    ydl_opts = {
        'download_ranges': set_download_ranges
    }

    movieURL: str = movie_url

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(movieURL)


def sound(movie_url: str, start_time: int, end_time: int):

    def set_download_ranges(info_dict, self):
        duration_opt = [{
            'start_time': start_time,
            'end_time': end_time
        }]
        return duration_opt

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'download_ranges': set_download_ranges
    }

    movieURL: str = movie_url

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(movieURL)
