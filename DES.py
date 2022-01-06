# this fn converts  from Bin num to hexadecimal numbers
def Bin_To_Hex_(s):
    mappng = {"0000" : '0', 
          "0001" : '1',
          "0010" : '2', 
          "0011" : '3',
          "0100" : '4',
          "0101" : '5', 
          "0110" : '6',
          "0111" : '7', 
          "1000" : '8',
          "1001" : '9', 
          "1010" : 'A',
          "1011" : 'B', 
          "1100" : 'C',
          "1101" : 'D', 
          "1110" : 'E',
          "1111" : 'F' }
    xHe2_ = ""
    for h in range(0,len(s),4):
        hc1 = ""
        hc1 = hc1 + s[h]
        hc1 = hc1 + s[h + 1] 
        hc1 = hc1 + s[h + 2] 
        hc1 = hc1+ s[h + 3] 
        xHe2_ = xHe2_ + mappng[hc1]
          
    return xHe2_

# this fn converts Hexadecinum to bin number
def Hex_To_Bin_(s):
    mappng = {'0' : "0000", 
          '1' : "0001",
          '2' : "0010", 
          '3' : "0011",
          '4' : "0100",
          '5' : "0101", 
          '6' : "0110",
          '7' : "0111", 
          '8' : "1000",
          '9' : "1001", 
          'A' : "1010",
          'B' : "1011", 
          'C' : "1100",
          'D' : "1101", 
          'E' : "1110",
          'F' : "1111" }
    n2ib_ = ""
    for j in range(len(s)):
        n2ib_ = n2ib_ + mappng[s[j]]
    return n2ib_
     #hexatobinary 


#bintohexa

# this fn converts Binary num to decimal number
def Bin_To_Dec_(_b2): 
        
    bi1ayrn = _b2 
    ce2d_, k, n = 0, 0, 0
    while(_b2 != 0): 
        c1ed = _b2 % 10
        _b2 = _b2//10
        ce2d_ = ce2d_ + c1ed * pow(2, k) 
        k += 1
    return ce2d_
 #bin to dec
  

  
# fn to Permute  i.e., permute function to rearrange the bits
def Muperte_(k, arr, n):
    Mupertitation_ = ""
    for j in range(0, n):
        Mupertitation_ += k[arr[j] - 1]
    return Mupertitation_
  
# this fn converts  Decimal num to _b2 number
def Dec_To_Bin_(num): 
    Resp_ = bin(num).replace("0b", "")
    if(len(Resp_)%4 != 0):
        quo_ = int(len(Resp_) / 4)
      
        quocount =(4 * (quo_ + 1)) - len(Resp_) 
        for k in range(0, quocount):
            Resp_ = '0' + Resp_
    return Resp_
#dec to bin  

# fn to shift the bits towards by nshifts up_
def Left_Shift(k, nth_shifts):
    t = ""
    for i in range(nth_shifts):
        for j in range(1,len(k)):
            t += k[j]
        t += k[0]
        k = t
        t = "" 
    return k    


# to calculate Xor of a & b i.e.,two bin numstrings
def Epr_(a, b):
    answer = ""
    for j in range(len(a)):
        if a[j] != b[j]:
            answer = answer + "1"
        else:
            answer = answer + "0"
    return answer
  
# Initial Permutation Table: below is the Table of Position of 64 bits at initi_ level
Initial_Perm_ = [58, 50, 42, 34, 26, 18, 10, 2, 
                60, 52, 44, 36, 28, 20, 12, 4, 
                62, 54, 46, 38, 30, 22, 14, 6, 
                64, 56, 48, 40, 32, 24, 16, 8, 
                57, 49, 41, 33, 25, 17, 9, 1, 
                59, 51, 43, 35, 27, 19, 11, 3, 
                61, 53, 45, 37, 29, 21, 13, 5, 
                63, 55, 47, 39, 31, 23, 15, 7] 
  
#  D-box Expansion   Table
D_box_Exp_ = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5, 
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 
         12, 13, 12, 13, 14, 15, 16, 17, 
         16, 17, 18, 19, 20, 21, 20, 21, 
         22, 23, 24, 25, 24, 25, 26, 27, 
         28, 29, 28, 29, 30, 31, 32, 1 ]
  
# given  straight permutaion Table 
Permute_Table_ = [ 16,  7, 20, 21,
        29, 12, 28, 17, 
         1, 15, 23, 26, 
         5, 18, 31, 10, 
         2,  8, 24, 14, 
        32, 27,  3,  9, 
        19, 13, 30,  6, 
        22, 11,  4, 25 ]
  
#  below is the S-box Table
S_Box_ =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
             
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], 
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]], 
    
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]], 
        
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ], 
         
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]], 
        
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ], 
          
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ], 
         
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]
    
# Final Permutaion Table
Final_Permute_table = [ 40, 8, 48, 16, 56, 24, 64, 32, 
               39, 7, 47, 15, 55, 23, 63, 31, 
               38, 6, 46, 14, 54, 22, 62, 30, 
               37, 5, 45, 13, 53, 21, 61, 29, 
               36, 4, 44, 12, 52, 20, 60, 28, 
               35, 3, 43, 11, 51, 19, 59, 27, 
               34, 2, 42, 10, 50, 18, 58, 26, 
               33, 1, 41, 9, 49, 17, 57, 25 ]

