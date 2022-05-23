#Read file
#extract sequence infomation
#import BLOSUM_62
#alignment-score
#Print alignment result in central line

import pandas as pd
import re

#import BLOSUM_62 matrix,this matrix is obtained from   https://github.com/Raha-Kheirinia/BLOSUM62
BLOSUM_62={'A':[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,0,-4],'R':[-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0,-1,-4],
           'N':[-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0,-1,-4],'D':[-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1,-1,-4],
           'C':[0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3,-2,-4],'Q':[-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3,-1,-4],
           'E':[-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],'G':[0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2,-1,-4],
           'H':[-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0,-1,-4],'I':[-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3,-1,-4],
           'L':[-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3,-1,-4],'K':[-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1,-1,-4],
           'M':[-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1,-1,-4],'F':[-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3,-1,-4],
           'P':[-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1,-2,-4],'S':[1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0,0,-4],
           'T':[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,0,-4],'W':[-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3,-2,-4],
           'Y':[-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2,-1,-4],'V':[0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2,-1,-4],
           'B':[-2,-1,3,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1,-1,-4],'Z':[-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
           'X':[0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1,-1,-4],'*':[-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]}
BLOSUM_62=pd.DataFrame(BLOSUM_62,columns=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'],
                       index=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*'])

#import DNA sequence
def readfa(file):
    Raw_file=open(file)
    for lines in Raw_file:
        if lines.startswith('>') == False:
            sequence=lines
    return sequence

#use matrix to mark
def Global_alignment(sequence1,sequence2):
    score=0
    for i in range(len(sequence1)):
        score=score+BLOSUM_62[sequence1[i]][sequence2[i]]
    return score

#indentity calculator
def identity_calculator(sequence1,sequence2):
    same=0;central_line=''
    for i in range(len(sequence1)):
        if sequence1[i]==sequence2[i]:
            same+=1
            central_line=central_line+sequence1[i]
        elif sequence1[i]!=sequence2[i] and BLOSUM_62[sequence1[i]][sequence2[i]] > 0:
            central_line=central_line+'+'
        else:
            central_line=central_line+' '
    identity=(same/len(sequence1))*100;identity=str('%.2f'%identity)+'%'  #output identity
    return (identity,central_line)

#implement of functions
DLX5_human=readfa(r'DLX5_human.fa')
DLX5_mouse=readfa(r'DLX5_mouse.fa')
Random_seq=readfa(r'RandomSeq.fa')

DLX5_human=re.sub(r'\s','',DLX5_human)    #Remove all the space
DLX5_mouse=re.sub(r'\s','',DLX5_mouse)
Random_seq=re.sub(r'\s','',Random_seq)

score_human_vs_mouse=Global_alignment(DLX5_human,DLX5_mouse)
score_human_vs_random=Global_alignment(DLX5_human,Random_seq)
score_mouse_vs_random=Global_alignment(DLX5_mouse,Random_seq)

Rawresult_humanvsmouse=identity_calculator(DLX5_human,DLX5_mouse)
Rawresult_humanvsrandom=identity_calculator(DLX5_human,Random_seq)
Rawresult_mousevsrandom=identity_calculator(DLX5_mouse,Random_seq)

identity_humanvsmouse=Rawresult_humanvsmouse[0]
central_line_humanvsmouse=Rawresult_humanvsmouse[1]
identity_humanvarandom=Rawresult_humanvsrandom[0]
central_line_humanvsrandom=Rawresult_humanvsrandom[1]
identity_mousevsrandom=Rawresult_mousevsrandom[0]
central_line_mousevsrandom=Rawresult_mousevsrandom[1]
print(f'---Alignment score:{score_human_vs_mouse} Human vs Mouse---')
print('DLX5_human',DLX5_human)
print('          ',central_line_humanvsmouse)
print('DLX5_mouse',DLX5_mouse)
print('Identity',identity_humanvsmouse)
print(f'---Alignment score:{score_human_vs_random} Human vs Random---')
print('DLX5_human',DLX5_human)
print('          ',central_line_humanvsrandom)
print('Random_seq',Random_seq)
print('Identity',identity_humanvarandom)
print(f'---Alignment score:{score_mouse_vs_random} Mouse vs Random---')
print('DLX5_mouse',DLX5_mouse)
print('          ',central_line_mousevsrandom)
print('Random_seq',Random_seq)
print('Identity',identity_mousevsrandom)

#Summary:
#The alignment score of human DLX5 vs murine DLX5 is 1490.
#The alignment score of human DLX5 vs random is -351.
#The alignment score of murine DLX5 vs random is -348.
#The identity of human DLX5 and mouse DLX5 is 96.54%,while the identity against random sequence is 2.77% and 3.11% respectively.
#This result shows a significant evolutional homologous of human and murine DLX5.