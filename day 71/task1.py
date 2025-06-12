def capitalize(user):
    split_user = user.split()
    result = []
    for word in split_user:
        result.append(word.capitalize())
    return "".join(result)

print(capitalize('This is a really really really long sentence for goa')) 
