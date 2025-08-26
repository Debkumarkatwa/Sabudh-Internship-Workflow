def roman_to_int(s: str) -> int:
    d = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
        }   # dictionary to store the integer values

    result = 0   # to store the integer value
    flag = 0     # to track if the last value is special case or not (like IV, IX, XL, XC, CD, CM)

    data = [d[i] for i in s]  # converting the roman numeral to integer values and storing in a list
    
    for i in range(len(data)):
        if flag == 1:   # if last value is special case then skip it and reset the flag
            flag = 0
            continue
            
        if i == len(data)-1:   
            result +=data[i] # if it is the last value then add it to result and continue else it will give index error as we check i+1 in next step
            
        else:
            if data[i] < data[i+1]: # if current value is less than next value then it is a special case 
                result += (data[i+1] - data[i])  # so we subtract current value from next value and add it to result
                flag = 1  # also set the flag to 1 to skip the next value as it is already added
            else:
                result += data[i]       # else simply add the current value to result
        
    
    return result
    

print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))