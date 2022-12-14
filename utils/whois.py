import socket
from urllib.parse import urlparse

import asyncwhois
from loguru import logger

from core.db.db_api import whois_table


async def get_whois(url: str) -> None:
    ip = None
    try:
        ip = socket.gethostbyname(urlparse(url).netloc)
    except Exception as e:
        logger.error(f"Failing getting ip with socket: {e}")

    res = await asyncwhois.aio_whois_ipv4(ip)
    try:
        await whois_table.insert_url_whois_to_db(
            ip,
            url,
            res.parser_output["org_country"],
            res.parser_output["org_city"],
            res.parser_output["organization"],
        )
    except Exception as e:
        logger.error(f"Error while trying save {url} whois to db\n{e}")
