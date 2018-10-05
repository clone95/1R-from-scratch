

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


def max_occ_per_val (ditt):

    max_per_val_attr = max(ditt, key=ditt.get)
    return max_per_val_attr


def attrib_error(values_dict, solo_values, attrib):
    total_attrib_error = 0
    values_errors = []
#    for i in solo_values[attrib]:
 #       for el in range(0, len(values_dict[attrib])):
  #          err = 0
   #         piu_freq = max(values_dict[attrib], key=values_dict[attrib].count)
    #        print(piu_freq)
     #       values_errors.append(err)


    return total_attrib_error


def main():

    total_error = dict()
    values_dict = values_to_dictionary('lenses.txt')
    target_col = values_dict.__getitem__("lenses_target")
    values_dict.__delitem__("lenses_target")
    single_values_dict = dict()

    for code in range(1, 5):
        attribs = multi_labeler(values_dict, code, "myope", "hypermetrope", "non astigmatic", "astigmatic", "normal", "reduced")

    solo_values_set = different_values(attribs)

    for key in (values_dict.keys()):
        single_values_dict[key] = set(values_dict[key])

    for attrib in single_values_dict:
        total_error[attrib] = 0
        total_error[attrib] = attrib_error(values_dict, single_values_dict, attrib)

    # print(total_error)


main()
