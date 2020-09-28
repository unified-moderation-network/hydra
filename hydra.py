#   Copyright 2020 Michael Hall
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


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
