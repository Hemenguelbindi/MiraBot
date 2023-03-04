import random
from datetime import datetime
from loguru import logger


class ImagesSelector:
    """Хранилище картинок"""
    def __init__(self):
        self.__img = {
            "hello": [
                "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif",
                "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif",
                "https://ineedanime.com/wp-content/uploads/2021/09/sawako-kuronuma-wave.gif",
                "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
                "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
                "https://64.media.tumblr.com/ec3c2b97aa28dd215acba2e29f3956bf/tumblr_o8ncepi5G61vptudso1_500.gif",
            ],

            "help": [
                "https://thumbs.gfycat.com/AcclaimedSimilarHalibut-size_restricted.gif",
                "https://thumbs.gfycat.com/DefensiveRigidHorsefly-size_restricted.gif",
                "https://aniyuki.com/wp-content/uploads/2021/12/aniyuki-anime-girl-36.gif",
            ],

            "clouds": [
                "https://media.tenor.com/GK4kKaUWXesAAAAM/sky-anime.gif",
                "https://media.tenor.com/eQEHNQIUKIoAAAAC/anime-girl.gif",
                "https://media.tenor.com/Fyhu5etD_84AAAAC/anime-sky.gif",
                "https://i.pinimg.com/originals/29/a8/75/29a875eae195e1f2a3f8d763b3a1e89b.gif",
                "https://i.gifer.com/g0Qh.gif",
            ],

            "rain": [
                "https://media0.giphy.com/media/3qYZ2RnKW6veM/giphy.gif",
                "https://i.pinimg.com/originals/7a/4b/90/7a4b90c1fb431754e35218251dd0220d.gif",
                "https://gifdb.com/images/thumbnail/anime-rain-yukino-oha5in4uqghd6eb4.gif",
                "https://i.gifer.com/D6ra.gif",
                "https://i.pinimg.com/originals/bf/fe/df/bffedfc88f6136c45bcccf30432138cc.gif",
            ],

            "snow": [
                "https://media.tenor.com/kChUnN4Iv9gAAAAM/lord-el.gif",
                "https://i.pinimg.com/originals/42/d4/e4/42d4e4c15f286b71f6af39e07e25fafe.gif",
                "https://i.gifer.com/48qc.gif",
                "https://i.pinimg.com/originals/e6/99/41/e699411a4d4ff3c487c8103c18676666.gif",
                "https://i.pinimg.com/originals/e6/99/41/e699411a4d4ff3c487c8103c18676666.gif",
                "https://animesher.com/orig/1/128/1288/12885/animesher.com_salt-flake-snow-snow-gif-1288500.gif",
            ],

            "thunderstorm": [
                "https://media.tenor.com/goRRLNiv0WwAAAAM/thunder-anime.gif",
                "https://i.pinimg.com/originals/5b/a6/a5/5ba6a538061b7b99b1f5e8bb7fa00f93.gif",
                "https://i.pinimg.com/originals/62/74/44/6274449b7de92b80da82ca4fe151ba87.gif",
                "https://giffiles.alphacoders.com/113/113745.gif",
                "https://media.tenor.com/goRRLNiv0WwAAAAC/thunder-anime.gif",
                "https://media.tenor.com/wNTOa_xu-xkAAAAd/anime-lightning.gif",
            ],

            "clear": [
                "https://data.whicdn.com/images/331009426/original.gif",
                "https://i.pinimg.com/originals/15/b3/12/15b3125aeae577611bd3296381d3ea58.gif",
                "https://64.media.tumblr.com/3e38e1fb27067b471f306abc97454f0d/tumblr_nnuh4mQ1wP1ttmhcxo1_500.gif",
                "https://aniyuki.com/wp-content/uploads/2021/06/aniyuki-anime-avatars-gif-discord-56.gif",
                "https://media.tenor.com/Xl68k_UY0boAAAAM/sunrise-desert.gif",
                "https://thumbs.gfycat.com/AdorableWarmheartedIndianabat-size_restricted.gif",
                "https://media.tenor.com/a9T2_mQK_6QAAAAC/anime-girl.gif",
            ],

            "other": [
                "https://media.tenor.com/OGLxbsYN7x0AAAAS/siesta-anime.gif",
                "https://media.tenor.com/e3hReDfulTsAAAAd/anime.gif",
            ],

            "sport": [
            "https://i.pinimg.com/originals/8f/94/35/8f943534fffd82233ad3f51167f02a3b.gif",
            "https://animesher.com/orig/1/188/1884/18841/animesher.com_sport-jump-girls-1884150.gif",
            "https://i.pinimg.com/originals/60/7a/35/607a354344d527ff5868ad46ace65888.gif",
            "https://media.tenor.com/A1b1qbwOwWIAAAAC/baseball-anime.gif",
            "https://media.tenor.com/QISAQBv9xx8AAAAC/nichijou-funny.gif",
            ],

            "just_learn": [
            "https://media4.giphy.com/media/6XX4V0O8a0xdS/giphy.gif",
            "https://i.pinimg.com/originals/20/b9/cd/20b9cd1fc76421096bfe205351789f89.gif",
            "https://media.tenor.com/sVhqqxs-7kYAAAAC/anime-studying.gif",
            "https://i.pinimg.com/originals/de/ed/d7/deedd73851f44c98c077e37504a53f2b.gif",
            ],

        }

    def random_img(self, gif_list_name: str) -> str:
        """Выбирает картинки на основе критериев заданных для выбора"""
        try:
            logger.info("Random choice image ")
            if gif_list_name in self.__img:
                return random.choice(self.__img[gif_list_name])
            else:
                return random.choice(self.__img["other"])
        except Exception as e:
            logger.error(e)
            return None


