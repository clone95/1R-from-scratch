def max_occ_per_val(ditt):

    max_per_val_attr = max(ditt, key=ditt.get)
    return max_per_val_attr


def matrix_to_csv(file):
    file = open(file)
    output = open("output.csv", "w")
    output.write("age,sp,ast,tpr,lens\n")
    for line in file:
        output.write(line.split()[1])
        output.write(",")
        output.write(line.split()[2])
        output.write(",")
        output.write(line.split()[3])
        output.write(",")
        output.write(line.split()[4])
        output.write(",")
        output.write(line.split()[5])
        output.write("\n")


def labeler(v1, v2, val_dict, string):
    for i in range(0, len(val_dict[string])):
        if val_dict[string][i] == 1:
            val_dict[string][i] = v1
        else: val_dict[string][i] = v2
    return val_dict


def multi_labeler(val_dict, code, v1, v2, v3 ,v4, v5 ,v6):

    if code == 1:
        for i in range(0, len(val_dict["age"])):
            if val_dict["age"][i] == 1:
                val_dict["age"][i] = "young"
            elif val_dict["age"][i] == 2:
                val_dict["age"][i] = "pre-presbyopic"
            else:
                val_dict["age"][i] = "presbyopic"
        return val_dict

    if code == 2:
        labeler(v1, v2, val_dict, "prescription")

    if code == 3:
        labeler(v3, v4, val_dict, "astigmatism")

    if code == 4:
        labeler(v6, v5, val_dict, "tear_production")

    return val_dict


def values_to_dictionary(file):

    values_dict = dict()
    columns = ["age", "prescription", "astigmatism", "tear_production", "lenses_target"]
    for col in columns:
        values_dict.__setitem__(col, [])

    file = open(file)

    for line in file:
        values_dict["age"].append(int(line.split()[0]))
        values_dict["prescription"].append(int(line.split()[1]))
        values_dict["astigmatism"].append(int(line.split()[2]))
        values_dict["tear_production"].append(int(line.split()[3]))
        values_dict["lenses_target"].append(int(line.split()[4]))

    return values_dict


def different_values(lista):
    values = []
    for el in lista:
        values.append(set(lista[el]))
    return values


def max_occ_per_val(ditt):
    max_per_val_attr = max(ditt, key=ditt.get)
    return max_per_val_attr


def total_error(lista, attribute, target):
    target_list = list(set(target))

    primo = target_list[2]
    secondo = target_list[1]
    terzo = target_list[0]
    attr = ["", primo, secondo, terzo]
    max_dict = dict()
    errors = dict()
    input_v = [0, 1, 2, 3]
    corrects = 0
    print(target_list)
    for value in lista:
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


        print(value, "----->", ditt)

        errors[value] = 1 - (ditt[max_dict[value]] / attribute.count(input_v[value]))


        corrects += max(ditt.values())




    print("corrects  ", corrects)
    print("remaining",len(target)-corrects)
    error = (len(target)- corrects)/len(target)
    print("______",error)
   # for err in errors:
    #    corrects += errors[err]


    return error      # each attrib value with his most frequent target value


def main():

    errors_dict = dict()
    values_dict = values_to_dictionary('lenses.txt')
    target_col = values_dict.__getitem__("lenses_target")
    values_dict.__delitem__("lenses_target")
    single_values_dict = dict()


    for code in range(1, 5):
        attribs = multi_labeler(values_dict, code, "myope", "hypermetrope", "non astigmatic", "astigmatic", "normal", "reduced")

    values_dict = values_to_dictionary('lenses.txt')
    for el in range(0, len(target_col)):
        if target_col[el] == 1:
            target_col[el] = "hard"
        elif target_col[el] == 2:
            target_col[el] = "soft"
        else: target_col[el] = "none"

    solo_values_set = different_values(attribs)

    for key in (values_dict.keys()):
        single_values_dict[key] = set(values_dict[key])
    values_dict.__delitem__("lenses_target")
    for key in values_dict:
        set_b = set(values_dict[key])
        conversion = dict()
        n = 1
        list_input = []

        for el in set_b:
            conversion[el] = n
            list_input.append(n)
            n += 1
        print(key)

        errors_dict[key] = total_error(list_input, values_dict[key], target_col)


    print(errors_dict)



main()
