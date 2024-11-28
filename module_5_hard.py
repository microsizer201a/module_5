import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user.nickname

    def register(self, nickname, password, age):
        user_exist = False
        for user in self.users:
            if user.nickname == nickname:
                user_exist = True
        if not user_exist:
            usr = User(nickname, password, age)
            self.users.append(usr)
            self.current_user = usr.nickname
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            title_exist = False
            for exist_video in self.videos:
                if video.title == exist_video.title:
                    title_exist = True
                    break
            if not title_exist:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        search_list = []
        for video in self.videos:
            search_title = video.title.lower()
            if search_word in search_title:
                search_list.append(video.title)
        return search_list

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if title == video.title:
                    current_user = None
                    for user in self.users:
                        if self.current_user == user.nickname:
                            current_user = user
                            break
                    if (video.adult_mode and current_user.age >= 18) or (not video.adult_mode):
                        for i in range(video.duration):
                            #time.sleep(1)
                            video.time_now += 1
                            print(video.time_now)
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    if video.time_now == video.duration:
                        print("Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1)
ur.add(v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



