
primo = "a"
secondo = "b"
terzo = "c"



def max_occ_per_val(ditt):

    max_per_val_attr = max(ditt, key=ditt.get)
    return max_per_val_attr

attribute = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
target = ["primo", "primo", "primo", "primo", "secondo", "secondo", "secondo", "terzo", "terzo", "terzo", "terzo"]
#b = ["secondo", "secondo", "secondo", "secondo", "primo", "primo", "primo", "terzo", "terzo", "terzo", "terzo"]
set_a = set(attribute)
target = ["a", "a", "a", "a", "b", "b", "b", "c", "c", "c", "c"]
set_b = set(target)

conversion = dict()
n = 1
list_input = []
for el in set_b:
    conversion[el] = n
    list_input.append(n)
    n += 1

print(list_input)


def total_error(list, attribute, target):

    max_dict = dict()
    errors = dict()
    input_v = [0, 1, 2, 3]
    for value in list:
        ditt = dict()

        for el in set(target):       # initialized ditt
            ditt[el] = 0

        for el in range(0, len(attribute)):

            if attribute[el] == value and target[el] == primo:
                ditt[target[el]] += 1

            elif attribute[el] == value and target[el] == secondo:
                ditt[target[el]] += 1

            elif attribute[el] == value and target[el] == terzo:
                ditt[target[el]] += 1

            max_dict[value] = max_occ_per_val(ditt)     # finds the most frequent value, per attrib_value

        # print(value, ditt)

        errors[value] = 1 - (ditt[max_dict[value]] / attribute.count(input_v[value]))

        # print(ditt[max_dict[value]], " -- associazioni corrette")
        # print(b.count(attr[value]),  " quante volte compare nel target il valore")
        # print(max_dict[value])
        # print(ditt[max_dict[value]], "/")
        # print(a.count(input[value]))
        # print("--------------")

    total_error = 0
    for err in errors:
        total_error += errors[err]
    return total_error      # each attrib value with his most frequent target value



print(total_error(list_input, attribute, target))




