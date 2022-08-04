from core.db.connection import RawConnection


class WhoisAPI(RawConnection):
    @staticmethod
    async def check_url_in_db(url: str):
        sql = "SELECT EXISTS(SELECT 1 FROM whois WHERE url = $1 )"
        params = (url,)
        return await WhoisAPI.make_request(sql, params, fetch=True)

    @staticmethod
    async def insert_url_whois_to_db(ip, url, country, city=None, organization=None):
        record = dict(await WhoisAPI.check_url_in_db(url))
        if not record["exists"]:
            sql = """INSERT INTO whois(ip, url, country, city, organization)
                   VALUES ($1, $2, $3, $4, $5)"""
            params = (ip, url, country, city, organization)
            await WhoisAPI.make_request(sql, params)

    @staticmethod
    async def get_whois_from_db(url):
        sql = "SELECT ip, country, city, organization FROM whois WHERE url = $1"
        params = (url,)
        return await WhoisAPI.make_request(sql, params, fetch=True)


whois_table = WhoisAPI()
