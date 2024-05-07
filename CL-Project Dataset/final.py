import subprocess
from hindi import hindimain
from wx import wxmain
from verbscrape import verbmain

def hindi():
    # print('ok')
    hindimain()
    crf_code = ["crf_test", "-m", "model", "hindi_tokens.txt", ">", "hindi_output.txt"]
    subprocess.run(crf_code)
    return


def wx():
    # print('notok')
    wxmain()
    crf_code = ["crf_test", "-m", "model", "wx_tokens.txt", ">", "wx_output.txt"]
    subprocess.run(crf_code)
    return

print('Choose your sentence type:')
print('1. Hindi Unicode')
print('2. WX Notation')
number=int(input())
if number==1:
    hindi()
elif number==2:
    wx()