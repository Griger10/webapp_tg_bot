from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import RequestContact, Url
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Format, Const

from backend.tg_bot.bot_dialogs.main.getters import get_share_phone_text
from backend.tg_bot.bot_dialogs.main.handlers import phone_handler, topic_handler, problem_handler
from backend.tg_bot.fsm.states import StartFSM, TicketFSM

start_dialog = Dialog(
    Window(
        Format("{text}"),
        MessageInput(phone_handler, content_types=ContentType.CONTACT),
        RequestContact(Const("Поделиться номером телефона")),
        markup_factory=ReplyKeyboardFactory(resize_keyboard=True, selective=True),
        getter=get_share_phone_text,
        state=StartFSM.share_phone,
    ),
    Window(
        Const("<b>Отлично!</b>\n\nТеперь вы можете заполнить заявку по кнопке ниже👇"),
        Url(Const("Заполнить заявку 📝"), Const("https://google.com/")),
        state=StartFSM.success,
    ),
)

ticket_dialog = Dialog(
    Window(
        Const("<b>Введите причину обращения:</b>"),
        MessageInput(func=topic_handler, content_types=ContentType.TEXT),
        state=TicketFSM.topic
    ),
    Window(
        Const("<b>Опишите вашу проблему:</b>"),
        MessageInput(func=problem_handler, content_types=ContentType.TEXT),
        state=TicketFSM.description
    ),
    Window(
        Const("<b>Отлично!</b>\n\nВаша заявка отправлена в администрацию!"),
        state=TicketFSM.success
    )
)
