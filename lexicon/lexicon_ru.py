import random


STIKER_HELLO: list = [
    "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif", 
    "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif",
    "https://ineedanime.com/wp-content/uploads/2021/09/sawako-kuronuma-wave.gif",
    "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
    "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
    "https://static.wikia.nocookie.net/criminal-case-grimsborough/images/a/af/Waving_Anime_Girl.gif/revision/latest/scale-to-width-down/300?cb=20141003120301",
    "https://media.tenor.com/n1szpPp19d0AAAAM/yuigahama-yahallo.gif",
    "https://64.media.tumblr.com/ec3c2b97aa28dd215acba2e29f3956bf/tumblr_o8ncepi5G61vptudso1_500.gif",
]

ANSWER_ADMIN: dict = {
    "Victor": """Хозяин я умею расказывать про погоду! Вы такой молодец.\nTodo для хозяина: Реализовать возможность авто отправки сообщения.""",
    "Kristina": "Ох, это же самая лучшая хозайка в мире!"
    }


hello_random_file: str = random.choice(STIKER_HELLO)