from os import write

from PIL.DdsImagePlugin import item1

input_text_file = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/Abbildungen/Chimera/Flya_24_sec_struc.txt"
output_text_file = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/Abbildungen/Chimera/Flya_24_sec_struc_chimera.txt"
header = "\nattribute: talos\nrecipient: residues\n"

def add_initial_tabstop():

    with open(input_text_file) as input_file:
        initial_list = input_file.readlines()

    new_list = ["\t" + item for item in initial_list]

    return new_list

def write_result_file(chimera_list):

    new_file = header

    for item in chimera_list:
        new_file += item

    return new_file

chimera_list = add_initial_tabstop()
new_file = write_result_file(chimera_list)
#print(new_file)

with open(output_text_file, "w") as output_file:
    output_file.write(new_file)

