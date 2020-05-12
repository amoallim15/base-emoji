"""
Base Emoji Encoding

Implementation of  a binary-to-emoji encoding scheme
that represent binary data in a subset of the Unicode Emoji symbols.
"""

# This module is capable of triggering senior programmers effortlessly.
# Random emojis in group messaging app have meaning now!
# For ultimate mockery implement more flavors of different emoji
# groups sad/happy/flags/cat-face ;)
# Bordom is good.

from abc import ABCMeta, abstractmethod


class OutOfOrderException(Exception):
    pass


class CodepointException(Exception):
    pass


class FlavorException(Exception):
    pass


class Flavor(metaclass=ABCMeta):
    def __init__(self, name, flavorcp, base):
        self.name = name
        self.flavorcp = flavorcp
        self.base = base

    @abstractmethod
    def codepoint(self, order):
        pass

    @abstractmethod
    def char(self, cp):
        pass

    @abstractmethod
    def emojis(self):
        pass

    def __repr__(self):
        return (
            f"Flavor (name={self.name}, "
            f"flavor_codepoint={hex(self.flavorcp)}, "
            f"base={self.base})"
        )


class DefaultFlavor(Flavor):
    """
    Default Emoji Flavor. {55} Symbols supported.
    """

    def __init__(self):
        super().__init__(name="default", flavorcp=0x1F600, base=55)

    def codepoint(self, order):
        if order < 0 or order >= self.base:
            raise OutOfOrderException(f"order {order} is larger than the flavor base.")
        return (self.flavorcp + 1) + order

    def char(self, cp):
        if cp < self.flavorcp or cp >= (self.flavorcp + 1) + self.base:
            raise CodepointException(f"codepoint {cp} is not part of the flavor.")
        return chr(cp)

    def emojis(self):
        for order in range(self.base):
            yield self.char(self.codepoint(order)).encode("utf-8")


# class SmileysFlavor(Flavor):
#     def __init__(self):
#         raise NotImplementedError

#     def codepoint(self):
#         pass

#     def char(self):
#         pass

#     def emojis(self):
#         pass


def encode(s, flavor=DefaultFlavor):
    """
    Encode an object using different flavors.
    """
    flv = flavor()
    emojis = list(flv.emojis())
    s = s if isinstance(s, bytes) else str(s).encode("utf-8")
    coded, p, acc = b"", 1, 0
    for c in reversed(s):
        acc += p * c
        p = p << 8
    while acc:
        acc, idx = divmod(acc, flv.base)
        coded = emojis[idx] + coded
    return flv.char(flv.flavorcp) + coded.decode("utf-8")


def decode(s, flavor=DefaultFlavor):
    """
    Decode an object using different flavors.
    """
    flv = flavor()
    emojis = list(flv.emojis())
    s = s if isinstance(s, bytes) else str(s).encode("utf-8")
    coded, flavorcp, s, acc = b"", s[:4], s[4:], 0
    if flv.char(flv.flavorcp).encode("utf-8") != flavorcp:
        raise FlavorException(
            f"Flavor mismatch, {flv.name} flavor can not decode this."
        )
    for i in range(0, len(s), 4):
        c = s[i : i + 4]
        acc = acc * flv.base + emojis.index(c)
    while acc > 0:
        acc, mod = divmod(acc, 256)
        coded = bytes([mod]) + coded
    return coded.decode("utf-8")
