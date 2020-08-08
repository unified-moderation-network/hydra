from __future__ import annotations

"""
This really small component should probably be
replaced with native code later.

It exists so that we have a stable point of communication and socket ownership
for components that are less robust, such as those which might fail abruptly
due to external API issues. There's little room to improve this design wise
unless the design of the whole application needs adjustments for scale.

This makes a good target for native code later on given the simplicity of it
and the role in the application.
"""


import zmq


PUB_ADDR = "epgm://localhost:5555"
PULL_ADDR = "tcp://localhost:5556"


def main():
    ctx = zmq.Context()

    puller = ctx.socket(zmq.PULL)
    publisher = ctx.socket(zmq.PUB)
    puller.bind(PULL_ADDR)
    publisher.bind(PUB_ADDR)

    while True:
        msg = puller.recv_multipart()
        publisher.send_multipart(msg)
