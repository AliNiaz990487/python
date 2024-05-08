import time

GRAY = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

class Rectangle:
    def __init__(self, width: int, height: int, chars: dict = None, colors: dict = None):
        self._validate(width=width, height=height)
        
        self.width = width
        self.height = height
        self.chars = self._validate_dict(chars, "*")
        self.colors = self._validate_dict(colors, RESET)
        self.get_inner_width = lambda: self.width-(len(self.chars["left"])+len(self.chars["right"]))
        
    def create(self, is_create: bool = True) -> str:
        rec_str = f"{self.colors['top']}{self.chars['top']}"*self.width + "\n"

        for _ in range(self.height):
            rec_str += f"{self.colors['left']}{self.chars['left']}{RESET}" 
            rec_str += f" "*self.get_inner_width() 
            rec_str += f"{self.colors['right']}{self.chars['right']}\n"

        rec_str += f"{self.colors['bottom']}{self.chars['bottom']}"*self.width + f"\n{RESET}"

        if is_create:
            print(rec_str)

        return rec_str
    
    def create_animate(self, run_time: int = 1):
        rec_str = self.create(is_create=False)
        t = run_time/len(rec_str)

        for i in range(len(rec_str)):
            print(end=rec_str[i], flush=True)
            time.sleep(t)

    def _validate(self, **kwargs):
        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise ValueError(f"{RED}{key} must be an integer.{RESET}")
            if value <= 0:
                raise ValueError(f"{RED}{key} should be grater than 0 not ({value}).{RESET}")
        
        
    
    def _validate_dict(self, dictionary: dict, value: str):
        sides = ["top", "right", "bottom", "left"]
        if dictionary is None:
            dictionary = dict()
            for side in sides:
                dictionary[side] = value
            return dictionary

        if "all" in dictionary.keys():
            for side in sides:
                dictionary[side] = dictionary["all"]
            return dictionary
        
        for side in sides:
            try:
                    dictionary[side]
            except:
                dictionary[side] = value
            
        return dictionary
            

class Squar(Rectangle):
    def __init__(self, side_length, **kwargs):
        super().__init__(side_length*2, side_length, **kwargs)



r = Rectangle(20, 4, chars={"all": "="}, colors={"top": GREEN, "right": BLUE, "bottom": YELLOW})
# r.create()
r.create_animate(run_time=3)

s = Squar(5, colors={"all": BLUE}, chars={"top": "-", "right": "", "bottom": "-", "left": "||"})
s.create()

