"""
This exists so that we have a stable point of communication and socket ownership
for components that are less robust, such as those which might fail abruptly
due to external API issues. There's little room to improve this design wise
unless the design of the whole application needs adjustments for scale.
"""


import zmq


def main():
    ctx = zmq.Context()
    puller = ctx.socket(zmq.PULL)
    publisher = ctx.socket(zmq.PUB)
    publisher.bind("tcp://127.0.0.1:5555")
    puller.bind("tcp://127.0.0.1:5556")
    while True:
        msg = puller.recv()
        publisher.send(msg)


if __name__ == "__main__":
    main()
