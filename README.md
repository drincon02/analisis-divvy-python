# Cyclist Data Analysis

## Basic Information:

This is the data analysis documentation for the cyclist company, a fictitious company located in Chicago which offers a shared bike system with a total of 5824 bicycles and 692 stations spread throughout Chicago.
The company has three main pricing plans:
• Bike pass
• Full Day pass
• Annual membership

The company's finance department has determined that its most profitable pricing plan is the annual membership. Customers who purchase this membership are called Cyclist Members by the company while what the other two pricing plans use are called casual users.
Flexibility in pricing plans has been one of the reasons for the company's success, but they still need to maximize the number of annual memberships sold.
The marketing department realizes that most casual users are already aware of the annual membership, so they set about converting these casual users to Cyclist Members.

For this, marketing needs to know the answer to 3 key questions:
1. How does the use of Cyclist bikes by casual users and Cyclist members differ?
2. Why would casual users buy an annual membership?
3. How Cyclist can use digital media to influence casual users to become annual members.

I was tasked with solving the company's first question using user trip data from the last 12 months.
The data to be used is published in the following link https://divvy-tripdata.s3.amazonaws.com/index.html , (the name of the company in the data is different from the name of the company in this case due to this data being taken from a real company under this license https://www.divvybikes.com/data-license-agreement .)
With this dataset it is prohibited to correlate data with real names, addresses among other personal data.

## Data manipulation:
Considering that it is a large data with millions of rows or records i could use various tools such as Excel with Power Pivot and Access, SQL, Python or R.
For this case I am going to use the Python programming language for data manipulation since it is capable of handling large amounts of data, and I will also use PowerBi to make graphs.
To see the data manipulation in detail I recommend you review the following Python script whis is at main.py

## Final Analysis:
The objective of our analysis is to know how the use of bikes differs between casual users and members.
The first thing I want to know is what type of users make the most trips in total.

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/Imagen2.png)

In the previous graph I can see that 55% of the trips are made by members while 44% are made by casual users, this by itself it is not enough to know which users are more active.

The second question I ask myself when I see this is what type of bikes do users use for their trips?

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/Imagen1.png)

With this graph I can see that casual users don’t have a clear preference for one bike, as the docked bike it’s the most used with a low difference with classic bike while for the members there is a clear preference for classic bikes.
Knowing this, I must now know on which day of the week users are most active.

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/Imagen3.png)

With this graph i can see that the number of trips per day is constant for members while casual users have a low number of trips on weekdays and a very high number on weekends, especially on Saturday.
Now i want to know the average number of minutes per trip for each user type and for each day of the week.

![Image text](https://github.com/drincon02/analisis-divvy/blob/main/image.png)

In this graph I can see that casual users’ trips are longer than members trips, reaching their maximum average duration at the weekend around 45 minutes per trip, while for the members maximum average duration per trip only takes between 15 and 20 minutes.
It is important to know that the standard deviations of the average trip duration are high for both casual users and members, for casual users there is a standard deviation of 5 hours while for members there is a standard deviation of 50 minutes.

## Conclusions and recommendations:
Based on the analysis made, I could not draw any important conclusions due to not being able to link the data between specific users, but I was able to gain the following insights:
- Casual users frequently take trips on weekends, so a marketing attempt on the weekends at bicycle stands would be interesting, or perhaps increasing the price of the service on weekends for casual users.

- Members have a high preference over classic bikes while casual users do not have a strong preference although they make more trips on docked bikes.

- The average trip duration for casual users is higher than the average trip duration for members, but casual users also have a higher standard deviation than that of the members, so casual user’s trips are more unpredictable and longer than members.
