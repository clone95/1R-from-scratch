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


def add_record(new_record, lens):
    file = open("lenses.txt", "a")

    if new_record[0] == "young":
        age = '1'
    elif new_record[0] == "pre-presbyopic":
        age = '2'
    else:
        age = '3'

    if new_record[1] == "myope":
        dis = '1'
    else:
        dis = '2'

    if new_record[2] == "yes":
        ast = '1'
    else:
        ast = '2'

    if new_record[3] == "reduced":
        tpr = '1'
    else:
        tpr = '2'

    if lens == "hard":
        lenses = '1'
    elif lens == "soft":
        lenses = '2'
    else:
        lenses = '3'

    record = age + "  " + dis + "  " + ast + "  " + tpr + "  " + lenses
    file.write(record)


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
    print("ATTRIBUTE ERROR  ---> ", error, "")
    print("_____________________________________\n")

    return error        # each attrib value with his prediction error


def printer(attribute, predictor, list_dict, precision):
    print("value : 1  ---> Lenses : ", max_occ_per_val(attribute[0]).upper())
    print("value : 2  ---> Lenses : ", max_occ_per_val(attribute[1]).upper())
    if len(attribute) == 3:
        print("value : 3  --->", attribute[1])
    precision = 1 - precision
    print("\n\n|||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print("\n\nWelcome Medic : insert parameters of the patient")
    age = input("\nInsert the age :\n")
    disease = input("\nInsert the disease :\n")
    astigmatism = input("\n\Insert the astigmatism :   y  /  n\n")
    tear_rate = input("\nInsert the tear rate:\n\n")

    if predictor == "tear_production":
        if tear_rate == "reduced":
            best_value_occ = list_dict[7]
            shot = max(best_value_occ, key=best_value_occ.get)
            print("\n\n", best_value_occ)
            print("\nLENSES TYPE  :  ", shot)
            print("\nATTENTION: the precision of the system is ", precision)
            choice = input("\nCorrect prediction? press yes to insert record\n")
            new_record = [age, disease, astigmatism, tear_rate, shot]
            if choice == "yes":
                add_record(new_record, shot)
                print("Record added!")
            else:
                shot = input("which which lens is required is this case?\n")
                add_record(new_record, shot)
                print("Record added!")
        else:
            best_value_occ = list_dict[8]
            shot = max(best_value_occ, key=best_value_occ.get)
            print("\n\n", best_value_occ)
            print("\nLENSES TYPE  :  ", shot)
            print("\nATTENTION: the precision of the system is ", precision)
            choice = input("\nCorrect prediction? press yes to insert record")
            new_record = [age, disease, astigmatism, tear_rate, shot]
            if choice == "yes":
                add_record(new_record, shot)
                print("Record added!")

            else:
                shot = input("which which lens is required is this case?")
                add_record(new_record, shot)
                print("Record added!")









