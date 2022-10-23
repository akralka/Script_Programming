import argparse, re
 
def open_file():
    with open("file.py", "r") as file:
        print(file.read()) 
        # for el in file.readlines():
        #     print(el, end="")
        #     file.close()





if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help=r"a continuation character for input files (default: '\')", required=False)
    parser.add_argument("-f", "--file", help="Give input!", required=True)

    try:
        args = parser.parse_args()
        
    except:
        print("Specify file names")      


        # open_file()




