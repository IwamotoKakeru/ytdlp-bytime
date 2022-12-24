import ytdlp_bytime


def main():
    movie_url: str = 'https://www.youtube.com/watch?v=6T8Jia_4tZc'
    start_time: int = 10
    end_time: int = 45

    ytdlp_bytime.download_movie_bytime(movie_url, start_time, end_time)


if __name__ == "__main__":
    main()
