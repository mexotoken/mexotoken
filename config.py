import os
from dotenv import load_dotenv

load_dotenv()


# Bot Settings

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))


# Airdrop Settings

AIRDROP_REWARD = 3000
REFERRAL_REWARD = 500


# Telegram Channel

CHANNEL_USERNAME = "@Mexotoken"


# X (Twitter)

X_URL = "https://x.com/MexoToken"


# Database

DATABASE_NAME = "data/mexo.db"


# Messages

WELCOME_TEXT = """
🪙 Welcome to MEXO Airdrop

Join the MEXO community and complete simple tasks to earn MEXO tokens.

"""


AIRDROP_TEXT = f"""
🎁 Your Airdrop

Complete the tasks below to receive {AIRDROP_REWARD:,} MEXO
"""


FINISH_TEXT = f"""
🎉 Congratulations!

You have earned {AIRDROP_REWARD:,} MEXO.
"""
