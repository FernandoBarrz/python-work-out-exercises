# Exercise number 25 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1



    
def myxml(tag_name, content="", **kwargs):
    attrs = "".join([f" {key}='{value}'" for key, value in kwargs.items()])
    return f"<{tag_name} {attrs}>{content}</{tag_name}>"


print(myxml("foo"))
    
            
            
            








