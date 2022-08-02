import asyncio

import asyncpg

from config import settings


class RawConnection:
    @staticmethod
    async def _make_request(
        sql: str,
        params: [tuple, list[tuple]] = None,
        retries_count: int = 5,
        fetch: bool = False,
    ):
        if RawConnection.connection_pool is None:
            RawConnection.connection_pool = await asyncpg.create_pool(
                **settings.get_db_connection_data()
            )
            async with RawConnection.connection_pool.acquire() as conn:
                conn: asyncpg.Connection
                for _ in range(retries_count):
                    try:
                        await conn.execute(sql, params)
                    except Exception as e:
                        if "Deadlock found" in str(e):
                            await asyncio.sleep(1)
                        else:
                            pass
                    finally:
                        await RawConnection.connection_pool.release(conn)
                    if fetch:
                        return await conn.fetch(sql, params)
