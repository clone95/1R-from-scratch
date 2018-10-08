# THE CODE IS SO MUCH COMMENTED BECAUSE IT'S A PROJECT FOR THE UNIVERSITY SO I NEED TO EXPLAIN WELL MY IMPLEMENTATION CHOICES.  

def max_occ_per_val(ditt):
    max_per_val_attr = max(ditt, key=ditt.get)
    return max_per_val_attr  # returns the most class value for a given attribute value.


def matrix_to_csv(file):  # returns a CSV file from the dataset got at UCI Repository
    file = open(file)
    output = open("output.csv", "w")
    output.write("age,sp,ast,tpr,lens\n")  # attribute names
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


def labeler(v1, v2, val_dict, string):  # labels a value of an attribute with a string
    for i in range(0, len(val_dict[string])):
        if val_dict[string][i] == 1:
            val_dict[string][i] = v1
        else:
            val_dict[string][i] = v2
    return val_dict


def multi_labeler(val_dict, code, v1, v2, v3, v4, v5, v6):  # labels all the dataset columns

    if code == 1:                                           # i need this function if we want the values in string form
        for i in range(0, len(val_dict["age"])):            # the dataset given by the UCI repo has values with INT
            if val_dict["age"][i] == 1:
                val_dict["age"][i] = "young"
            elif val_dict["age"][i] == 2:
                val_dict["age"][i] = "pre-presbyopic"
            else:
                val_dict["age"][i] = "presbyopic"
        return val_dict

    if code == 2:                                           # i have set some "launch code" to reuse this function
        labeler(v1, v2, val_dict, "prescription")           # in different cases

    if code == 3:
        labeler(v3, v4, val_dict, "astigmatism")

    if code == 4:
        labeler(v6, v5, val_dict, "tear_production")

    return val_dict


def values_to_dictionary(file):  # stores value into a dictionary for logical operations

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


def different_values(lista):  # assigns to each value of a given attribute ID for better handling the logic
    values = []
    for el in lista:
        values.append(set(lista[el]))
    return values


def max_occ_per_val(ditt):  # returns the most frequent class(target), for a given attribute VALUE
    max_per_val_attr = max(ditt, key=ditt.get)
    return max_per_val_attr


def get_occurrences(attribute, value, target, first, second, third, ditt, el):

        if attribute[el] == value and target[el] == first:
            ditt[target[el]] += 1

        elif attribute[el] == value and target[el] == second:
            ditt[target[el]] += 1

        elif attribute[el] == value and target[el] == third:
            ditt[target[el]] += 1


def total_error(attr_values_list, attribute, target, temp_dict, dict_list):  # return total error of given attribute

    target_list = list(set(target))      # make an iterable set of the values of the given attribute
    first = target_list[0]               # assign target values to variables
    second = target_list[1]
    third = target_list[2]
    max_dict = dict()                    # will host the "most hit class" for each value of the attribute
    errors = dict()
    input_v = [0, 1, 2, 3]
    corrects = 0                         # corrects prediction, after knowing the most frequent class
    for value in attr_values_list:       # for each value of the attribute e.g. [young, pre-presbyopic, presbyopic]...
        ditt = dict()

        for el in set(target):           # ditt is a support dict() for holding the count of
            ditt[el] = 0                 # the occurrences of each class, for each value.

        for el in range(0, len(attribute)):      # collects the occurrences of the target value for each attr value

            get_occurrences(attribute, value, target, first, second, third, ditt, el)

            max_dict[value] = max_occ_per_val(ditt)  # finds the most frequent value, per attrib_value

        print("attribute value encoded as ", value, "--->", ditt)  # prints the mapping of the value on the target class

        errors[value] = 1 - (ditt[max_dict[value]] / attribute.count(input_v[value]))  # error contribution

        corrects += max(ditt.values())  # errors sum. For example ...
        # ...an entire call of this function it sums the prediction error of young, pre-presbyopic and presbyopic values

        dict_list.append(ditt)         # i save the several occurrences over each attribute

    error = (len(target) - corrects) / len(target)

    print("right values :  ", corrects)
    print("wrong values :  ", len(target) - corrects, "\n")            # some output
    print("ATTRIBUTE ERROR  ---> ", error, "\n")
    print("_____________________________________\n\n")

    return error        # each attrib value with his prediction error


def printer(attribute):
    print("value : 1  ---> Lenses : ", max_occ_per_val(attribute[0]).upper())
    print("value : 2  ---> Lenses : ", max_occ_per_val(attribute[1]).upper())
    if len(attribute) == 3:
        print("value : 3  --->", attribute[1])


def main():

    errors_dict = dict()
    values_dict = values_to_dictionary('lenses.txt')                # imports values from file to dict()
    target_col = values_dict.__getitem__("lenses_target")           # copy the target column
    values_dict.__delitem__("lenses_target")                        # drop the target column from the attrib dict()
    single_values_dict = dict()
    best_dict = dict()
    temp_dict = dict()
    dict_list = []
    iter_dict = dict()
    a = 0
    for el in range(0, len(target_col)):                            # converts target values (INT) in the correct labels
        if target_col[el] == 1:
            target_col[el] = "hard"
        elif target_col[el] == 2:
            target_col[el] = "soft"
        else:
            target_col[el] = "none"

    for key in (values_dict.keys()):                                # takes distinct attribute values
        single_values_dict[key] = set(values_dict[key])

    for key in values_dict:
        iter_dict[key] = a
        set_b = set(values_dict[key])
        conversion = dict()
        n = 1
        list_input = []

        for el in set_b:
            conversion[el] = n
            list_input.append(n)
            n += 1
        a += 1
        print(key.upper(), "\n")                                 # which attribute am I studying in this iteration?

        errors_dict[key] = total_error(list_input, values_dict[key], target_col, temp_dict, dict_list)  # attr. error

    best_predictor = min(errors_dict, key=errors_dict.get)

    best_pred_list = list(set(values_dict[best_predictor]))

    for code in range(1, 5):
        attribs = multi_labeler(values_dict, code, "myope", "hypermetrope", "non astigmatic",
                                "astigmatic", "normal", "reduced")

    best_pred_values = list(set(attribs[best_predictor]))

    for i in range(0, len(best_pred_list)):
        best_dict[best_pred_list[i]] = best_pred_values[i]

    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

    print("CONCLUSIONS AND SUGGESTION FOR THE MEDKNOW TEAM:\n")
    print("The best predictor for the lenses type is the parameter", best_predictor.upper(), "\n")

    age = dict_list[:3]
    prescription = dict_list[3:5]
    astigmatism = dict_list[5:7]
    tear_rate = dict_list[7:]

    print("Suggestions for the lenses: \n")

    if best_predictor == "age":
        printer(age)
        print("(1) young, (2) pre-presbyopic, (3) presbyopic")
    elif best_predictor == "prescription":
        print("(1) myope, (2) hypermetrope")
        printer(prescription)
    elif best_predictor == "astigmatism":
        print("(1) no, (2) yes")
        printer(astigmatism)
    else:
        print("(1) reduced, (2) normal\n")
        printer(tear_rate)


main()
