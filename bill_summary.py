import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
#print(tips)

df = pd.DataFrame(tips)
#EDA - Exploratory Data Analysis
print(df)
print(df.head(10))
print(df.info())
print(df.describe())
print("\n Missing values: \n", df.isnull().sum())
print("\n Tip by day: \n", df.groupby("day",observed=True)["tip"].sum())
tip_summary = df.groupby(["day","time"],observed=True)["tip"].sum()
print("\nTip summary: \n", tip_summary)

bill_summary_ex_tip = df.groupby(["day","time"],observed=True)["total_bill"].sum()
print("\n bill_summary excluding tip: \n ", bill_summary_ex_tip)

df["total_bill_in_tip"] = df["total_bill"]+df["tip"]
print("bill including tip: \n",df["total_bill_in_tip"])
print("\n bill summary including tip by day and time: \n", df.groupby(["day","time"],observed=True)["total_bill_in_tip"].sum())
print("\n bill summary including tip by day: \n", df.groupby(["day"],observed=True)["total_bill_in_tip"].sum())
best_day = df.groupby(["day"],observed=True)["total_bill_in_tip"].sum().idxmax()
print("\n best day for earning is : ",best_day)
worst_day = df.groupby(["day"],observed=True)["total_bill_in_tip"].sum().idxmin()
print("\n Worst day for earning is : ", worst_day)

df["tip_percent"] = (df["tip"]/df["total_bill"])*100
print(df["tip_percent"])
average_tip_percent = df.groupby("day", observed=True)["tip_percent"].mean()
print("\n Average tip percent: ",df.groupby("day", observed=True)["tip_percent"].mean())
print("\n Day with most generous customers : \n", average_tip_percent.idxmax())

plt.figure(figsize=(10,5))

average_tip_percent.sort_values().plot(kind="bar", color="green")
plt.title("Average tip percent")
plt.xlabel("Day")
plt.ylabel("Tip percent")
plt.tight_layout()
plt.show()
sns.boxplot(x="time", y="tip", data=df)
plt.title("tip distribution by time of day")
plt.show()
sns.boxplot(x="sex", y= "day", data =df)
plt.title("gender distribution by time of day")
plt.show()