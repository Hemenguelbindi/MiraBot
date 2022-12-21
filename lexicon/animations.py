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

rain: list[str] = [
    "https://media0.giphy.com/media/3qYZ2RnKW6veM/giphy.gif",
    "https://i.pinimg.com/originals/7a/4b/90/7a4b90c1fb431754e35218251dd0220d.gif",
    "https://gifdb.com/images/thumbnail/anime-rain-yukino-oha5in4uqghd6eb4.gif",
    "https://media.tenor.com/_CQxjNMw8i0AAAAd/anime-menhera.gif",
    "https://media.tenor.com/oDfaYWgbvGoAAAAC/anime-raining.gif",
    "https://i.gifer.com/D6ra.gif",
    "https://i.pinimg.com/originals/bf/fe/df/bffedfc88f6136c45bcccf30432138cc.gif",
    "https://media3.giphy.com/media/VFHa3Kg39gFLVbinN1/200w.gif?cid=6c09b952ouu3cmkkc92b2f4pb9v6k5id7epianehug3h117o&rid=200w.gif&ct=g",
]

snow: list[str] = [
    "https://media.tenor.com/kChUnN4Iv9gAAAAM/lord-el.gif",
    "https://i.pinimg.com/originals/42/d4/e4/42d4e4c15f286b71f6af39e07e25fafe.gif",
    "https://i.gifer.com/48qc.gif",
    "https://i.pinimg.com/originals/e6/99/41/e699411a4d4ff3c487c8103c18676666.gif",
    "https://i.pinimg.com/originals/e6/99/41/e699411a4d4ff3c487c8103c18676666.gif",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPcm-XDayZcodq6CBotTzj6_HBxqhlhX5IBQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwEql5DLrTwdnpT17syYdjaNchBz6y2KUcyQ&usqp=CAU",
    "https://animesher.com/orig/1/128/1288/12885/animesher.com_salt-flake-snow-snow-gif-1288500.gif",
]

thunderstorm: list[str] = [
    "https://media.tenor.com/goRRLNiv0WwAAAAM/thunder-anime.gif",
    "https://i.pinimg.com/originals/5b/a6/a5/5ba6a538061b7b99b1f5e8bb7fa00f93.gif",
    "https://i.pinimg.com/originals/62/74/44/6274449b7de92b80da82ca4fe151ba87.gif",
    "https://giffiles.alphacoders.com/113/113745.gif",
    "https://media.tenor.com/goRRLNiv0WwAAAAC/thunder-anime.gif",
    "https://media.tenor.com/wNTOa_xu-xkAAAAd/anime-lightning.gif",
    "https://64.media.tumblr.com/d85507353d36962d5c16e583757e032a/7a1449b05c4dcf5c-64/s500x750/03932dd05d44da2d9bdd5fe5344e404d4e6070ab.gif",
]
clear: list[str] = [
    "https://data.whicdn.com/images/331009426/original.gif",
    "https://i.pinimg.com/originals/15/b3/12/15b3125aeae577611bd3296381d3ea58.gif",
    "https://64.media.tumblr.com/3e38e1fb27067b471f306abc97454f0d/tumblr_nnuh4mQ1wP1ttmhcxo1_500.gif",
    "https://aniyuki.com/wp-content/uploads/2021/06/aniyuki-anime-avatars-gif-discord-56.gif",
    "https://media.tenor.com/Xl68k_UY0boAAAAM/sunrise-desert.gif",
    "https://64.media.tumblr.com/189dd51c5fee2a496ef1d16d54b399d2/2f0027a82b3b291d-04/s540x810/dcc921c8e0ea402ab0924bcb72c47972fdf05da4.gifv",
    "https://thumbs.gfycat.com/AdorableWarmheartedIndianabat-size_restricted.gif",
    "https://media.tenor.com/a9T2_mQK_6QAAAAC/anime-girl.gif",
]

other: list[str] = [
    "https://i.pinimg.com/originals/3d/08/8a/3d088a42a512fc3ae83f9bd209dd31e0.gif",
    "https://i0.wp.com/blerdyotome.com/wp-content/uploads/2016/07/shocked.gif?fit=500%2C281&ssl=1",
    "https://www.icegif.com/wp-content/uploads/2022/07/icegif-1198.gif",
    "https://media.tenor.com/HCaG2zPIo_UAAAAC/nezuko-kamado-demon-slayer.gif",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUVA1yK4bdIO4YDyn9uIoicAmHtrQ6d3O0Zg&usqp=CAU",
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
                case "rain":
                    return random.choice(rain)
                case "snow":
                    return random.choice(snow)
                case "thunderstorm":
                    return random.choice(thunderstorm)
                case "clear":
                    return random.choice(clear)
                case "other":
                    return random.choice(other)
                
        except Exception as e:
            logger.error(e)
            return None
