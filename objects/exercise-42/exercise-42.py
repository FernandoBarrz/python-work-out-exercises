# Exercise number 42 - Python Workout 50 essential exercises book
# Author: Barrios Ramirez Luis Fernando
# Language: Python3 3.10.2 64-bit on Mac M1


class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
            
        except ValueError:
            pass

        return dict.__getitem__(self, key)

new_dict = FlexibleDict()
new_dict[1] = 'FERNANDO'
new_dict[2] = 'PABLO'
new_dict['3'] = 'MARCO'
new_dict['4'] = 'ANTONIO'

print(new_dict[4])