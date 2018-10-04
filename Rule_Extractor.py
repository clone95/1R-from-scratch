

def matrix_to_csv(file):
    file = open(file)
    output = open ("output.csv", "w")
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

    # print(values_dict["age"])

    return values_dict


def different_values(list):
    values = []
    for el in list:
        values.append(set(list[el]))
    return values


def main():

    values_dict = values_to_dictionary('lenses.txt')
    target_col = values_dict.__getitem__("lenses_target")
    values_dict.__delitem__("lenses_target")


    for code in range(1, 5):
        print("hello")
        attribs = multi_labeler(values_dict, code, "myope", "hypermetrope", "non astigmatic", "astigmatic", "normal", "reduced")

    solo_values = different_values(attribs)

    print(attribs)

main()
