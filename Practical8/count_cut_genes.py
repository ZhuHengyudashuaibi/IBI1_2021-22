import re

file_name=input('Please type in your fasta file name')
org_file=open('cut_genes.fa','r')
newfile=open(file_name,'w')
#read everyline
frag=[]
for line in org_file:
    if line.startswith('>'):
        continue
    else:
        frag.append(len(re.findall('GAATTC',line))+1)
org_file.close()
org_file=open('cut_genes.fa','r')
name=[]
i=0
for line in org_file:
    if line.startswith('>'):
        line=re.sub(r'[0-9]+',str(frag[i]),line)
        newfile.write(line)
        i=i+1
    else:
        newfile.write(line)

