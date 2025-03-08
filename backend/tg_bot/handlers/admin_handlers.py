from aiogram import Router, F
from aiogram.filters import MagicData

router = Router()

router.message.filter(MagicData(F.event.chat.id.in_(F.admin_ids)))
