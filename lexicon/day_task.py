import random
from datetime import datetime

warm_up_tranging = [
    "https://youtu.be/2ax28C-hWPY",
    "https://youtu.be/DJcG7AUuzBA",
    "https://www.youtube.com/watch?v=5vfqX6wGTWQ",
    "https://www.youtube.com/watch?v=qRXs-c3LHr4",
    "https://www.youtube.com/watch?v=xit7yDZguYY",
    "https://www.youtube.com/watch?v=YArvGEk8c6c",
]
hands_traning = [
    "https://youtu.be/eSwsiODvzeA",
    "https://www.youtube.com/watch?v=zXLwlRGfCMQ",
    "https://www.youtube.com/watch?v=Lu0ZVXcaiPI",
    "https://www.youtube.com/watch?v=E5_SDJXuGkg",
]

press_traning= [
    "https://www.youtube.com/watch?v=v2ruAhNGiUE&t=124s",
    "https://www.youtube.com/watch?v=p4OLS1iByYA",
    "https://www.youtube.com/watch?v=8dPiN8I7q_U",
    "https://youtu.be/2nlSPvy20JI",
]
all_body_traning = [
    "https://www.youtube.com/watch?v=Ex1XOU1wr64",
    "https://www.youtube.com/watch?v=23WTBzutLJE",
    "https://www.youtube.com/watch?v=j9j9TIMu6xQ",
    "https://www.youtube.com/watch?v=IbdS_z2Pu4c",
]
cardios_traning = [
    "https://www.youtube.com/watch?v=ChkB8xFLPfM",
    "https://www.youtube.com/watch?v=vHHp56rVygk",
    "https://www.youtube.com/watch?v=miPJFOj-9m0",
    "https://www.youtube.com/watch?v=fG-p3lgTOa8",
]
hitch_traning = [
    "https://www.youtube.com/watch?v=eSzUNyWh0zg",
    "https://www.youtube.com/watch?v=y3DjEepGlkQ",
    "https://www.youtube.com/watch?v=qRXs-c3LHr4&t=23s",
    "https://www.youtube.com/watch?v=h5nKxK8bmB0",
]
stretching_traning = [
    "https://www.youtube.com/watch?v=CHhQb_mUNcU",
    "https://www.youtube.com/watch?v=3ZjkYjtvrek",
    "https://www.youtube.com/watch?v=3YP6Ldxj71U",
    "https://www.youtube.com/watch?v=X1BbolkPf0I",
    "https://www.youtube.com/watch?v=4JZCt9Ex-ow",
]


def genarate_traning() -> str:
    weekday = datetime.now().date()
    match weekday.strftime('%w'):
        case 1:
            return (f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:\n</b>"
                    f"Разминка: {random.choice(warm_up_tranging)}\n"
                    f"Упражнения для рук: {random.choice(hands_traning)}\n"
                    f"Заминка: {random.choice(hands_traning)}\n"
                    "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"
                    )
        case 2:
            return (
                f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:\n</b>"
                f"Разминка: {random.choice(warm_up_tranging)}\n"
                f"Упражнения на пресс: {random.choice(press_traning)}\n"
                f"Заминка: {random.choice(hands_traning)}\n"
                "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"
                )
        case 3:
            return (
                f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:\n</b>"
                f"Разминка: {random.choice(warm_up_tranging)}\n"
                f"Упражнения на все тело: {random.choice(all_body_traning)}\n"
                f"Заминка: {random.choice(hands_traning)}\n"
                "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"
            )
        case 4:
            return (
                f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:\n</b>"
                f"Разминка: {random.choice(warm_up_tranging)}\n"
                f"Кардио в студию: {random.choice(cardios_traning)}\n"
                f"Заминка: {random.choice(hands_traning)}\n"
                "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"
            )

        case 5:
            return (
                f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:\n</b>"
                f"Разминка: {random.choice(warm_up_tranging)}\n"
                f"Растяжка на все тело: {random.choice(stretching_traning)}\n"
                f"Заминка: {random.choice(hands_traning)}\n"
                "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"
            )
        case 6:
            return (
                f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:\n</b>"
                f"Разминка: {random.choice(warm_up_tranging)}\n"
                f"Кардио в студию: {random.choice(cardios_traning)}\n"
                f"Заминка: {random.choice(hands_traning)}\n"
                "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"
            )
        case 7:
            return (
                f"<b>Приветсвую сегодня понедельник и выбор упражнений у нас вот такой:\n</b>"
                f"Разминка: {random.choice(warm_up_tranging)}\n"
                f"Упражнения на все тело: {random.choice(all_body_traning)}\n"
                f"Заминка: {random.choice(hands_traning)}\n"
                "И не забудь отчитаться о выполнение спасибо! Удачи, с каждым днем ты становишься все лучше!"
            )


if __name__ == "__main__":
    print(genarate_traning())