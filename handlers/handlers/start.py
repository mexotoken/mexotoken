import secrets

from telegram import Update

from telegram.ext import ContextTypes

from telegram.constants import ParseMode

from config import WELCOME_TEXT

from database import (
    add_user,
    get_user
)

from keyboards.inline import start_keyboard


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    telegram_id = user.id

    ref_code = secrets.token_hex(4)

    referred_by = None

    if context.args:

        referred_by = context.args[0]


    db_user = await get_user(
        telegram_id
    )


    if not db_user:

        await add_user(
            telegram_id=telegram_id,
            username=user.username,
            first_name=user.first_name,
            ref_code=ref_code,
            referred_by=referred_by
        )


    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=start_keyboard()
    )
