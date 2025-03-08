from typing import Any

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner  # type: ignore


async def get_share_phone_text(
    dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs: Any
) -> dict[str, str]:
    return {"text": i18n.phone.text()}
