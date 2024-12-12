from amino_acids import one_letter

########################################################################################################################

# creates files that can be read by TALOS-N from Flya output files. You need the flya.tab file and the sequence.seq
# file for this to work

########################################################################################################################

flya_prot_filepath = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/FLYA Ergebnisse/Flya_run_23_shiftassign_fix/flya.prot"
flya_sequence_file = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/FLYA Ergebnisse/Flya_run_23_shiftassign_fix/sequence.seq"
talos_filepath = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/TALOS-N/Flya_run_23/talos_23.tab"

########################################################################################################################


def process_prot_file():

    with open(flya_prot_filepath) as flya_file:
        flya_data = flya_file.readlines()

    flya_lists = [entry.split() for entry in flya_data]

    return flya_lists


def process_sequence():

    with open(flya_sequence_file) as seq_file:
        sequence = seq_file.readlines()
        sequence_lists = [entry.split() for entry in sequence]
        sequence_dict = {entry[1]:entry[0] for entry in sequence_lists}
        sequence_dict_one_letter = {number:one_letter[name.lower()] for number, name in sequence_dict.items()}

        sequence_header = [name for number, name in sequence_dict_one_letter.items()]
        sequence_string = "".join(sequence_header)

        first_id = sequence_lists[0][1]

        return [sequence_dict_one_letter, sequence_string, first_id]


def create_full_list():

    flya_list = process_prot_file()
    sequence = process_sequence()[0]

    full_list = [[entry[4], sequence[entry[4]], entry[3], entry[1]] for entry in flya_list]

    return full_list


def create_result_file():

    processed_sequence = process_sequence()
    full_list = create_full_list()
    first_id = processed_sequence[2]
    header = (f"DATA FIRST_RESID {first_id}\nDATA SEQUENCE {processed_sequence[1]}\n"
              f"VARS   RESID RESNAME ATOMNAME SHIFT\nFORMAT %4d   %1s     %4s      %8.3f\n")

    new_file = ""
    new_file += header

    for entry in full_list:
        new_line = f"{entry[0]}\t{entry[1]}\t{entry[2]}\t{entry[3]}\n"
        new_file += new_line

    return new_file



result_file = create_result_file()
print(result_file)

with open(talos_filepath, mode="w") as talos_file:
    talos_file.write(result_file)






