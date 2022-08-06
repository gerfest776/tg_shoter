from unittest.mock import AsyncMock

import pytest

from handlers.groups.help import bot_help


@pytest.mark.asyncio
async def test_group_help_handle():
    message_mock = AsyncMock(text="/help")
    await bot_help(message=message_mock)
    message_mock.answer.assert_called_with(
        "Hello, everyone!\nI am screen bot. Just send me a link to get screenshot of your page!"
    )
