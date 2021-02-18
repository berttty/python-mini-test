import json
import glob
import pandas as pd

# get the columns in some order predefined to dont swap values
cols = ['ac_realpower', 'apparent_power', 'day_yield', 'dc_inc_volt_A', 'dc_input', 'grid_current_ampere', 'grid_freq', 'grid_phase_A', 'grid_phase_B', 'grid_phase_C', 'reactive_power', 'yield_total']

# get a json inside of str and create a list using the cols variable to extract the values
def jsonStr2col(json_str):
    data = json.loads(json_str)
    row = []
    for name_col in cols:
        row.append( data[name_col] )
    return row

# Read all the file in the folder
l = [pd.read_csv(filename, header=None) for filename in glob.glob("input/*.csv")]
origin = pd.concat(l, axis=0)
origin.reset_index(drop=True, inplace=True)

#convert the list obtained from the json to a new dataframe
json_part = pd.DataFrame([x for x in origin[5].apply(jsonStr2col).values], columns=cols)

#concatenate the two dataframes over one
full_csv= pd.concat([origin.drop(5, axis=1), json_part], axis=1)

full_csv.to_csv("output.csv", index=False)

