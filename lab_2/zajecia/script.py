import argparse, re

def open_file(file):
    with open(file, "r") as f:
        for i in f.readlines():
            print(i, end="")

def conversion(file, char):

    new_file =  open('file_tmp.txt',"w")

    string = ""

    if char in "+*?.[]()\{\}$^\\|":
        tmp = f"\\{char}$"
    else:
        tmp = f"{char}$"

    file = open(file, 'r').read()
    lines = file.split('\n')
    for line in lines:
        if re.search(tmp, line):
            string += line[:-1]     
            new_file.write(string)      
        else:
            string +=line 
            new_file.write(string+'\n')
        string = ""

    new_file.close()
    return open_file("file_tmp.txt")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help=r"a continuation character for input files (default: '\')", required=False, default="\\")
    parser.add_argument("-f", "--file", help="Give input!", required=True, nargs="+")

    
    try:
        args = parser.parse_args()
        
    except:
        print("Specify file names")      
        exit()

    for file in args.file:
        conversion(file, args.c[0])


# python .\script.py -f file.py    

