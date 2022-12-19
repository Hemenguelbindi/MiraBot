import random
from loguru import logger

STIKER_HELLO: list[str] = [
    "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif", 
    "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif",
    "https://ineedanime.com/wp-content/uploads/2021/09/sawako-kuronuma-wave.gif",
    "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
    "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
    "https://static.wikia.nocookie.net/criminal-case-grimsborough/images/a/af/Waving_Anime_Girl.gif/revision/latest/scale-to-width-down/300?cb=20141003120301",
    "https://media.tenor.com/n1szpPp19d0AAAAM/yuigahama-yahallo.gif",
    "https://64.media.tumblr.com/ec3c2b97aa28dd215acba2e29f3956bf/tumblr_o8ncepi5G61vptudso1_500.gif",
]

HELP_ANIMATIONS: list[str] = [
    "https://www.icegif.com/wp-content/uploads/2022/07/icegif-1198.gif",
    "https://thumbs.gfycat.com/AcclaimedSimilarHalibut-size_restricted.gif",
    "https://thumbs.gfycat.com/DefensiveRigidHorsefly-size_restricted.gif",
    "https://www.gifcen.com/wp-content/uploads/2022/06/anime-girl-gif-7.gif",
    "https://aniyuki.com/wp-content/uploads/2021/12/aniyuki-anime-girl-36.gif",
]

def get_random_hello() -> str:
    try:
        return random.choice(STIKER_HELLO)
    except Exception as e:
        logger.error(e)
        return None

def get_random_help() -> str:
    try:
        return random.choice(HELP_ANIMATIONS)
    except Exception as e:
        return None
    
