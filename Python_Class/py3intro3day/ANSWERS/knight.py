#!/usr/bin/env python

class Knight(object):
    def __init__(self, name):
        self._name = name
        with open('../DATA/knights.txt') as knights_in:
            for raw_line in knights_in:
                line = raw_line.rstrip('\n\r')
                (name, title, color, quest, comment) = line.split(":")
                if name == self._name:
                    self._title = title
                    self.favorite__color = color
                    self._quest = quest
                    self._comment = comment
                    break

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @property
    def favorite_color(self):
        return self.favorite__color

    @property
    def quest(self):
        return self._quest

    @property
    def comment(self):
        return self._comment


if __name__ == "__main__":
    k = Knight("Arthur")
    print(k.name, k.favorite_color, k.comment, k.title)
