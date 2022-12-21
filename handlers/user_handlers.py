from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext
from lexicon import random_hello_user,  help_text, choise_random_gif
from external_services.weather import WeatherClient
from states.states import DateWeather


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_command_start_user, commands=['start', 'старт', "Старт"])
    dp.register_message_handler(send_command_help_user, commands=['help', "помощь", "Помощь"])



# Commad Start from user
async def send_command_start_user(message: types.Message):
   await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("hello"),                     
                caption=random_hello_user)
   await message.delete()
   
# Commad Help from user
async def send_command_help_user(message: types.Message):
   await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("help"),                     
                caption=help_text)
   await message.delete()


# async def send_command_weather(message: types.Message):
#     await message.answer("Введите название города на кирилице или латинице например: Moscow, Саратов")
#     await DateWeather.City.set()



# async def send_weather(message: types.Message, state: FSMContext):  
#     city = message.text
#     await state.update_data(city=city)
#     try:
#         weather = WeatherClient(city=city)
#         weather_data = weather.ask_data()
#         weather_description = weather_data["weather"][0]["main"]
        
#         match weather_description:
            
#             case "Clouds":
#                 await message.send_animation(
#                 chat_id=message.chat.id,
#                 animation=clouds,
#                 caption=weather.message_format_tg(),
#                 )
#                 await state.reset_state()
            
#             case "Rain":
#                 await mira.send_animation(
#                 chat_id=message.chat.id,
#                 animation=rain,
#                 caption=weather.message_format_tg()
#                 )
#                 await state.reset_state()
            
#             case "Thunderstorm":
#                 await mira.send_animation(
#                 chat_id=message.chat.id,
#                 animation=thunderstorm,
#                 caption=weather.message_format_tg(),
#                 )
#                 await state.reset_state()
            
#             case "Snow":
#                 await mira.send_animation(
#                 chat_id=message.chat.id,
#                 animation=snow,
#                 caption=weather.message_format_tg(),
#                 )
#                 await state.reset_state()
                
#             case "Clear":
#                 await mira.send_animation(
#                 chat_id=message.chat.id,
#                 animation=clear,
#                 caption=weather.message_format_tg(),
#                 )
#                 await state.reset_state()
            
#             case _ :
#                 await mira.send_animation(
#                 chat_id=message.chat.id,
#                 animation=atmosphere,
#                 caption=weather.message_format_tg(),
#                 )
#                 await state.reset_state()
                

#     except Exception as e:
#         await mira.send_message(
#             chat_id=message.chat.id,
#             text=("<b>Вы не правильно ввели название города. </b>"
#                   "<b>Повторите команду /weather, для получения погоды</b>"))
#         await state.reset_state()
#         mira.telegram_client.post(method="sendMessange", 
#                                   params={"text":create_error_message(e), 
#                                             "chat_id":admin_hemen})