class LinkLessonSelector:
    """Хранилище ссылок на лекции"""

    def __init__(self):
        self.lesson = {
            "0": "Доброго вечера изучаем Go вот ссылка: https://stepik.org/lesson/526868/step/1?unit=519587",
            "1": "Доброго вечера изучаем Си вот ссылка: https://stepik.org/lesson/40164/step/1?unit=30907",
            "3": "Доброго вечера изучаем Rex на Python вот ссылка:https://stepik.org/lesson/701290/step/1?unit=701347",
            "4": "Доброго вечера изучаем Go вот ссылка: https://stepik.org/lesson/526868/step/1?unit=519587",
            "6": "Доброго вечера изучаем Си вот ссылка: https://stepik.org/lesson/40164/step/1?unit=30907",
        }

    def lesson_link(self):
        now = datetime.now()
        week_day = datetime.weekday(now)
        if str(week_day) in self.lesson:
            return self.lesson.get(str(week_day))
        return None


class LinkVideoSelector:
    """Класс хранилища со ссылками на видио """

    def __init__(self):
        self.__video = {
            "warm_up_tranging": [
                "https://youtu.be/2ax28C-hWPY",
                "https://youtu.be/DJcG7AUuzBA",
                "https://www.youtube.com/watch?v=5vfqX6wGTWQ",
                "https://www.youtube.com/watch?v=qRXs-c3LHr4",
                "https://www.youtube.com/watch?v=xit7yDZguYY",
                "https://www.youtube.com/watch?v=YArvGEk8c6c",
            ],
            "hands_traning": [
                "https://youtu.be/eSwsiODvzeA",
                "https://www.youtube.com/watch?v=zXLwlRGfCMQ",
                "https://www.youtube.com/watch?v=Lu0ZVXcaiPI",
                "https://www.youtube.com/watch?v=E5_SDJXuGkg",
            ],

            "press_traning": [
                "https://www.youtube.com/watch?v=v2ruAhNGiUE&t=124s",
                "https://www.youtube.com/watch?v=p4OLS1iByYA",
                "https://www.youtube.com/watch?v=8dPiN8I7q_U",
                "https://youtu.be/2nlSPvy20JI",
            ],
            "all_body_traning": [
                "https://www.youtube.com/watch?v=Ex1XOU1wr64",
                "https://www.youtube.com/watch?v=23WTBzutLJE",
                "https://www.youtube.com/watch?v=j9j9TIMu6xQ",
                "https://www.youtube.com/watch?v=IbdS_z2Pu4c",
            ],
            "cardios_traning": [
                "https://www.youtube.com/watch?v=ChkB8xFLPfM",
                "https://www.youtube.com/watch?v=vHHp56rVygk",
                "https://www.youtube.com/watch?v=miPJFOj-9m0",
                "https://www.youtube.com/watch?v=fG-p3lgTOa8",
            ],
            "hitch_traning": [
                "https://www.youtube.com/watch?v=eSzUNyWh0zg",
                "https://www.youtube.com/watch?v=y3DjEepGlkQ",
                "https://www.youtube.com/watch?v=qRXs-c3LHr4&t=23s",
                "https://www.youtube.com/watch?v=h5nKxK8bmB0",
            ],
            "stretching_traning": [
                "https://www.,youtube.com/watch?v=CHhQb_mUNcU",
                "https://www.youtube.com/watch?v=3ZjkYjtvrek",
                "https://www.youtube.com/watch?v=3YP6Ldxj71U",
                "https://www.youtube.com/watch?v=X1BbolkPf0I",
                "https://www.youtube.com/watch?v=4JZCt9Ex-ow",
            ],
        }

    def video_choice(self, type_vidio: str) -> str:
        """Выбирает ссылку на видио на основе критериев заданных для выбора"""
        try:
            logger.info("Random choice image")
            if type in self.__video:
                return random.choice(self.__video[type_vidio])
            else:
                return random.choice(self.__video["other"])
        except Exception as e:
            logger.error(e)
            return None


