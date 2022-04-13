import re

gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
tem = ''
# transform fasta form into dictionary
#   extract information and seq -> 2 lists
#   combine-> dictionary
#   for list1-> simplify
#   for list2 -> search for EcoRI-> sign out the False seq
#   combine into a dictionary
#   rewrite into a fasta file

info = [];
seq = []
for line in gene:
    line.rstrip()
    if line.startswith('>'):
        info.append(line)
gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
lin = ''
for line in gene:
    if line.startswith('>'):
        lin = '*'
    else:
        lin = line
    tem = tem + lin
tem = re.sub(r'\n', '', tem)
seq = tem.split('*')
seq.remove('')

# select out seqs
for i in range(len(seq)):
    if not re.search('GAATTC', seq[i]):
        seq[i] = ''
# extract DNA length
length = []
for i in range(len(seq)):
    if seq[i] != '':
        length.append(len(seq[i]))
    if seq[i] == '':
        length.append('*')
# simplify
for q in range(len(info)):
    info[q] = ''.join(re.findall(r'^>(.+)?_mRNA', info[q]))
#gene_name + gene_length
name_len=[]
for q in range(len(info)):
    name_len.append(info[q]+'  '+str(length[q]))
#combine as a dictionary
output={}
output=dict(zip(name_len,seq))
#kick off *
for key in list(output.keys()):
    if ('*' in key)==True:
        del output[key]                #This code is obtainde from https://blog.csdn.net/aobian2884/article/details/101404445?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164983697716781683984125%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=164983697716781683984125&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-101404445.142^v7^pc_search_result_control_group,157^v4^new_style&utm_term=python%E5%88%A0%E9%99%A4dictionary%E4%B8%ADvalue&spm=1018.2226.3001.4187
                                      #Every member in the key of this dictionary is extracted.
#Write a new fasta file
otfile=open('cut_genes.fa','w')
keys=list(output.keys())
for j in range(len(output)):
    otfile.write('>'+keys[j]+'\n')
    otfile.write(output[keys[j]]+'\n')
