import random
n = int(input("please entre  number of rows: "))
m = int(input("please entre number of columns: "))
def create_matrix(rows, columns):
    zakarya = []
    for i in range(0, rows):
        inner_list = []
        for j in range(0, columns):
            inner_list.append(round(random.uniform(-10, 10), 2))
        zakarya.append(inner_list)
    return zakarya
def spec_subtract(zakarya):
    for i in range(0, len(zakarya) - 1):
        for j in range(0, len(zakarya[i])):
            zakarya[i][j] = zakarya[i][j] - zakarya[len(zakarya) - 1][j]
    return zakarya
def print_matrix(zakarya):
    print("\n".join(["".join([" {:.2f}".format(item) for item in row]) for row in zakarya]))
zakarya_ = create_matrix(n, m)
print_matrix(zakarya_)
zakarya_ = spec_subtract(zakarya=zakarya_)
print_matrix(zakarya_)