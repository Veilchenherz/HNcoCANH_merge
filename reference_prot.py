

poky_output_file_path = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/p38_reference_prot/p_38_new_ref/p38_solids_only_with_ps6D_neu"


def process_poky_output():

    with open(file=poky_output_file_path) as poky_file:
        poky_data = poky_file.readlines()

    poky_data_list = [line.split() for line in poky_data]

    cleaned_list = []

    for item in poky_data_list:
        del item[4]
        amino_acid = list(item[0])
        item.append(amino_acid[0])
        del amino_acid[0]
        "".join()





    print(poky_data_list)

process_poky_output()