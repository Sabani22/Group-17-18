def send_love_letter(name):
    letter = (
        "My dearest, \n\n"
        "From the moment I saw you, my world changed forever. Your smile lights up the darkest days, "
        "and your kindness brings warmth to every heart you touch. There are no words that can truly express "
        "how much you mean to me, but I will spend every day trying. You are my inspiration, my joy, and my everything.\n\n"
        f"With love to {name}"
    )
    return letter

# Example usage:
love_letter = send_love_letter("Emily")
print(love_letter)
