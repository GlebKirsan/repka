import lyricwikia


def get_lyrics(author: str, title: str) -> str:
    return lyricwikia.get_lyrics(author, title)


if __name__ == "__main__":
    author = input("Введите автора песни > ")
    title = input("Введите название песни > ")

    print('Текст песни')
    print(lyricwikia.get_lyrics(author, title))
