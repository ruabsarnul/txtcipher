def caesercyper_fun(inputTxt, step):
    chiper = []
    output = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for datum in inputTxt:
        if datum in uppercase:
        
         indexx = uppercase.index(datum);
        #  print(f"Index:", indexx)
         chiperIndx = (indexx + step)%26 #### 26 change the index position....
        #  print(f"cipher alphabet:", cyperIndx)
         chiper.append(chiperIndx)
        #  print(chiper);
         newLatter = uppercase[chiperIndx]
         output.append(newLatter)
        #  print(output)
        elif datum in lowercase:
          indexx =lowercase.index(datum)
          chiperIndexForLowerCase = (indexx + step)%26
          chiper.append(chiperIndexForLowerCase)
          newLatterForLowerCase = lowercase[chiperIndexForLowerCase]
          output.append(newLatterForLowerCase)
          print(output)
          return output
    # print("Test the fun")
    for i in output:
             print(i)
caesercyper_fun("ABC", 2)
   
    
    
    
    
# print("Test the py script")