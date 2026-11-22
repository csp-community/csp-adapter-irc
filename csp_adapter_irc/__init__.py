"""CSP adapter for IRC, built on chatom."""

__version__ = "0.1.0"

from chatom.irc import (
    IRC_CAPABILITIES,
    IRCBackend,
    IRCChannel,
    IRCConfig,
    IRCMessage,
    IRCPresence,
    IRCUser,
    MockIRCBackend,
    mention_channel,
    mention_user,
)

from .adapter import IRCAdapter

__all__ = (
    "IRC_CAPABILITIES",
    "IRCAdapter",
    "IRCBackend",
    "IRCChannel",
    "IRCConfig",
    "IRCMessage",
    "IRCPresence",
    "IRCUser",
    "MockIRCBackend",
    "mention_channel",
    "mention_user",
)
