"""IRC CSP adapter using chatom's IRC backend."""

from chatom.csp import BackendAdapter
from chatom.irc import IRCBackend, IRCConfig

__all__ = ("IRCAdapter",)


# chatom declares BackendAdapter conditionally: a placeholder function when csp is
# missing, the real class otherwise. csp is a hard dependency here, so it is always
# the class at runtime, but ty sees the union of both branches.
class IRCAdapter(BackendAdapter):  # ty: ignore[invalid-base]
    """CSP adapter for IRC, wrapping chatom's IRCBackend.

    ``subscribe()`` returns a time series of incoming messages and ``publish()``
    sends them.
    """

    def __init__(self, config: IRCConfig):
        super().__init__(IRCBackend(config=config))
