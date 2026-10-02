import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as c 

df_main = pd.read_csv("C:/Users/pandy/Desktop/Himesh Pandya/Python/DS-AI/Projects/destinations_rows.csv",encoding= "Latin1")
print(df_main.head())
print(df_main.describe())
print(df_main.info())

df = df_main[["id","slug","name","state","region","type","budget","duration_days","best_season","difficulty","crowd","nearby","alternative_to"]]
df = df.set_index("id")
print(df.head())
print(df.describe())
print(df.info())


#Analysis based on  days and budget(numerical column)
#DAYS
max_days_tour = (df["duration_days"] == df["duration_days"].max()).sum()
print(f"Max days of tour is {df['duration_days'].max()} and no. of places having max days are {max_days_tour}")
min_days_tour = (df["duration_days"] == df["duration_days"].min()).sum()
print(f"Min days of tour is {df['duration_days'].min()} and no. of places having min days are {min_days_tour}")
mean_days = df["duration_days"].mean()
print(f"Average days of tour:{mean_days}")
#Graph
count_days = df["duration_days"].value_counts()
x = count_days.index
y = count_days.values
plt.figure(figsize=(10,6))
plt.xlabel("No. of days")
plt.ylabel("Toursite")
plt.title("No. of days/toursite ",fontsize = 12)
plt.bar(x,y,width=0.3,color = "Orange")
plt.show()
#BUDGET
max_budget = (df["budget"] == df["budget"].max()).sum()
print(f"The max budget is {df['budget'].max()}₹ and no. of place having max budget is {max_budget}")
min_budget = (df["budget"] == df["budget"].min()).sum()
print(f"The min budget is {df['budget'].min()}₹ and no. of place having min budget is {min_budget}")
mean_budget = df["budget"].mean()
print(f"Average budget for toursite:{mean_budget}₹.")
#Graph
count_budget = df["budget"].value_counts()
y1 = count_budget.index
x1 = count_budget.values
plt.figure(figsize=(10,6))
plt.xlabel("Budget(₹)")
plt.ylabel("no. of places")
plt.title("Toursite v/s budget",fontsize = 12)
plt.bar(y1,x1,width=400,color = "Orange")
plt.show()
#Budget days relations
c.scatterplot(data = df,x = "budget",y = "duration_days",hue= "region")
plt.show()                      


#Analysis based on states and regions
state_count = df["state"].value_counts()
region_count = df["region"].value_counts()
state_count = state_count.sort_values(ascending=False)
region_count = region_count.sort_values(ascending=False)
print(f"The most popular state for tourism is {state_count.index[0]} with no. of tourism places  {state_count.iloc[0]}")
print(f"The least popular state for tourism is {state_count.index[-1]} with no. of tourism places  {state_count.iloc[-1]}")
print(f"The most popular region for tourism is {region_count.index[0]} with no. of tourism places  {region_count.iloc[0]}")
print(f"The least popular region for tourism is {region_count.index[-1]} with no. of tourism places  {region_count.iloc[-1]}")
#region-wise-datasets
sid = df[df["region"] == "Southern India"]
nid = df[df["region"] == "Northern India"]
neid = df[df["region"] == "Northeastern India"]
wid = df[df["region"] == "Western India"]
eid = df[df["region"] == "Eastern India"]
cid = df[df["region"] == "Central India"]
region_wise_Datasheet = {
    "Region":["South India","North India","Northeast India","West India","East India","Central India"],
    "Tourism places":[74,69,64,58,38,25],
    "No. of States":[sid["state"].nunique(),nid["state"].nunique(),neid["state"].nunique(),wid["state"].nunique(),eid["state"].nunique(),cid["state"].nunique()],
    "Average budget(₹)":[sid["budget"].mean(),nid["budget"].mean(),neid["budget"].mean(),wid["budget"].mean(),eid["budget"].mean(),cid["budget"].mean()],
    "Average duration days":[sid["duration_days"].mean(),nid["duration_days"].mean(),neid["duration_days"].mean(),wid["duration_days"].mean(),eid["duration_days"].mean(),cid["duration_days"].mean()],
    "Best Season":[sid["best_season"].max(),nid["best_season"].max(),neid["best_season"].max(),wid["best_season"].max(),eid["best_season"].max(),cid["best_season"].max()],
    "Trek":[(sid["type"] == "Trek").sum(),(nid["type"] == "Trek").sum(),(neid["type"] == "Trek").sum(),(wid["type"] == "Trek").sum(),(eid["type"] == "Trek").sum(),(cid["type"] == "Trek").sum()],
    "Mountain":[(sid["type"] == "Mountain").sum(),(nid["type"] == "Mountain").sum(),(neid["type"] == "Mountain").sum(),(wid["type"] == "Mountain").sum(),(eid["type"] == "Mountain").sum(),(cid["type"] == "Mountain").sum()],
    "Valley":[(sid["type"] == "Valley").sum(),(nid["type"] == "Valley").sum(),(neid["type"] == "Valley").sum(),(wid["type"] == "Valley").sum(),(eid["type"] == "Valley").sum(),(cid["type"] == "Valley").sum()], 
    "Village":[(sid["type"] == "Village").sum(),(nid["type"] == "Village").sum(),(neid["type"] == "Village").sum(),(wid["type"] == "Village").sum(),(eid["type"] == "Village").sum(),(cid["type"] == "Village").sum()],
    "Beach":[(sid["type"] == "Beach").sum(),(nid["type"] == "Beach").sum(),(neid["type"] == "Beach").sum(),(wid["type"] == "Beach").sum(),(eid["type"] == "Beach").sum(),(cid["type"] == "Beach").sum()],
    "Island":[(sid["type"] == "Island").sum(),(nid["type"] == "Island").sum(),(neid["type"] == "Island").sum(),(wid["type"] == "Island").sum(),(eid["type"] == "Island").sum(),(cid["type"] == "island").sum()],
        
}
df2 = pd.DataFrame(region_wise_Datasheet)
df2.to_csv("Tourism places.CSV",index=False)
df3 = pd.read_csv("C:/Users/pandy/Desktop/Himesh Pandya/Python/DS-AI/Projects/Tourism places.CSV",index_col= "Region",encoding="Latin1")
print(df3)

#graphs
plt.title("Tourism across the region of india")
plt.pie(region_count.values,labels= region_count.index,startangle = 90,autopct= "%1.1f%%")
plt.show()
plt.title("Tourism across the states of india")
plt.pie(state_count.values,labels= state_count.index,startangle = 90,autopct= "%1.1f%%")
plt.show()
c.heatmap(df3[["Tourism places","No. of States","Average duration days","Trek","Mountain","Valley","Village","Beach","Island"]],annot= True)#To show values
plt.show()
c.pairplot(df3)
plt.show()

#Alternate to
alt_series = df_main["alternative_to"].value_counts()
x_bar = alt_series.index
y_bar = alt_series.values
plt.xticks(rotation = 90)
plt.xlabel("main places",fontsize = 12)
plt.ylabel("number of places",fontsize= 12)

plt.title("Alternative places of main place",fontsize = 12)

plt.bar(x_bar,y_bar,width=3,color = "Orange")
plt.show()