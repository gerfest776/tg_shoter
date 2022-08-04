from core.db.connection import RawConnection


class DatabaseTables(RawConnection):
    @staticmethod
    async def create_whois_table():
        sql = """CREATE TABLE IF NOT EXISTS whois(
            id SERIAL PRIMARY KEY,
            ip INET UNIQUE,
            url VARCHAR(256) UNIQUE,
            country VARCHAR(50),
            city VARCHAR(100),
            organization VARCHAR(100));
            """
        await DatabaseTables.make_request(sql)

    async def init_database(self):
        tables = ("whois",)
        for table in tables:
            await eval(f"self.create_{table}_table()")


database = DatabaseTables()
