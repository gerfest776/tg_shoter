import asyncio
from unittest.mock import AsyncMock

import pytest
from aiogram.types import InputFile, InputMedia

from core.db.db_api import WhoisAPI
from core.db.tables import DatabaseTables
from handlers.groups.screen_groups import handle_link_message_groups


@pytest.mark.asyncio
async def test_group_screen_handle():
    await DatabaseTables().init_database()
    url = "https://github.com"
    message_mock = AsyncMock(text=f"/screen {url}")
    await handle_link_message_groups(message_mock)
    assert isinstance(message_mock.method_calls[0].args[0], InputFile)
    assert message_mock.method_calls[0].args[1] == "Your image is processing..."
    await asyncio.sleep(3)
    assert isinstance(message_mock.mock_calls[2].args[0], InputMedia)
    assert isinstance(message_mock.mock_calls[2].args[0].caption, str)

    record = dict(await WhoisAPI.check_url_in_db(url))
    assert record["exists"]
