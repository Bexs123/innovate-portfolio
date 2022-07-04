# Object Oriented Programming 

# Procedural programming
# reads top down

# scaleabilty 


class Guitar():
    def __init__(self, colour,string_no):
        self.colour = colour
        self.string_no = string_no
        
        # class give custom methods
        def play(self):
            print('Noise!')
        
        wills_guitar= Guitar ("blue", 6)
        
        wills_guitar.play()
        # print(wills_guitar)
        
        example_variable_1 = 3.14152
        
        print(type(example_variable_1))
        
        example_variable_2 = "Hello World"
        
        print(type(example_variable_2))
        
        var = 'string example blah blah blah'
        
        example_list = [
            1,2, 3, 4, 5, 6, 7, 8
        ]
        
        some_list = []
        print(type(example_list))
        
        example_list.pop()
        
        print(wills_guitar)
        
        # this empty codespace is an object as well.