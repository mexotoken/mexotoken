from telegram import Update
from telegram.ext import ContextTypes

from database import get_account


async def account(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = await get_account(
        update.effective_user.id
    )

    if not user:

        await update.message.reply_text(
            "Please start the bot first."
        )
        return

    text = f"""
👤 Account

💰 Balance: {user["balance"]:,} MEXO

👥 Invites: {user["invite_count"]}

🎁 Referral Rewards: {user["referral_reward"]:,} MEXO

💎 Wallet:
{user["wallet"] if user["wallet"] else "Not submitted"}
"""

    await update.message.reply_text(text)
