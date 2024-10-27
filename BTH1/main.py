# # Bai 1
# n = int(input("n = "))
# print(("*"*n+"\n")*n)
# for i in range(1, n+1):
#     print("*"*i)
# for i in range(1, n+1):
#     print(" "*(n-i)+"*"*i)
# for i in range(1, n+1, 2):
#     print(("*" * i).center(n))
# # Bai 2

# n = int(input("n = "))
# # (Cach 1)
# a = []  # list
# for i in range(n):
#   a.append(int(input(f"a[{i}] = ")))
# print(a)
#
# # (Cach 2)
# a = [int(input(f"a[{i}] = ")) for i in range(n)]
# print(a)
# d = [x for x in a if x > 0]
# print("So duong lon nhat : ", max(d) if len(a)>0 else "*")
# e = [x for x in a if x < 0]
# print("So am be nhat : ", min(d) if len(a)>0 else "*")
#
# for x in set(a): # set la tap hop (ko trung lap)
#     print(f"{x} xuat hien {a.count(x)} lan")
#
# a.sort(reverse=True)
# print(a)

# # Bai 3
words = {
    "sadness": "noi buon",
    "rain": "mua",
    "cat": "meo",
    "heart": "trai tim",
    "winter": "mua dong"
}
# words[rain] = "mua"

def add_word(word, mean):
    if word not in words:
        words[word] = mean


def delete_word(word):
    if word in words:
        # words.pop(word)
        del words[word]


def display():
    for k, v in words.items():
        print(f"{k} -> {v}")


def find_word(word):
    if word in words:
        print(f"{word} -> {words[word]}")
    else:
        print("Khong tim thay.")


if __name__ == '__main__':
    add_word("tear", "nuoc mat")
    add_word(mean="lanh", word="cold")
    delete_word("cold")
    display()
    find_word("sadness")
