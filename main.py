from core.db.tables import database


async def on_startup(dp):
    import filters

    filters.setup(dp)

    from utils.admin_notify import on_startup_notify

    await on_startup_notify(dp)
    await database.init_database()


if __name__ == "__main__":
    from aiogram import executor

    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
