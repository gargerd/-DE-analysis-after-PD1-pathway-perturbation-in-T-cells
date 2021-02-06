import pandas as pd
import numpy as np
te_d=r"C:\Users\Dani\Desktop\Dream\Mouse"
tr_d=r"C:\Users\Dani\Desktop\Dream\Mouse"

with open ("metadata_features.txt") as f:
    metad=f.read().split()


class series_matrix:
    def __init__(self,fname):
        self.fname=fname

    def read_series_matrix(self):
        with open(self.fname) as f:
            content = f.read().split("!")
        return content

    def print_row_with_word(self,word):
        return_list=[]
        txt=self.read_series_matrix()
        for t in txt:
            if word in t:
                return_list.append(t)
        return return_list

    def look_for_word(self,func,word,split=None):
        txt=func
        for w in txt:
            if word in w:
                if split==None:
                    return (w.split())
                elif split!= None:
                    return w.split(split)

project="GSE39205"

#p is class of series matrix of the project
p=series_matrix(tr_d+"/"+project+"/"+project+"_series_matrix.txt")

#creating gene expression counts (normalized)
sam=(p.look_for_word(p.print_row_with_word("Sample_title"),"PDL1-overexpressed"))
sam=[x.strip('"') for x in sam[3::4]]
pd1=['y' if 'overexpressed'in x else 'n' for x in sam]
data_list=[pd1]
gsm=(p.look_for_word(p.print_row_with_word("Sample_geo_accession"),"GSM958123"))
gsm=[x.strip('"') for x in gsm[1:]]

dic=dict(zip(metad,data_list))
df_metad=pd.DataFrame(dic,index=gsm)
df_metad.to_csv(project+"_metadata.csv")


d=pd.read_csv(project+"_exp_data.txt",delimiter="\t")
d.set_index("ID_REF",inplace=True)
#d.rename(columns=dict(zip(d.columns[:],sam)),inplace=True)
d.to_csv(project+"_gene_exp.csv")