class MessageSelector:
    """Хранилище шаблонов текста """

    def __init__(self):
        self.__link = LinkVideoSelector()
        self.__message = {
            "help_message": ("Описание комманд:\n"
                             "/start /старт - запуск бота"
                             "/weather - позволяет узнать погоду, при использование нужно указать название города\n"
                             "Работает как с латиницей так и с кирилицей\n"
                             "(Moscow, Saratov, Ufa and ect)"),
            "from_admin": {"Victor": "Хозяин не медлите пожалуйста, улучайте меня дальше.",
                           "Kristina": "Ох, это же самая лучшая хозайка в мире!",
                           },
            "from_user": [
                "Здраствуй, мой дорогой пользователь!",
                "Ура, ты запустил меня",
                "Добро пожаловать! Я счастлив, что вы посетили нас впервые.",
                "Привет я бот Мира, если хочешь узнать что я могу и умею, напиши /help"
            ],
            "0": (f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:</b>\n"
                  f" Разминка: {random.choice(self.__link.video_choice('warm_up_tranging'))}\n"
                  f"Упражнения для рук: {random.choice(self.__link.video_choice('hands_traning'))}\n"
                  f"Заминка: {random.choice(self.__link.video_choice('hitch_traning'))}\n"
                  "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"),

            "1": (f"<b>Приветсвую сегодня вторник и выбор упражнений у нас вот такой:</b>\n"
                  f"Разминка: {random.choice(self.__link.video_choice('warm_up_tranging'))}\n"
                  f"Упражнения на пресс: {random.choice(self.__link.video_choice('press_traning'))}\n"
                  f"Заминка: {random.choice(self.__link.video_choice('stretching_traning'))}\n"
                  "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"),

            "2": (f"<b>Приветсвую сегодня среда и выбор упражнений у нас вот такой:</b>\n"
                  f"Разминка: {random.choice(self.__link.video_choice('warm_up_tranging'))}\n"
                  f"Упражнения на все тело: {random.choice(self.__link.video_choice('all_body_traning'))}\n"
                  f"Заминка: {random.choice(self.__link.video_choice('hitch_traning'))}\n"
                  "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"),

            "3": (f"<b>Приветсвую сегодня четверг и выбор упражнений у нас вот такой:</b>\n"
                  f"Разминка: {random.choice(self.__link.video_choice('warm_up_tranging'))}\n"
                  f"Кардио в студию: {random.choice(self.__link.video_choice('cardios_traning'))}\n"
                  f"Заминка: {random.choice(self.__link.video_choice('stretching_traning'))}\n"
                  "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"),

            "4": (f"<b>Приветсвую сегодня пятница и выбор упражнений у нас вот такой:</b>\n"
                  f"Разминка: {random.choice(self.__link.video_choice('warm_up_tranging'))}\n"
                  f"Растяжка на все тело: {random.choice(self.__link.video_choice('stretching_traning'))}\n"
                  f"Заминка: {random.choice(self.__link.video_choice('hitch_traning'))}\n"
                  "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"),

            "5": (f"<b>Приветсвую сегодня суббота и выбор упражнений у нас вот такой:\n</b>"
                  f"Разминка: {random.choice(self.__link.video_choice('warm_up_tranging'))}\n"
                  f"Кардио в студию: {random.choice(self.__link.video_choice('cardios_traning'))}\n"
                  f"Заминка: {random.choice(self.__link.video_choice('hitch_traning'))}\n"
                  "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"),

            "6": (f"<b>Приветсвую сегодня воскресенье и выбор упражнений у нас вот такой:\n</b>"
                  f"Разминка: {random.choice(self.__link.video_choice('warm_up_tranging'))}\n"
                  f"Упражнения на все тело: {random.choice(self.__link.video_choice('all_body_traning'))}\n"
                  f"Заминка: {random.choice(self.__link.video_choice('stretching_traning'))}\n"
                  "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"),
        }

    def message_sport(self):
        now = datetime.now()
        week_day = datetime.weekday(now)
        return self.__message.get(str(week_day))

    def message_admin(self, admin_name):
        return self.__message.get("from_admin")[admin_name]

    def message_user(self, header):
        return random.choice(self.__message.get(header))