#  below is fn to desencryptinhex_ 
def desencryptinhex_(Plain_Text_, Round_Key_Binary_, Round_Key_in_Hex):
    Plain_Text_ = Hex_To_Bin_(Plain_Text_)
      
    # Initial Permutation
    Plain_Text_ = Muperte_(Plain_Text_, Initial_Perm_, 64)
    #print("After inital Mupertitation_", Bin_To_Hex_(Plain_Text_))
      
    # Splitting
    up_ = Plain_Text_[0:32]
    Down_ = Plain_Text_[32:64]
    for k in range(0, 16):
        #  Expansion D-box: Expanding the 32 bits data into 48 bits 
        Right_Expanded_ = Muperte_(Down_, D_box_Exp_, 48)
          
        # XOR RoundKey[i] and Right_Expanded_ 
        Xor_X_ = Epr_(Right_Expanded_, Round_Key_Binary_[k])
  
        # S-boxex: substituting the value from s-box table by calculating ro2w_ and column 
        S_Box_str_ = ""
        for j in range(0, 8):
            ro2w_ = Bin_To_Dec_(int(Xor_X_[j * 6] + Xor_X_[j * 6 + 5]))
            cl2o_ = Bin_To_Dec_(int(Xor_X_[j * 6 + 1] + Xor_X_[j * 6 + 2] + Xor_X_[j * 6 + 3] + Xor_X_[j * 6 + 4]))
            vl1a = S_Box_[j][ro2w_][cl2o_]
            S_Box_str_ = S_Box_str_ + Dec_To_Bin_(vl1a)
              
        # Straight D-box: After substituting rearranging the bits  
        S_Box_str_ = Muperte_(S_Box_str_, Permute_Table_, 32)
          
        # XOR up_ and S_Box_str_
        R_ul2et = Epr_(up_, S_Box_str_)
        up_ = R_ul2et
          
        # Swapper
        if(k != 15):
            up_, Down_ = Down_, up_ 
        #print("Round ", i + 1, " ", Bin_To_Hex_(up_), " ", Bin_To_Hex_(Down_), " ", Round_Key_in_Hex[i])
      
    # Combination
    Cmo2bn = up_ + Down_
      
    # Final permutaion: final rearranging of bits to get cipher text
    Cipher_Text_ = Muperte_(Cmo2bn, Final_Permute_table, 64)
    return Cipher_Text_

# Des encryption final fn of 16 bits 
def E(Plain_Text_):
    #Plain_Text_ = "123456ABCD132536"
    K2_aey_ = "AABB09182736CCDD"
    
    # Key generation
    # --hex to _b2
    K2_aey_ = Hex_To_Bin_(K2_aey_)
    
    # --parity bit drop table
    Key_Parity_ = [57, 49, 41, 33, 25, 17, 9, 
            1, 58, 50, 42, 34, 26, 18, 
            10, 2, 59, 51, 43, 35, 27, 
            19, 11, 3, 60, 52, 44, 36, 
            63, 55, 47, 39, 31, 23, 15, 
            7, 62, 54, 46, 38, 30, 22, 
            14, 6, 61, 53, 45, 37, 29, 
            21, 13, 5, 28, 20, 12, 4 ]
    
    # getting 56 bit K2_aey_ from 64 bit using the parity bits 
    K2_aey_ = Muperte_(K2_aey_, Key_Parity_, 56)
    
    # Number of bit shifts 
    Shift_Table_ = [1, 1, 2, 2, 
                    2, 2, 2, 2, 
                    1, 2, 2, 2, 
                    2, 2, 2, 1 ]
    
    # Key- Compression Table : Compression of K2_aey_ from 56 bits to 48 bits
    Key_Compression_Table = [14, 17, 11, 24, 1, 5, 
                3, 28, 15, 6, 21, 10, 
                23, 19, 12, 4, 26, 8, 
                16, 7, 27, 20, 13, 2, 
                41, 52, 31, 37, 47, 55, 
                30, 40, 51, 45, 33, 48, 
                44, 49, 39, 56, 34, 53, 
                46, 42, 50, 36, 29, 32 ]
    
    # Splitting 
    up_ = K2_aey_[0:28]     
    Down_ = K2_aey_[28:56]  
    
    Round_Key_Binary_ = []    # Round_Key_Binary_ for Round Keys in _b2
    Round_Key_in_Hex  = []    # Round_Key_in_Hex for Round Keys in hexadecimal 
    for j in range(0, 16):
        # Shifting the bits by nth shifts by checking from shift table
        up_ = Left_Shift(up_, Shift_Table_[j])
        Down_ = Left_Shift(Down_, Shift_Table_[j])
        
        # Combination of up_ and Down_ string
        combine_str = up_ + Down_
        
        # Compression of K2_aey_ from 56 to 48 bits 
        round_key = Muperte_(combine_str, Key_Compression_Table, 48)
    
        Round_Key_Binary_.append(round_key)
        Round_Key_in_Hex.append(Bin_To_Hex_(round_key))
    
    #print("Encryption")
    Cipher_Text_ = Bin_To_Hex_(desencryptinhex_(Plain_Text_, Round_Key_Binary_, Round_Key_in_Hex))
    return Cipher_Text_
    #print("Cipher Text : ",Cipher_Text_)
    
    #print("Decryption")
    Round_Key_B_Rev = Round_Key_Binary_[::-1]  #Round_Key_B_Rev in Round_Key_Binary in Reverse
    Round_Key_H_Rev = Round_Key_in_Hex[::-1]    #Round_Key_H_Rev in Round_Key_Hex in Reverse
    plaintext = Bin_To_Hex_(desencryptinhex_(Cipher_Text_, Round_Key_B_Rev, Round_Key_H_Rev))
    #print("Plain Text : ",plaintext)
  


#print(E("123456ABCD132536"))
