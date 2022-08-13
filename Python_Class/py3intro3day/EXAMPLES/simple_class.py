#!/usr/bin/env python

class Simple():  # <1>
    def __init__(self, message_text):  # <2>
        self._message_text = message_text  # <3>

    def text(self):  # <4>
        return self._message_text


if __name__ == "__main__":
    msg1 = Simple('hello')  # <5>
    print(msg1.text())  # <6>

    msg2 = Simple('hi there')  # <7>
    print(msg2.text())
