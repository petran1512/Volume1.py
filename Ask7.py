7)
# s = result = s.title()
# s = input("Wright a sentence:")
# s = s[0].lower() + s[1:-1].upper() + s[-1].lower()
# print(s)

# 7) Given a random sentence, lowercase the first and last character of each word and uppercase all other characters of the word.
# For example: “hELLo wORLd”, “wELCOMe to tHe dESSERt of tHe rEAl”


def cap(sent):
    final = ""
    for w in sent.split():
        final += w[0].lower() + w[1:-1].upper() + w[-1].lower() + " "
    return final[:-1]


sent = input("Wright a sentence:")
final = cap(sent)
print(final)