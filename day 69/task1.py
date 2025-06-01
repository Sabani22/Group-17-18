def split(sentence):
    return sentence.split("$")

input_string = "ეს$არის$დავალება$სადაც$დაშორებულია$სიტყვები"
result = split(input_string)
print(result)
