from unittest.mock import AsyncMock

import pytest

from handlers.users.start import bot_start


@pytest.mark.asyncio
async def test_group_help_handle():
    message_mock = AsyncMock(text="/start")
    message_mock.from_user.full_name = "John"
    await bot_start(message=message_mock)
    assert (
        message_mock.method_calls[0][1][0]
        == "Hello, John!\nI am screen bot. Just send me a link to get screenshot of your page!"
    )
