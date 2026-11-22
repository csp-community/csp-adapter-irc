"""Reply to any IRC message that says hello."""

import os

import csp
from csp import ts

from csp_adapter_irc import IRCAdapter, IRCConfig, IRCMessage


@csp.node
def reply_to_hello(msg: ts[IRCMessage]) -> ts[IRCMessage]:
    if "hello" in msg.content.lower():
        return IRCMessage(channel=msg.channel, content=f"hello, {msg.author_name}")


def graph(adapter: IRCAdapter):
    messages = csp.unroll(adapter.subscribe())
    csp.print("messages", messages)
    adapter.publish(reply_to_hello(messages))


if __name__ == "__main__":
    config = IRCConfig(
        server=os.environ["IRC_SERVER"],
        nickname=os.environ["IRC_NICKNAME"],
        password=os.environ.get("IRC_PASSWORD", ""),
        channels=[os.environ["IRC_CHANNEL"]],
    )
    csp.run(graph, IRCAdapter(config), realtime=True)
