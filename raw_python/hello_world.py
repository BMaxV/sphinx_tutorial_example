from submodule.func import say_hi

class Hi:
    """hi class"""
    def main(self):
        say_hi()
        
def test():
    h=Hi()
    h.main()

if __name__=="__main__":
    test()
    
        
