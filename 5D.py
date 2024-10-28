import pandas
import decimal

#File paths for peak lists, CCPN-part as .csv file and list part as .list file
ccpn_csv_path = "/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/peaklists/HNcoCANH_700/HNcoCANH_less_peaks.csv"
list_file_path = "/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/peaklists/HNcoCANH_700/hCANH-700.list"

#file path for the resulting .peaks file
result_path = "/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/peaklists/HNcoCANH_700/HNcoCANH-700_less_peaks.peaks"

#columns following the data in the .peaks file
other_columns = "1\tU\t1\t1\te\t0\t0\t0\t0\t0\t0\t0"

#header of the resulting .peaks file
header = ("#\tNumber\tof\tdimensions\t5\n"
          "#FORMAT xeasy5D\n"
          "#INAME\t1\tCA\n"
          "#INAME\t3\tN1\n"
          "#INAME\t3\tH1\n"
          "#INAME\t4\tH2\n"
          "#INAME\t5\tN2\n"
          "#SPECTRUM HNcoCANH_5D CA N2 H2 H1 N1\n")


#returns number with exactly 3 decimal points as string
def create_three_decimals(number: str):
    number_decimal = decimal.Decimal(number).as_tuple().exponent * -1

    if number[-1] != "." and number_decimal == 0:
        number += ".000"

    else:
        while number_decimal < 3:
            number = number.ljust(len(number) + 1, "0")
            number_decimal = decimal.Decimal(number).as_tuple().exponent * -1

    return number


#returns list with first item being the plane number and the second and third item being the chemical shifts from CCPN .csv file
def process_ccpn_list():
    hn = pandas.read_csv(ccpn_csv_path)
    hn_data = (hn[["Pos F3", "Pos F2", "Pos F1"]]).sort_values("Pos F3")
    hn_data["Pos F3"] = hn_data["Pos F3"].round()

    hn_data_list = [[
        int(series.iloc[0]),
        round(float(series.iloc[1]), 3),
        round(float(series.iloc[2]), 3)] for (index, series) in hn_data.iterrows()]

    final_ccpn_data_list = []
    for entry in hn_data_list:
        new_entry = [entry[0]]
        for item in entry[1:]:
            new_item = create_three_decimals(str(item))
            new_entry.append(new_item)

        final_ccpn_data_list.append(new_entry)

    return final_ccpn_data_list


#returns dictionary with index(plane number) as key and list of chemical shifts as value from .list file
def process_list_file():
    with open(list_file_path) as canh_data:
        canh = canh_data.readlines()
    canh_list = [item.split("\t") for item in canh]
    canh_list_clean = [[
        round(float(item[1]), 3),
        round(float(item[2]), 3),
        round(float(item[3]), 3)] for item in canh_list]

    final_list_list = []
    for entry in canh_list_clean:
        new_entry = []
        for item in entry:
            new_item = create_three_decimals(str(item))
            new_entry.append(new_item)

        final_list_list.append(new_entry)

    canh_list_index = []
    i = 1
    for item in final_list_list:
        item.insert(0,i)
        canh_list_index.append(item)
        i += 1

    canh_dict = {item[0]:[item[1], item[2], item[3]] for item in canh_list_index}

    return canh_dict



hn_data = process_ccpn_list()
canh_data = process_list_file()


results = ""
counter = 1

#construct lines of result file from hn_data and canh_data
for shift in hn_data:
    new_line = (
        f"{counter}\t"
        f"{canh_data[shift[0]][0]}\t"
        f"{canh_data[shift[0]][1]}\t"
        f"{canh_data[shift[0]][2]}\t"
        f"{shift[1]}\t"
        f"{shift[2]}\t"
        f"{other_columns}\n"
        )

    results = results + new_line
    counter += 1


final_result = header + results

#print final result to console
print(final_result)

#write final peak list including header to .peaks file
# with open(result_path, "w") as result_file:
#     result_file.write(final_result)







