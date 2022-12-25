import ytdlpbytime.download as dl_bytime


def main():
    movie_url: str = 'https://www.youtube.com/watch?v=v0ZQU2gq_J0'
    start_time: int = 10
    end_time: int = 45

    dl_bytime.movie(movie_url, start_time, end_time)


if __name__ == "__main__":
    main()
