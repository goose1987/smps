import os
import re
mod_lines=[]


params={"RLOAD":1,"VIN":20} # parameters to update
netlist="buck.net" # netlist to edit
FET = "EPC2012C" # fet to test
with open(netlist,"r") as f:
    for line in f:

        if 'XSWMAIN' in line:# find line with X device with the correct name, if iterating over different fets
            line = re.sub(r'(\s)(\w+)$',"\g<1>"+FET,line) # replace the last word in the line as this specify the model
        if '.PARAM' in line:
            pId = re.search(r'\s*(\w+)\s*=',line).group(1) # find the parameter ID in the text line
            if pId in params.keys(): # if the param is in the keys list update the netlist, dont change parameters that are not in the dictionary
                line= re.sub("(\s"+pId+"\s*=)(.*)$","\g<1>"+str(params[pId]),line) # find and replace the parameter value, iterating over param values
        mod_lines.append(line)# reconstruct netlist
#print back updated netlist to file
with open(netlist,"w") as f:
    for m in mod_lines:
        f.write(m)

#os.system("xyce "+netlist)
