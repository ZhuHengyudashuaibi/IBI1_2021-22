from matplotlib import pyplot as plt
import xml.sax
import numpy as np
import math

GO_dict={};GO_dict_withtranslation={};GO_dict_parent={}
term=0
nodes=0
node_record={} ;node_record_withtranslation={}     #definition of global variables
With_translation_list=[]

#Extract term ID and is_a IDs and store it in a dictionary
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData= ''
        self.id=''
        self.is_a=''
        self.wetherterm=False       #This boolean variable is added to avoid id under "typedef" being included.
        self.contents= []           #This method is obtained from https://blog.csdn.net/qq_22766903/article/details/106481917?ops_request_misc=&request_id=&biz_id=102&utm_term=python%20SAX%E8%A7%A3%E6%9E%90XML%E6%97%B6%EF%BC%8Ccharact&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-106481917.142^v10^control,157^v4^control&spm=1018.2226.3001.4187
                                    #When xml.sax dealing with some huge data, the content may be seperated into several list. E.g. At first my is_a value of id:GO:0006816 is 070838,but it should be GO:0070838
                                    #This method join the several lists together to get a complete character

    def startElement(self,tag,attributes):
        global term
        self.CurrentData= tag
        if tag=='term':
            self.wetherterm=True
            term=term+1
        elif tag == 'typedef':
           self.wetherterm=False
        return term

    def endElement(self,tag):
        global GO_dict
        global GO_dict_parent
        if self.wetherterm==True:
           if self.CurrentData == 'id':
              GO_dict[self.id]=[]
              GO_dict_parent[self.id]=[]
           elif self.CurrentData=='is_a':
                GO_dict[self.id].append(self.is_a)
        self.CurrentData=''
        self.contents.clear()
        return GO_dict

    def characters(self,content):
        if self.CurrentData=='id':
            self.contents.append(content)
            self.id= ''.join(self.contents)
        elif self.CurrentData == 'is_a':
            self.contents.append(content)
            self.is_a = ''.join(self.contents)

class GOHandler_with_translation(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData= ''
        self.id=''
        self.defstr=''
        self.wetherterm=False       #This boolean variable is added to avoid id under "typedef" being included.
        self.contents= []           #This method is obtained from https://blog.csdn.net/qq_22766903/article/details/106481917?ops_request_misc=&request_id=&biz_id=102&utm_term=python%20SAX%E8%A7%A3%E6%9E%90XML%E6%97%B6%EF%BC%8Ccharact&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-106481917.142^v10^control,157^v4^control&spm=1018.2226.3001.4187
                                    #When xml.sax dealing with some huge data, the content may be seperated into several list. E.g. At first my is_a value of id:GO:0006816 is 070838,but it should be GO:0070838
                                    #This method join the several lists together to get a complete character
    def startElement(self,tag,attributes):
        self.CurrentData= tag
        if tag=='term':
            self.wetherterm=True
        elif tag == 'typedef':
           self.wetherterm=False

    def endElement(self,tag):
        global With_translation_list
        if self.wetherterm==True :
           if self.CurrentData == 'id':
             With_translation_list.append(self.id)
        self.CurrentData=''
        self.contents.clear()

    def characters(self,content):
        global With_translation_list
        if self.CurrentData=='id':
            self.contents.append(content)
            self.id= ''.join(self.contents)
        elif self.CurrentData == 'defstr':
            if self.wetherterm == True:
                self.contents.append(content)
                self.defstr = ''.join(self.contents)
                whethertrans= ("translation" in self.defstr) or ("Translation" in self.defstr)
                if whethertrans == False and (self.id in With_translation_list):
                    With_translation_list.remove(self.id)

parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler= GOHandler()
parser.setContentHandler( Handler )
parser.parse('go_obo.xml')


parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler= GOHandler_with_translation()
parser.setContentHandler( Handler )
parser.parse('go_obo.xml')


#make a dict storing {id:[parentnodes]}
for key,value in GO_dict.items():
    for every_is_a in value:
        GO_dict_parent[every_is_a].append(key)
#Find the number of parentnodes
    #get root
    #get parent nodes
    #set parent nodes as root
    #find until no parent
class Tree():
    def __init__(self):
        self.root=[]
        self.parent=[]
        self.all_parent=[]

    def getroot(self,root):
        temlist=[]
        temlist.append(root)
        root=temlist     #make it a list
        self.root=root

    def getparent(self):
        for everyroot in self.root:
            self.parent.extend(GO_dict_parent[everyroot])
        self.parent=list(set(self.parent))              #remove all the repeating elements in self.parent
        self.all_parent.extend(self.parent)
        return self.parent

    def exchange(self):
        self.root=self.parent
        self.parent=[]

    def count(self):
        global nodes
        self.all_parent=list(set(self.all_parent))
        nodes=len(self.all_parent)

    def record(self,root):
        global node_record
        node_record[root]=nodes

    def loading(self,root,nodes,loading):
        print(f"{root}: parent nodes= {nodes}****loading..... {loading}/47340")
        self.all_parent=[]


#Get the number of nodes for all the terms
tree=Tree()
loading=0         #Initialize
for root in GO_dict:
    loading+=1
    tree.getroot(root)        #Initialize
    i=[1]
    while i != []:
        tree.getparent()
        i = tree.getparent()
        tree.exchange()
    tree.count()
    tree.record(root)
    tree.loading(root, nodes, loading)
    nodes=0
print('<DONE>')


#Get the number of nodes for terms with translation
loading2=0
for everyid in With_translation_list:
    if everyid in node_record:
        node_record_withtranslation[everyid]=node_record[everyid]
        loading2+=1
        print(f'{everyid}: {node_record[everyid]} ****loading ({loading2}/301)')
#Make boxplot for all terms
def makeboxplot(dict,title):
    node_count=[]
    for keys in dict:
        value=dict[keys]
        value=math.log(value+1)           #Use ln(value+1) to normalise the data
        node_count.append(value)
    plt.boxplot(node_count,
                vert=True,
                whis=3,
                patch_artist=True,
                meanline=False,
                showbox=True,
                showcaps=True,
                labels=['term'],
                showfliers=True)
    plt.title(title)
    plt.ylabel('log(Node+1)',fontsize=10)
    plt.show()

title_all='Box plot of the number of childnodes for all terms'
makeboxplot(node_record,title_all)
title_translation='Box plot of the number of childnodes for terms involving translation'
makeboxplot(node_record_withtranslation,title_translation)

#data analysis
print('Total number of terms: ',term)
print('Maximum nodes in all the terms ',np.max(list(node_record.values())))
print('Average nodes in all the terms ',np.mean(list(node_record.values())))
print('Maximum nodes in terms with translation ',np.max(list(node_record_withtranslation.values())))
print('Average nodes in terms with translation',np.mean(list(node_record_withtranslation.values())))
#Comment:
#"Translation" terms contain a greater number of child nodes than the overall gene ontology on average.
#The average number of childnodes of "translation" terms is 13.30, while the average number of all terms is 12.08.

