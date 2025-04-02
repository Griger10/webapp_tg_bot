from aiogram.fsm.state import StatesGroup, State


class StartFSM(StatesGroup):
    share_phone = State()
    success = State()


class TicketFSM(StatesGroup):
    topic = State()
    description = State()
    success = State()
