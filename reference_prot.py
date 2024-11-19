poky_output_file_path = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/p38_reference_prot/p_38_new_ref/p38_solids_only_with_ps6D_neu"
amino_acid_number_shift = 0


def process_poky_output():

    with open(file=poky_output_file_path) as poky_file:
        poky_data = poky_file.readlines()

    poky_data_list = [line.split() for line in poky_data]
    cleaned_list = []

#split residue number and name into two list entries (e.g. ['E14'] -> ['E', '14'])
#correct number of amino acid by the specified "amino_acid_number_shift"

    for item in poky_data_list:
        del item[4]
        amino_acid = list(item[0])
        item.append(amino_acid[0])
        del amino_acid[0]
        amino_acid_number = int("".join(amino_acid)) + amino_acid_number_shift
        amino_acid_number_str = str(amino_acid_number)
        del item[0]
        item.append(amino_acid_number_str)
        cleaned_list.append(item)



#create lines of result file from cleaned_list
    result = ""
    for entry in cleaned_list:
        new_line = f"{cleaned_list.index(entry) + 1}\t{entry[2]}\t{entry[3]}\t{entry[0]}\t{entry[5]}\n"
        result += new_line

    return result



final_result = process_poky_output()

print(final_result)