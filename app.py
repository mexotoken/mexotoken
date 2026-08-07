from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from database import create_database

from handlers.start import start_command
from handlers.tasks import (
    start_airdrop,
    check_channel,
)
from handlers.account import account
from handlers.referral import invite_friends
from handlers.leaderboard import leaderboard
from handlers.admin import admin_stats


async def on_start(app):
    await create_database()


app = (
    Application.builder()
    .token(BOT_TOKEN)
    .post_init(on_start)
    .build()
)


app.add_handler(
    CommandHandler("start", start_command)
)

app.add_handler(
    CommandHandler("account", account)
)

app.add_handler(
    CommandHandler("leaderboard", leaderboard)
)

app.add_handler(
    CommandHandler("admin", admin_stats)
)


app.add_handler(
    CallbackQueryHandler(
        start_airdrop,
        pattern="^start_airdrop$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        check_channel,
        pattern="^check_channel$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        invite_friends,
        pattern="^invite$"
    )
)


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        account
    )
)


if __name__ == "__main__":
    app.run_polling()
