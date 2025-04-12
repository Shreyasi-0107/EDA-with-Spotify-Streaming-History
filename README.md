Spotify-Streaming-History-EDA
📌 Overview
This repository contains an exploratory data analysis (EDA) project based on personal Spotify Streaming History data. The goal is to uncover insights into music listening habits, preferences, and behavioral patterns over time. By analyzing the streaming data, this project helps identify top artists, peak listening hours, completion rates, and platform usage, offering a comprehensive view of the user’s music consumption trends.

The analysis incorporates key data preprocessing steps including data type conversion, handling missing values, and timestamp extraction. Multiple visualization techniques are employed to highlight listening frequency, completion behavior, and engagement across platforms and time periods.

🎯 Key Objectives
Listening Habits Over Time
Analyze how many songs were streamed on each day and identify high and low listening periods.

Top Artists by Listening Time
Determine which artists the user spent the most time listening to by calculating total playback hours.

Relationship Between Song Duration and Time of Day
Explore whether the user prefers longer or shorter tracks at different times using scatter plots.

Platform Usage Analysis
Examine which devices or platforms (e.g., Android, Web Player, iOS) were most frequently used for streaming.

Daily Stream Count Trends
Track how daily stream counts change over time and detect long-term listening trends.

⚙️ Features
Exploratory Data Analysis (EDA)
Includes summary statistics, missing value checks, feature engineering (e.g., time extraction), and more.

Visualizations
Multiple Matplotlib charts including histograms, scatter plots, pie charts, and line plots to communicate insights clearly.

Behavioral Patterns
Discover when, how, and what type of content the user consumes most, and identify habits like song-skipping or platform switching.

📂 Dataset
The dataset is exported from the Spotify platform using its personal data export tool. It consists of two files:

spotify_history.csv: Contains detailed logs of each track played including timestamp, duration, artist, platform, and device info.

spotify_data_dictionary.csv: Describes each column in the dataset and its meaning.

Key Info:

~25,000 records

16 columns

File size: ~4.3 MB

Time span: Multiple months of data

Granular metadata including skip status, connection type, and more

📦 Prerequisites
To run this analysis, the following Python libraries are required:

pandas – for data manipulation

matplotlib – for visualization

Install them using:
pip install pandas matplotlib
