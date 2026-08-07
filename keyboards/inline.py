from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from config import (
    CHANNEL_USERNAME,
    X_URL
)


def start_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "🚀 START AIRDROP",
                callback_data="start_airdrop"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)


def tasks_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "📢 Join Telegram",
                url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}"
            )

        ],

        [

            InlineKeyboardButton(
                "✅ Check Join",
                callback_data="check_channel"
            )

        ],

        [

            InlineKeyboardButton(
                "🐦 Follow X",
                url=X_URL
            )

        ],

        [

            InlineKeyboardButton(
                "💎 Submit TON Wallet",
                callback_data="wallet"
            )

        ],

        [

            InlineKeyboardButton(
                "👥 Invite Friends",
                callback_data="invite"
            )

        ]

    ]

    return InlineKeyboardMarkup(keyboard)
