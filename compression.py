import os
import sys
import pathlib
from os.path import isdir as isFolder
from os.path import exists as isFile_exist

#Public Var's                                       🥞
directory       = ""
good_char       = '+'
bad_char        = '-'
critical_char   = '!'
neutral_char    = '*'
open_info       = '['
close_info      = ']'
root_folder     = ''
Files_Compress  = []
Folders         = []

#Main                                               🍭
def main():
    #probably not needed
    global directory
    global Folders
    global Files_Compress

    if(check_dir(directory)):
        good_info("Proceeding Compression ...\n")
        neutral_info("Getting All the Folders ...")
        neutral_info("Getting All the Files ...\n")
        all_files, all_folders  = get_tree(directory)
        Folders, Files_Compress = all_folders, all_files
        if(len(Folders)):
            good_info("All the Folders Found")
        else:
            neutral_info("No Folders ouf no recursion YYAAAASS")
        if(len(Files_Compress)):
            good_info("All the Files Found")
            #Processing the left over

        else:
            neutral_info("No Files")
            bad_info("if there is no files there is no Compression\n")
            bad_info("Proceeding exit ...")
    else:
        if(isFile_exist(directory)):
            bad_info("Please refer to a folder not a file")
        else:
            bad_info("the Folder doesnt exist")


#Check directory (dont ask me why i made it lel)                                                    🚀
def check_dir(dir):
    return isFolder(dir)
#esthetic print with informative goal (positive)                                                    🚀
def good_info(string):
    print(open_info+good_char+close_info+" ",end="")
    print(string)
#esthetic print with informative goal (negative)                                                    🚀
def bad_info(string):
    print(open_info+bad_char+close_info+" ",end="")
    print(string)
#esthetic print with informative goal (neutral)                                                     🚀
def neutral_info(string):
    print(open_info+neutral_char+close_info+" ",end="")
    print(string)
#esthetic print with informative goal (critical)                                                    🚀
def critical_info(string):
    print(open_info+critical_char+close_info+" ",end="")
    print(string)
#getting the tree of the folders with the files and the folders in them and yep it works with       🚀
#recursion thanks computerphile i love that youtube channel
def get_tree(dir):
    files_folders = os.listdir(dir)
    all_files = []
    all_folders = []
    dir_a  = str(pathlib.Path(dir).absolute())

    for x in files_folders:
        file_extension = os.path.splitext(dir+x)[1]
        edir = dir_a+"/"+x
        if(isFolder(edir)):
           all_folders.append({'foldername':x,"folderdir":dir_a+"/"+x,'Parentdir':dir_a,'checked':False})
        elif(isFile_exist(edir)):
            all_files.append({'filename':x,'filedir':dir_a,'filext':file_extension,'parentFoldername':os.path.basename(dir_a)})
        else:
            critical_info("i have no idea wtf happend {DEBUG TIME}")

    #here the painfull recursion experience               
    for x in all_folders:
        if(not x["checked"]):
            all_files_recursion, all_folders_recursion = get_tree(x["folderdir"])
            all_files = all_files + all_files_recursion
            all_folders = all_folders + all_folders_recursion
            x["checked"] = True

    return all_files, all_folders


#Check if an argument was given and call main        🥨
if(len(sys.argv) <= 1):
    bad_info(sys.argv[0]+" no Arguments")
    #🚬help()
else:
    directory = sys.argv[1]
    main()