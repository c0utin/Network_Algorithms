"""
RLE Explanation: 

The algorithm, executed at the link layer,
defines frame boundaries to segment data accurately.
While it aids in frame validation and loss detection,
it's susceptible to disruption from noise affecting the index byte,
leading to its disuse in modern networking technologies and protocols.

"""

def encapsulate_message(message_number):
    message_str = str(message_number)
    encapsulated = []

    index = 0
    while index < len(message_str):
        size = int(message_str[index])
        index += 1
        end_index = index + size
        if end_index <= len(message_str):
            encapsulated.append(message_str[index:end_index])
            index = end_index

    return encapsulated

def decapsulate_message(encapsulated):
    message_str = "".join(encapsulated)
    message_number = int(message_str)
    return message_number

# Usage example:
message_number = 634713591340567056383019525630561985

encapsulated = encapsulate_message(message_number)
print(f"Original message (number): {message_number}")
print(f"Encapsulated message: {encapsulated}")

message_decapsulated = decapsulate_message(encapsulated)
print(f"Decapsulated message (number): {message_decapsulated}")
