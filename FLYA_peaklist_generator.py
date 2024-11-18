import pandas
import decimal
import headers


#number of dimensions (can be 2,3,4) and name of the dimensions (for creating the header of the .peaks file)
dimensions = 4
dim1_name = "HN"
dim2_name = "N"
dim3_name = "C"
dim4_name = "CA"

#name of the spectrum according to FLYA library or LinserSolids.lib etc
spectrum_name = "shCACONH"

#name of the peak list file (without .csv extension)
peak_list_name = "CACONH"

#path of the directory, where the peak list is located
peak_list_directory = "example/example"


########################################################################################################################


#file path for peak list from CCPN as .csv file
peak_list_path = f"{peak_list_directory}/{peak_list_name}.csv"

#file path for the resulting .peaks file
result_path = f"{peak_list_directory}/{peak_list_name}.peaks"


#columns following the data in the .peaks file
zero_column = "\t0"
other_columns = f"1\tU\t1\t1\te{(dimensions + 1) * zero_column}"

#returns number with exactly 3 decimal places as string
def create_three_decimals(number: str):
    number_decimal = decimal.Decimal(number).as_tuple().exponent * -1

    if number[-1] != "." and number_decimal == 0:
        number += ".000"

    else:
        while number_decimal < 3:
            number = number.ljust(len(number) + 1, "0")
            number_decimal = decimal.Decimal(number).as_tuple().exponent * -1

    return number


#returns list with first item being the peak number and the others being chemical shifts from CCPN .csv file
def process_list():
    data = pandas.read_csv(peak_list_path)

    if dimensions == 2:
        shift_data = data[["#", "Pos F1", "Pos F2"]]
        data_list = [[
            int(series.iloc[0]),
            round(float(series.iloc[1]), 3),
            round(float(series.iloc[2]), 3)] for (index, series) in shift_data.iterrows()]
    elif dimensions == 3:
        shift_data = data[["#", "Pos F1", "Pos F2", "Pos F3"]]
        data_list = [[
            int(series.iloc[0]),
            round(float(series.iloc[1]), 3),
            round(float(series.iloc[2]), 3),
            round(float(series.iloc[3]), 3)] for (index, series) in shift_data.iterrows()]
    elif dimensions == 4:
        shift_data = data[["#", "Pos F1", "Pos F2", "Pos F3", "Pos F4"]]
        data_list = [[
            int(series.iloc[0]),
            round(float(series.iloc[1]), 3),
            round(float(series.iloc[2]), 3),
            round(float(series.iloc[3]), 3),
            round(float(series.iloc[4]), 3)] for (index, series) in shift_data.iterrows()]
    else:
        raise ValueError("Wrong number of dimensions!")

    final_data_list = []
    for entry in data_list:
        new_entry = [entry[0]]
        for item in entry[1:]:
            new_item = create_three_decimals(str(item))
            new_entry.append(new_item)

        final_data_list.append(new_entry)



    return final_data_list


spectrum_data = process_list()

results = ""

#construct lines of result file from spectrum_data
for shift in spectrum_data:
    new_line = ""
    new_line += f"{shift[0]}\t"
    for item in range(1, dimensions + 1):
        new_item = f"{shift[item]}\t"
        new_line += new_item
    new_line += f"{other_columns}\n"

    results += new_line


headers = headers.Headers(
    dimensions=dimensions,
    spectrum_name=spectrum_name,
    dim1=dim1_name,
    dim2=dim2_name,
    dim3=dim3_name,
    dim4=dim4_name
)

#creates the header for the .peaks file from the spectrum name and dimensions
header = headers.create_header()


final_result = header + results

#print final result to console
#print(final_result)

#write final peak list including header to .peaks file
with open(result_path, "w") as result_file:
    result_file.write(final_result)
