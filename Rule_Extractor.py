

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


def values_to_dictionary(file):

    values_dict = dict()
    values_dict.__setitem__("age", [])
    values_dict.__setitem__("spectacle_prescription", [])
    values_dict.__setitem__("astigmatic", [])
    values_dict.__setitem__("tpr", [])
    values_dict.__setitem__("lenses_target", [])

    file = open(file)

    for line in file:
        values_dict["age"].append(int(line.split()[0]))
        values_dict["spectacle_prescription"].append(int(line.split()[0]))
        values_dict["astigmatic"].append(int(line.split()[0]))
        values_dict["tpr"].append(int(line.split()[0]))
        values_dict["lenses_target"].append(int(line.split()[0]))

    # print(values_dict["age"])


def main():

    values_to_dictionary('lenses.txt')


main()
