# imports
import os
import csv
import sys

from grover.main import grover_predict

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))


# run model. No need to read the smiles from the input csv file, the model will read and return the smiles_list
outputs, smiles_list = grover_predict(input_txt_path=input_file, output_path=output_file)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(['u0_atom'])  # header
    for o in outputs:
        writer.writerow(o)