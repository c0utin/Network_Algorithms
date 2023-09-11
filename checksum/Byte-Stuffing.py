"""
It is important to remember that the choice of escape character
may vary depending on the specific communication protocol and system needs.
Therefore, in different contexts and implementations of data link protocols,
other characters may be chosen as the escape byte depending on the convenience
and security requirements of the protocol in question.

Byte stuffing: 

Is a data transmission technique used in communication protocols
to ensure that special characters, like flag bytes and escape bytes,
don't interfere with the actual data. In this algorithm
"""


def byte_stuffing(input):

  flagByte = "FLAG"
  escapeByte = "E"

  x = input.replace(escapeByte, escapeByte*2)
  y = x.replace(flagByte, escapeByte+flagByte)

  return print (f"Frame: {flagByte}{y}{flagByte}")

byte_stuffing("EEBZ")

