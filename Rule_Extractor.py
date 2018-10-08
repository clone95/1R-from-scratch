# THE CODE IS SO MUCH COMMENTED BECAUSE IT'S A PROJECT FOR THE UNIVERSITY SO I NEED TO EXPLAIN WELL MY IMPLEMENTATION CHOICES.  

from Functions import  *


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
        print("(1) young, (2) pre-presbyopic, (3) presbyopic")
        printer(age, best_predictor, dict_list, errors_dict["age"])
    elif best_predictor == "prescription":
        print("(1) myope, (2) hypermetrope")
        printer(prescription, best_predictor, dict_list, errors_dict["prescription"])
    elif best_predictor == "astigmatism":
        print("(1) no, (2) yes")
        printer(astigmatism, best_predictor, dict_list, errors_dict["astigmatism"])
    else:
        print("(1) reduced, (2) normal\n")
        printer(tear_rate, best_predictor, dict_list, errors_dict["tear_production"])


main()
