import sys
import argparse
import os
import json
from html.parser import HTMLParser

indir = '/u/cs401/A1/data/';

def preproc1( comment , steps=range(1,11)):
    ''' This function pre-processes a single comment

    Parameters:                                                                      
        comment : string, the body of a comment
        steps   : list of ints, each entry in this list corresponds to a preprocessing step  

    Returns:
        modComm : string, the modified comment 
    '''
    bool_check = False 
    # The modified comment after removing the noise from the comment. 
    # Noise is specifically mentioned in the below mentioned steps. 
    modComm = ''
    if '\n' in comment:
        modComm = remove_newline(comment)
        bool_check = True
    if 2 in steps:
        print('TODO')
    if 3 in steps:
        print('TODO')
    if 4 in steps:
        print('TODO')
    if 5 in steps:
        print('TODO')
    if 6 in steps:
        print('TODO')
    if 7 in steps:
        print('TODO')
    if 8 in steps:
        print('TODO')
    if 9 in steps:
        print('TODO')
    if 10 in steps:
        print('TODO')
    
        
    return modComm if bool_check else comment


## Helper Functions for specific tasks

#1 To remove the newline characters from the comment.

def remove_newline(comment):
    ''' Returns a string with all newline characters removed from it.
    
    @param String comment: a String to remove newline character from.
    @rtype: String
    >>> comment = "\nHel\nlo how\n \n are you?\n"
    >>> remove_newline(comment)
    >>> 'Hello how are you?'
    
    '''
    
    #Remove the newline character
    modified_comment = comment.replace("\n", "")
    
    return modified_comment

#2 Convert the HTML Character to their ascii values. 

def convert_HTML_char(comment):
    ''' Returns a string with all HTML characters replaced with their corresponding 
    ascii values.
    
    @param String comment: a String to replace HTML characters from
    @rtype: String
    >>> comment = "\nHel\nlo how\n \n are you?\n"
    >>> convert_HTML_char(comment)
    >>> 'Hello how are you?'
    
    '''
    pass 

def main( args ):

    allOutput = []
    for subdir, dirs, files in os.walk(indir):
        for file in files:
            fullFile = os.path.join(subdir, file)
            print("Processing " + fullFile)

            data = json.load(open(fullFile))
            for key in data:
                allOutput.append({key:data[key]})
           
            

            # TODO: select appropriate args.max lines
            # TODO: read those lines with something like `j = json.loads(line)`
            # TODO: choose to retain fields from those lines that are relevant to you
            # TODO: add a field to each selected line called 'cat' with the value of 'file' (e.g., 'Alt', 'Right', ...) 
            # TODO: process the body field (j['body']) with preproc1(...) using default for `steps` argument
            # TODO: replace the 'body' field with the processed text
            # TODO: append the result to 'allOutput'
            
    fout = open(args.output, 'w')
    fout.write(json.dumps(allOutput))
    fout.close()
    
    
    
    
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process each .')
    parser.add_argument('ID', metavar='N', type=int, nargs=1,
                        help='your student ID')
    parser.add_argument("-o", "--output", help="Directs the output to a filename of your choice", required=True)
    parser.add_argument("--max", help="The maximum number of comments to read from each file", default=10000)
    args = parser.parse_args()

    if (args.max > 200272):
        print("Error: If you want to read more than 200,272 comments per file, you have to read them all.")
        sys.exit(1)
        
    main(args)
