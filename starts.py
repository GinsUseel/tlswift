import re
from telethon.sync import TelegramClient
from telethon import events
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon.errors import BotInlineDisabledError, ChannelPrivateError
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon.tl.types import InputUserSelf
from telethon import errors

print('TLSwift Loaded.')

swift = events