"""Tests for csp-adapter-irc."""

import csp_adapter_irc
from csp_adapter_irc import IRCAdapter, IRCBackend, IRCConfig


def test_exports():
    for name in csp_adapter_irc.__all__:
        assert getattr(csp_adapter_irc, name) is not None
    assert isinstance(csp_adapter_irc.__version__, str)


def test_adapter_wraps_backend():
    adapter = IRCAdapter(IRCConfig(server="irc.example.org", nickname="bot", channels=["#test"]))
    assert type(adapter.backend) is IRCBackend
    assert adapter.backend.config.server == "irc.example.org"
