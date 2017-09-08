# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:42:20 2017

@author: jliu
"""

def parseString(string):
    """inputs: properly formatted string that specifies the base string
    and a list of strings. The base string and the list strings
    to be replaced are separated by a semicolon.
    
    returns: a tuple containing the base string and a list of strings
    
    Example:
        
        10011011001;0110,1001,1001,0,10,11
        
        returns (10011011001, [0110,1001,1001,0,10,11])
    """
    
    parsed_list = string.split(";")
    value_list = parsed_list[1].split(",")
    
#    find_replace_dict = {}
#    for i in range(int(len(value_list)/2)):
#        find_replace_dict[value_list[i*2]] = value_list[i*2+1]
    
    return parsed_list[0], value_list

def convertAB(string):
    """inputs: a string of 0's and 1's
    returns: a string of a's and b's where a's replace 0 and b's replace 1
    """
    ab_string = ""
    for char in string:
        if char == "0":
            ab_string = ab_string + "a"
        elif char == "1":
            ab_string = ab_string + "b"
    return ab_string

def revertAB(ab_string):
    """inputs: a string of a's, b's, 1's, and 0's
    returns: a string of 0's and 1's where 0's replace a and 1's replace b.
    Existing 1's and 0's in the input string are ignored
    """
    output_str = ""
    for char in ab_string:
        if char == "a":
            output_str = output_str + "0"
        elif char == "b":
            output_str = output_str + "1"
        else:
            output_str = output_str + char
    return output_str

####### main program #######

string = "10011011001;0110,1001,1001,0,10,11"
base, values = parseString(string)


for i in range(int(len(values)/2)):
    target = values[i*2]
    replacement = convertAB(values[i*2+1])
    if base.find(target) == -1:
        continue
    else:
        index = base.find(target)
        end_index = index + len(target)
        base = base[:index] + replacement + base[end_index:]

print(revertAB(base))











