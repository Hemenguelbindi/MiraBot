import random
from loguru import logger


hello: list[str] = [
    "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif", 
    "https://media.tenor.com/3g3D1mECft0AAAAC/anime-hi.gif",
    "https://ineedanime.com/wp-content/uploads/2021/09/sawako-kuronuma-wave.gif",
    "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
    "https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif",
    "https://static.wikia.nocookie.net/criminal-case-grimsborough/images/a/af/Waving_Anime_Girl.gif/revision/latest/scale-to-width-down/300?cb=20141003120301",
    "https://media.tenor.com/n1szpPp19d0AAAAM/yuigahama-yahallo.gif",
    "https://64.media.tumblr.com/ec3c2b97aa28dd215acba2e29f3956bf/tumblr_o8ncepi5G61vptudso1_500.gif",
]

help: list[str] = [
    "https://www.icegif.com/wp-content/uploads/2022/07/icegif-1198.gif",
    "https://thumbs.gfycat.com/AcclaimedSimilarHalibut-size_restricted.gif",
    "https://thumbs.gfycat.com/DefensiveRigidHorsefly-size_restricted.gif",
    "https://www.gifcen.com/wp-content/uploads/2022/06/anime-girl-gif-7.gif",
    "https://aniyuki.com/wp-content/uploads/2021/12/aniyuki-anime-girl-36.gif",
]

clouds: list[str] = [
    "https://media.tenor.com/GK4kKaUWXesAAAAM/sky-anime.gif",
    "https://media.tenor.com/eQEHNQIUKIoAAAAC/anime-girl.gif",
    "https://media.tenor.com/Fyhu5etD_84AAAAC/anime-sky.gif",
    "https://i.pinimg.com/originals/82/e4/b0/82e4b0fe6382490b2299acdac0c94b55.gif",
    "https://i.pinimg.com/originals/29/a8/75/29a875eae195e1f2a3f8d763b3a1e89b.gif",
    "https://i.gifer.com/g0Qh.gif",
    "https://gifdb.com/images/high/anime-girl-watching-sea-creatures-fly-in-sky-s6rkqojuapiieri5.gif",
    ]

    
def choise_random_gif(gif_list_name: str) -> str:
        try:
            logger.info("Random choise image")
            match gif_list_name:
                case "hello":
                    return random.choice(hello)
                case "help":
                    return random.choice(help)
                case "clouds":
                    return random.choice(clouds)
        except Exception as e:
            logger.error(e)
            return None
