import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_excel("Downloads//Detailed Results.xlsx")
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

data.isna().sum()
data.Const_name.value_counts()
data.Party.value_counts()
data.to_csv("election_kerala",index=False)

const_data=data=data.loc[data.Const_no==1]

g=sns.barplot(x="Party",y="Vote",data=const_data)
for index, row in const_data.iterrows():
    g.text(row.Party,row.Vote, color='black', ha="center")


plt.bar(x=const_data.Party,height=const_data.Vote)
for index, value in enumerate(const_data.Vote):
    plt.text(value, index, str(value))
plt.set_tick_params(pad=5)

fig, ax = plt.subplots(figsize =(10, 5))
 
# Horizontal Bar Plot
ax.barh(const_data.Party,const_data.Vote,color=['red', 'blue', 'orange'],edgecolor='black')
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')

l=data.Const_name.unique()
pd.DataFrame(l).to_csv("constituency",index=False)


