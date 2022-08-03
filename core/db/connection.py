import asyncpg
from loguru import logger

from config import settings


class RawConnection:
    connection_pool = None

    @staticmethod
    async def make_request(
        sql: str,
        retries_count: int = 5,
        fetch: bool = False,
    ):
        if RawConnection.connection_pool is None:
            RawConnection.connection_pool = await asyncpg.create_pool(
                **settings.get_db_connection_data(), command_timeout=60
            )
            async with RawConnection.connection_pool.acquire() as conn:
                conn: asyncpg.Connection
                for _ in range(retries_count):
                    try:
                        await conn.execute(sql)
                    except Exception as e:
                        logger.error(e)
                    else:
                        break
                if fetch:
                    return await conn.fetch(sql)
                else:
                    await RawConnection.connection_pool.release(conn)
