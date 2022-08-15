import asyncpg
from loguru import logger

from core.config import settings


class RawConnection:
    """
    class parent, which gives interface of pool connection
    """

    connection_pool = None

    @staticmethod
    async def make_request(
        sql: str,
        params: tuple | list[tuple] | None = None,
        retries_count: int = 5,
        fetch: bool = False,
    ):
        if RawConnection.connection_pool is None:
            logger.info(f"{settings.get_db_connection_data()}")
            RawConnection.connection_pool = await asyncpg.create_pool(
                **settings.get_db_connection_data()
            )
            logger.info(f"{RawConnection.connection_pool}")
        async with RawConnection.connection_pool.acquire() as conn:
            conn: asyncpg.Connection
            for _ in range(retries_count):
                try:
                    if params:
                        await conn.execute(sql, *params)
                    else:
                        await conn.execute(sql)
                except Exception as e:
                    logger.error(e)
                else:
                    break
            if fetch:
                return await conn.fetchrow(sql, *params)
            else:
                await RawConnection.connection_pool.release(conn)
