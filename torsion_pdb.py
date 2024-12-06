########################################################################################################################

# transforms the torsion angles from Chimera output files to csv for easier import into Excel (remove header first)
# Chimera -> Render by Attribute -> Residue -> Phi / Psi -> File -> Save Attributes

########################################################################################################################

phi_filepath = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/PDB Torsion angle/phi"
psi_filepath = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/PDB Torsion angle/psi"
result_filepath_phi = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/PDB Torsion angle/phi.csv"
result_filepath_psi = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/PDB Torsion angle/psi.csv"

########################################################################################################################


def process_file(filepath, resultpath):

    with open(filepath) as file:
        list = file.readlines()

    stripped_list = [item.strip().split("\t") for item in list]

    new_file = ""
    for item in stripped_list:
        new_line = f"{item[0]},{item[1]}\n"
        new_file += new_line

    with open(resultpath, mode="w") as result_file:
        result_file.write(new_file)

process_file(filepath=phi_filepath, resultpath=result_filepath_phi)
process_file(filepath=psi_filepath, resultpath=result_filepath_psi)

