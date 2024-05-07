import subprocess
from hindi import hindimain
from wx import wxmain
from verbscrape import verbmain
from wxuniwx import final_main

def hindi():
    # print('ok')
    hindimain()
    command = "crf_test -m model tokens.txt > output.txt"
    crf_code = ["crf_test", "-m", "model", "tokens.txt"]
    subprocess.run(command, shell=True)
    subprocess.run(crf_code)
    return


def wx():
    # print('notok')
    wxmain()
    command = "crf_test -m model tokens.txt > output.txt"
    crf_code = ["crf_test", "-m", "model", "tokens.txt"]
    subprocess.run(command, shell=True)
    subprocess.run(crf_code)
    return

def morph():
    verbmain()
    output_data = []
    lines = []
    with open("verbs_output.txt", "r") as file:
        for line in file:
            output_data.append(line.strip())
    for words in output_data:
        line=final_main(words)
        
        lines.append(line)
    print(lines)
    with open ('output.txt','a') as output:
        output.write('\n'.join(lines)) 

print('Choose your sentence type:')
print('1. Hindi Unicode')
print('2. WX Notation')
number=int(input())
if number==1:
    hindi()
elif number==2:
    wx()
morph()
# output = final_main('कर')
# print(output)
