import aiosqlite

from config import DATABASE_NAME


async def create_database():

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            telegram_id INTEGER UNIQUE,

            username TEXT,

            first_name TEXT,

            wallet TEXT,

            ref_code TEXT UNIQUE,

            referred_by TEXT,

            telegram_joined INTEGER DEFAULT 0,

            twitter_done INTEGER DEFAULT 0,

            wallet_done INTEGER DEFAULT 0,

            airdrop_completed INTEGER DEFAULT 0,

            invite_count INTEGER DEFAULT 0,

            referral_reward INTEGER DEFAULT 0,

            balance INTEGER DEFAULT 0,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        await db.commit()



async def add_user(
    telegram_id,
    username,
    first_name,
    ref_code,
    referred_by=None
):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute("""
        INSERT OR IGNORE INTO users
        (
            telegram_id,
            username,
            first_name,
            ref_code,
            referred_by
        )

        VALUES (?,?,?,?,?)

        """,
        (
            telegram_id,
            username,
            first_name,
            ref_code,
            referred_by
        ))

        await db.commit()



async def get_user(telegram_id):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *
            FROM users
            WHERE telegram_id=?
            """,
            (telegram_id,)
        )

        return await cursor.fetchone()



async def update_wallet(
    telegram_id,
    wallet
):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute(
            """
            UPDATE users

            SET wallet=?,
            wallet_done=1

            WHERE telegram_id=?

            """,
            (
                wallet,
                telegram_id
            )
        )

        await db.commit()



async def update_task(
    telegram_id,
    task
):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute(
            f"""
            UPDATE users

            SET {task}=1

            WHERE telegram_id=?

            """,
            (telegram_id,)
        )

        await db.commit()



async def update_balance(
    telegram_id,
    amount
):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute(
            """
            UPDATE users

            SET balance = balance + ?

            WHERE telegram_id=?

            """,
            (
                amount,
                telegram_id
            )
        )

        await db.commit()



async def get_top_users(limit=10):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *
            FROM users
            ORDER BY invite_count DESC
            LIMIT ?
            """,
            (limit,)
        )

        return await cursor.fetchall()



async def get_total_users():

    async with aiosqlite.connect(DATABASE_NAME) as db:

        cursor = await db.execute(
            """
            SELECT COUNT(*)
            FROM users
            """
        )

        result = await cursor.fetchone()

        return result[0]
