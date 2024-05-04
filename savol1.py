def find_last_position(substring, string):
    last_position = string.rfind(substring)
    return last_position

str1 = "Emma is a data scientist who knows Python. Emma works at google."
substring = "Emma"

last_position = find_last_position(substring, str1)
print(f"Last occurrence of {substring} starts at index {last_position}")