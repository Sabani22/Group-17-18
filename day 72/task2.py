def split_at_a(user):
    split_user = user.split('a')
    result = []
    for word in split_user:
        result.append(word)
    return result

print(split_at_a("eggplant"))
print(split_at_a("temo da luka"))
print(split_at_a("temo luka da dachi")) 