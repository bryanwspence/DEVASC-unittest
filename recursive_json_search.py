
from test_data import *


# recursive_json_search.py
ret_val=[]
def json_search(key,input_object):

    if isinstance(input_object, dict): # Handle dict
        for k, v in input_object.items(): # searching key in the dic
            if k == key:
                temp={k:v}
                ret_val.append(temp)
            if isinstance(v, dict): # the value is another dict so repeat
                json_search(key,v)
            elif isinstance(v, list): # it's a list
                for item in v:
                    if not isinstance(item, (str,int)): # but could be a dict or list so repeat
                        json_search(key,item)
    else: # handle a list, some APIs return JSON object in a list
        for val in input_object:
            if not isinstance(val, (str,int)):
                json_search(key,val)
    return ret_val
print (json_search("issueSummary",data))

# Replaces function in recursive_json_search.py
def json_search(key,input_object):
    """
    Search a key from JSON object, get nothing back if key is not found
    key : keyword to be searched, case sensitive
    input_object : JSON object to be parsed
    inner_function() is actually doing the job
    return a list of key:value pair
    """
    ret_val=[]
    def inner_function(key,input_object):
        if isinstance(input_object, dict): # Handle dict
            for k, v in input_object.items():
                if k == key:
                    temp={k:v}
                    ret_val.append(temp)
                if isinstance(v, dict):
                    inner_function(key,v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str,int)):
                            inner_function(key,item)
        else: # handle a list, some APIs return JSON object in a list
            for val in input_object:
                if not isinstance(val, (str,int)):
                    inner_function(key,val)

    inner_function(key,input_object)
    return ret_val
