data_dict = {
    "name" : "chandra" , 
    "course" : ["data science" , "ML" , "AI" , "MLOPS"] ,
    "greeting" : "welocome message from chandra !!"
}

def get_name():
    """
    This function returns the name of the course holder
    """
    return data_dict.get("name")
    
def get_course():
    """
    This function returns the courses enrolled by the user
    """
    return data_dict.get("course")
    
def greeting_msg():
    """
    This function greets
    """
    return data_dict.get("greeting")


"""
1. Create a class for dictionary parsing
a. WAF to return all the keys.
b. WAF to return all the values.
c. WAF to take key and value pair from user to add in dictionary.
d. WAF to take DICT from user as an input and parse that dictionary.
e. WAF to throw/raise an exception if i/p is not a dictionary.
"""

class dict_parser :

    # class properties
    dict_obj : dict = {}

    #while creating an object, the user has to pass a dictionary
    def __init__(self , dict1:dict):
        self.dict_obj = dict1


    # a
    def getKeys(self):
        """
        This is a function to return all the keys
        """
        # self.getValues() to call function inside another function.
        return self.dict_obj.keys()

    # b
    def getValues(self):
        """
        This is a function to return all the values
        """
        return self.dict_obj.values()

    # c
    def add(self , key , value):
        """
        This is a function to add the value to the dictionary and return the new dictionary
        """
        self.dict_obj[key] = value
        return self.dict_obj

    # d , e
    def parseUserDict(self , user_dict : dict):
        """
        take DICT from the user as an input and parse that dictionary. throw/raise an exception if i/p is not a dictionary.
        """
        if type(user_dict) != dict:
            raise ValueError("User dictionary is not a dictionary" , user_dict)
        else :
            print("User dictionary is valid")
            print("Keys :" , user_dict.keys())
            print("Values :" , user_dict.values())

    
