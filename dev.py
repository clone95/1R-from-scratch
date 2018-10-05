



ditt = dict()


primo = "primo"
secondo = "secondo"
terzo = "terzo"
ditt[primo] = 0
ditt[secondo] = 0
ditt[terzo] = 0


def max_occ_per_val (ditt):

    max_per_val_attr = max(ditt, key=ditt.get)
    return max_per_val_attr

a = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
b = ["primo", "primo", "primo", "secondo", "secondo", "secondo", "secondo", "terzo", "primo", "terzo", "terzo"]
set_a = set(a)
def maxes(values):

    max_dict = dict()
    errors = dict()
    attr = ["", "primo", "secondo", "terzo"]
    for value in values:
        ditt = dict()
        for target in set(b):
            ditt[target] = 0

        for el in range(0, len(a)):
            if a[el] == value and b[el] == primo:
                ditt[b[el]] += 1
            elif a[el] == value and b[el] == secondo:
                ditt[b[el]] += 1
            elif a[el] == value and b[el] == terzo:
                ditt[b[el]] += 1

            max_dict[value] = max_occ_per_val(ditt)     # finds the most frequent value, per attrib_value

        # print(value, ditt)

        errors[value] = 1-(ditt[max_dict[value]]/b.count(attr[value]))
        print(ditt[max_dict[value]], " -- associazioni corrette")
        print(b.count(attr[value]),  " quante volte compare nel target il valore")

    return errors      # each attrib value with his most frequent target value


print(maxes([1, 2, 3]))




