import string

normal = string.ascii_lowercase
normal = [*normal]
# print(normal)

plain = "iini pllain teksss"
plain = plain.replace(" ", "")
plain = [*plain]
# print(plain)

# key = "notakeye"
# key = [*key]
# key = list(dict.fromkeys(key))
# print(key)

def pairplain(teks, step):
    if step not in [len(teks), len(teks)-1]:
        if teks[step] == teks[step + 1]:
            teks.insert(step+1, "x")
            pairplain(teks, step+2)
        else:
            pairplain(teks, step+2)
        print(teks)
        print(step)
    else:
        return teks
    

print(pairplain(plain,0))

