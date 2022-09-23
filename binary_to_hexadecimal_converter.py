# -*- coding: utf-8 -*-
"""
@author: Burak Alanyalıoğlu
GitHub: @felsefesinde
Instagram: @felsefesinde
YouTube: Felsefesinde
Twitter: @felsefesinde & @binichburak
"""

def binary_to_hexadec(num):  
    """
    

    Parameters
    ----------
    num : string
        This is a binary (base-2) string of any number.

    Returns
    -------
    result : string
        This is a decimal (base-10) conversion of the input.

    """
    
    result = ""
    mapping = {"0": "0000",
               "1": "0001",
               "2": "0010",
               "3": "0011",
               "4": "0100",
               "5": "0101",
               "6": "0110",
               "7": "0111",
               "8": "1000",
               "9": "1001",
               "A": "1010", 
               "B": "1011", 
               "C": "1100", 
               "D": "1101", 
               "E": "1110", 
               "F": "1111"}

    radix = len(str(int(float(num))))
    
    if radix % 4 != 0:
        num = ("0" * (4 - (radix % 4))) + num

    for i in range (radix + 1, -1, -4):
        for keys in mapping:
            if mapping[keys] == num[i : i + 4]:
                result = keys + result
    try:
        num = int(num)
        return result
        
    except:
        result += "."
        num = num[radix + 2 : ]
        if len(num) % 4 != 0:
            num += ("0" * (4 - (len(num) % 4)))
        
        for i in range (0, len(num), 4):
            for keys in mapping:
                if mapping[keys] == num[i : i + 4]:
                    result += keys
        return result
        
#SAMPLE RUN FOR THE PROGRAM THAT DISPLAYS "467.CA88" AS THE RESULT WHICH IS CORRECT.     
print(binary_to_hexadec("10001100111.11001010100010"))
                
        
    
    
