import json


def load_employees():
    with open("data/em.json", encoding='utf-8') as f:
        return json.load(f) # print thu


def display(data):
    for em in data: # 1 em = 1 dictionary trong list data
        for k, v in em.items():
            if k.__eq__("ma_nv"):
                print(f"Ma nhan vien: {v}")
            elif k.__eq__("ten_nv"):
                print(f"Ten nhan vien: {v}")


def add_em(data, ma_nv, ten_nv):
    em = {
        "ma_nv": ma_nv,
        "ten_nv": ten_nv
    }
    data.append(em)
    with open("data/em.json", mode="w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        # mode w la write, tat ascii, khoang cach = 4


def delete_em(data, id):
    for idx, em in enumerate(data): # tra ve 1 doi tuong ma moi phan tu cua no la 1 tuple chua 1 cap index, value
        if em["ma_nv"] == id:
            del data[idx]
    with open("data/em.json", mode="w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# def search(data, kw):
#     kq=[]
#     for em in data:
#         if em["ten_nv"].find(kw) >= 0:
#             kq.append(em)
#     return kq

def search(data, kw):
    return [em for em in data if em["ten_nv"].find(kw) >= 0]


if __name__ == '__main__':
    data = load_employees()
    add_em(data, ma_nv=99, ten_nv="Loc")
    display(data)
    print("===")
    kq = search(data, "Văn")
    display(kq)
    delete_em(data, 99)
