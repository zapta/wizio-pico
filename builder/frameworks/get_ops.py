
import os, shutil
from os.path import join, normpath, basename
from shutil import copyfile

dir = ""
key = []
def wrap(fpath, name):
    global dir
    F = open(fpath, 'r')
    L = F.readlines()
    D = os.path.dirname(fpath)
    #print("-------------{}".format(D))
    for line in L:
        if False == line.startswith( 'wrapper_func' ): continue
        if dir == "":
            print("-------------{}".format(D))    
            dir = D
        print('            "-Wl,-wrap,{}",'.format(line.strip())) 
    F.close()  
    dir = ""

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            wrap( join(root, f), f )

def main():
    list_files("C:/Users/1124/.platformio/packages/framework-wizio-pico/SDK/pico")
    pass

if __name__ == "__main__":
    main()            