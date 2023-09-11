def byte_stuffing(input):

  flagByte = "FLAG"
  escapeByte = "E"

  x = input.replace(escapeByte, escapeByte*2)
  y = x.replace(flagByte, escapeByte+flagByte)

  return print (f"Frame: {flagByte}{y}{flagByte}")

byte_stuffing("EEBZ")

