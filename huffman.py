
class Huffman :
    
    __data = {}
    __done = {}
    __routes = {}
    __msg = "Ahmed Ali"
    __encoded_msg = ''
    __decoded_msg = ''
    __sum = 0
    


    def __init__(self , msg):

        self.__msg = msg
        


    def __get_Freq(self) :
       
        for i in self.__msg :

            self.__sum  +=1

            if i in self.__data :
                self.__data[i]['val'] +=1
                
            else:
                self.__data[i] = {'val' : 1}


        ########  Getters & Setters ################

    def set_msg(self , msg) :

        self.__msg = msg

    def Read_file(self , input) :
        with open(input) as file :
         self.__msg = file.read()

        

    def get_msg(self) :

        return self.__msg 
    
    def get_encoded_msg(self) :

        return self.__encoded_msg
    
    def export_msg(self , output) :

        with open(output , "w") as file :
          file.write(self.__msg)

    



    

        #############  Encoding & Decoding ################


    def Encoding(self) :

        #####  1 - Get frequecy of data ########

        self.__get_Freq()

        
        #####  2 - Sort by frequency ###########

        
        sorted_keys = sorted(self.__data , key = lambda x :self.__data[x]['val'] , reverse = True)

       

        #####  3 - Building Huffman Tree  ############

        while len(sorted_keys) > 1 :
            ak = sorted_keys.pop()  
            bk = sorted_keys.pop()
            akval = self.__data[ak]['val']
            bkval = self.__data[bk]['val']
            totalval = akval + bkval
            self.__done[ak] , self.__done[bk] = self.__data[ak] , self.__data[bk]
            del self.__data[ak] , self.__data[bk]
            self.__data[str(ak+bk)] = {'val' :totalval , 'left' : ak , 'right' : bk }
            sorted_keys = sorted(self.__data , key = lambda x :self.__data[x]['val'], reverse = True)
            self.__done[list(self.__data.keys())[0]] = list(self.__data.values())[0]
        

        #####  4- trace the Hufman tree ##############

        def trace(currentnode , char , route) :
            if 'left' in self.__done[currentnode] : 
                if char in self.__done[currentnode]['left'] :
                    newRoute = route + '0'
                    trace(self.__done[currentnode]['left'] , char , newRoute)

            if 'right' in self.__done[currentnode] : 
                if char in self.__done[currentnode]['right'] :
                    newRoute = route + '1'
                    trace(self.__done[currentnode]['right'] , char , newRoute)
            if 'left' not  in self.__done[currentnode] : 
                if 'right' not  in self.__done[currentnode] :
                    self.__routes[char] = route



        rootNode = list(self.__data.keys())[0]
        for i in rootNode :
            trace (rootNode , i , '')

        
        for i in self.__msg :
            self.__encoded_msg +=self.__routes[i]

        return(self.__encoded_msg )
    


    def Decoding(self ,binary_stream) :
    
        vals = list(self.__routes.values())
        keys = list(self.__routes.keys())
        out_str = ''
        current_char = ''
        for i in binary_stream :
            current_char += i
            if current_char in vals :
                out_str += keys[vals.index(current_char)]
                current_char = ''
        
        self.__decoded_msg = out_str



    
                    #############  printing Methods  ########################
                    

    def print_encoded_msg(self) :

        print(self.__encoded_msg )


    def print_Freq(self) : 
                        
        self.__get_Freq()
        for it in self.__data :
            print(f"{it} =  {(self.__data[it]['val'] / self.__sum):.3f}") 


    def print_Huff_Table(self) :

        for route in self.__routes :

            print(f'{route} =  {self.__routes[route]}')

    
    def print_decoded_msg(self) :

        print(self.__decoded_msg )



                





     