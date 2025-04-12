import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Shreyasi\OneDrive\Documents\4th sem\INT375\project\spotify_history.csv")

#OBJECTIVE 1 : Most streamed Artists and Tracks(Bar plot)
#**Artists**#
plt.figure(figsize=(10,6))
top_artists= df['artist_name'].value_counts().head(10).plot(kind='bar',color='navy')
plt.title("Top 10 Most Streamed Artists",fontsize=15)
plt.xlabel("Stream Count",fontsize=12)
plt.ylabel("Artist",fontsize=12)
plt.tight_layout()
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()
#**Tracks**#
plt.figure(figsize=(10,6))
top_tracks=df['track_name'].value_counts().head(10).plot(kind='bar',color='firebrick')
plt.title("Top 10 Most Streamed Tracks")
plt.xlabel("Stream Count",fontsize=12)
plt.ylabel("Tracks",fontsize=12)
plt.tight_layout()
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

#OBJECTIVE 2 : Listening Habits over Time(Histogram)
plt.figure(figsize=(10,6))
df['ts']=pd.to_datetime(df['ts']) #convert timestamp column to datetime
df['hour']=df['ts'].dt.hour     #extract hour of the day
plt.hist(df['hour'],bins=20,color='indigo',edgecolor='black')
plt.title("Listening Habits by Hour of Day",fontsize=15)
plt.xlabel("Hour of Day(0-23)",fontsize=12)
plt.ylabel("Nnumber of Streams",fontsize=12)
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()

#OBJECTIVE 3 : Track Completion Rataes(Scatter Plot)
plt.figure(figsize=(10,6))
plt.scatter(df['hour'],df['ms_played'],alpha=0.5,color='forestgreen')
plt.xlabel("Track Duration (ms)")
plt.ylabel("Time Played (ms)")
plt.title("Listening Time vs Hour of the Day")
plt.grid(True)
plt.tight_layout()
plt.show()

# OBJECTIVE 4 : Platform Usage Analysis(Pie Chart)
plt.figure(figsize=(10,6))
df['platform'].value_counts().plot(kind='pie',autopct='%1.1f%%',colors=plt.cm.Paired.colors,labeldistance=1.7,pctdistance=1.3)
plt.title("Platform Usage Distribution")
plt.ylabel("equal")
plt.show()

#OBJECTIVE 5 : Duration of Listening Sessions(Line plot)
plt.figure(figsize=(10,6))
df['date']= df['ts'].dt.date
daily_play=df.groupby('date')['ms_played'].sum()  #Groupby date and sum up the ms_played per day
daily_play_hours=daily_play/(1000*60*60)  #convert milliseconds to hours
daily_play_hours=daily_play_hours.head(20) #first 20 records
plt.plot(daily_play_hours.values,marker='d',linestyle='solid',color='crimson')
plt.title("Listening Duration Sessions")
plt.xlabel("Record Index(Day)")
plt.ylabel("Hours Listened")
plt.show()
