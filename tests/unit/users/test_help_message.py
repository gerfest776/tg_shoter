from unittest.mock import AsyncMock

import pytest

from handlers.users.help import bot_help


@pytest.mark.asyncio
async def test_group_help_handle():
    message_mock = AsyncMock(text="/help")
    await bot_help(message=message_mock)
    assert (
        message_mock.method_calls[0][1][0] == "Just send me a link to get screenshot of your page!"
    )
