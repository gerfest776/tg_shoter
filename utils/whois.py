import socket

import asyncwhois

from core.db.db_api import whois_table


async def get_whois(url: str) -> None:
    # ip = socket.gethostbyname(url)
    ip = "108.177.16.0"
    res = await asyncwhois.aio_whois_ipv4(ip)
    await whois_table.insert_url_whois_to_db(
        ip,
        url,
        res.parser_output["org_country"],
        res.parser_output["org_city"],
        res.parser_output["organization"],
    )
