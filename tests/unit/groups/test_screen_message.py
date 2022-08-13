from unittest.mock import AsyncMock

import pytest

from handlers.groups.screen_groups import handle_link_message_groups


@pytest.mark.asyncio
async def test_group_screen_handle():
    message_mock = AsyncMock(text="/screen ozckzdc")
    await handle_link_message_groups(message_mock)
    assert message_mock.reply.await_args[0][0] == "Please, send correct url"
