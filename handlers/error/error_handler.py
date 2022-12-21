from loguru import logger

from loader import dp, mira
from config_bot import admin_hemen

from message_exept import create_error_message


# Todo переписать написать свой и реализовать авто отправку увидомлений клиентов
@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param update:
    :param exception:
    :return: stdout logging
    """
    from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                          CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                          MessageTextIsEmpty, RetryAfter,
                                          CantParseEntities, MessageCantBeDeleted, BadRequest)

    if isinstance(exception, CantDemoteChatCreator):
        logger.debug("Can't demote chat creator")
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True

    if isinstance(exception, MessageNotModified):
        logger.debug('Message is not modified')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True
    if isinstance(exception, MessageCantBeDeleted):
        logger.debug('Message cant be deleted')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logger.debug('Message to delete not found')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logger.debug('MessageTextIsEmpty')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True

    if isinstance(exception, Unauthorized):
        logger.info(f'Unauthorized: {exception}')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True

    if isinstance(exception, InvalidQueryID):
        logger.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True

    if isinstance(exception, TelegramAPIError):
        logger.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True
    
    if isinstance(exception, RetryAfter):
        logger.exception(f'RetryAfter: {exception} \nUpdate: {update}')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True
    if isinstance(exception, CantParseEntities):
        logger.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True
    if isinstance(exception, BadRequest):
        logger.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
        return True
    mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(exception), 
                                            "chat_id":admin_hemen})
