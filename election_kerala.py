import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
data=pd.read_excel("C:\\Users\\snair\\Downloads\\Detailed Results.xlsx")
col=data.iloc[1,:]
data=data.iloc[2:,]
data.columns=col
data.reset_index(inplace=True,drop=True)

data.drop(["Candidate Sex","Candidate Age"," VALID VOTES POLLED in General"," VALID VOTES POLLED in Postal","Total Electors"],axis=1,inplace=True)

def int_type(feature):
    return int(feature)

data["Const_no"]=data["Const_no"].map(lambda x: int_type(x))
data["Vote"]=data["Vote"].map(lambda x: int_type(x))
data["Total_votes"]=data["Total_votes"].map(lambda x:int_type(x))

ind=[]
for i in range(1,141):
    temp=list(data.loc[data.Const_no==i][3:].index)
    ind.append(temp)

ind=[val for x in ind for val in x]
data.drop(ind,axis=0,inplace=True)
data.reset_index(inplace=True,drop=True)

pos=[i for i in range(1,4)]*140
data["Position"]=pos

data.Party.unique()
data.loc[data.Party=="CPM","Party"]="CPIM"

data.isna().sum()
data.Const_name.value_counts()
data.Party.value_counts()
data.loc[(data.Party=="BJP") & (data.Position==2)]

data.to_csv("assembly",index=False)



lok_sabha=pd.read_excel("2019_lok_sabha.xls")
col=lok_sabha.iloc[1,:]
lok_sabha=lok_sabha.iloc[2:,:].reset_index(drop=True)
lok_sabha.columns=col
lok_sabha.isna().sum()
lok_sabha=lok_sabha.iloc[18511:20100,:]
lok_sabha.reset_index(drop=True,inplace=True)
lok_sabha=lok_sabha.iloc[:,[3,4,8,9,10]]

col=['Const_no', 'Const_name', 'Candidate', 'Party', 'Vote']
lok_sabha.columns=col

lok_sabha["Const_no"]=lok_sabha["Const_no"].map(lambda x: int_type(x))
lok_sabha["Vote"]=lok_sabha["Vote"].map(lambda x: int_type(x))

lok_sabha.Party.unique()

lok_clean=lok_sabha.drop(lok_sabha.index)

for i in range(1,141):
    temp=lok_sabha.loc[lok_sabha.Const_no==i].sort_values('Vote',ascending=False)[:3]
    lok_clean=lok_clean.append(temp)

pos=[i for i in range(1,4)]*140
lok_clean["Position"]=pos

lok_clean.loc[(lok_clean.Party=="BJP") & (lok_clean.Position==1)]
lok_clean.to_csv("lok_sabha",index=False)


constituency=100
ass=data.loc[data.Const_no==constituency,["Party","Vote"]].reset_index(drop=True)
par=lok_clean.loc[lok_clean.Const_no==constituency,["Party","Vote"]].reset_index(drop=True)
ass["Year"]=2016
par["Year"]=2019
vote_share=ass.append(par).reset_index(drop=True)


fig, ax = plt.subplots(figsize =(12,8))
 
# Horizontal Bar Plot
ax=sns.barplot(x="Year", y="Vote", hue="Party", data=vote_share)
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 20)
ax.yaxis.set_tick_params(pad = 20)
plt.title(data.loc[data.Const_no==constituency,"Const_name"].unique()[0],
          fontsize = 25,fontweight ='bold')

ax.legend(loc='center', frameon=False)

# Add annotation to bars
for i in ax.patches:
    height=i.get_height()
    if not math.isnan(height):
        ax.annotate(str(int(height)), (i.get_x(),height), xytext=(0, 10), textcoords='offset points',fontsize = 12,fontweight ='bold')

len(data.loc[(data.Party=="CPIM") & (data.Position==1) ])
summary=pd.DataFrame([],columns={"","CPIM","INC","BJP"})
summary.iloc[:,0]=["First","Runner Up"]

for i in ["CPIM","INC","BJP"]:
    first=len(data.loc[(data.Party==i) & (data.Position==1) ])
    second=len(data.loc[(data.Party==i) & (data.Position==2) ])
    summary[i][0]=first
    summary[i][1]=second
    











