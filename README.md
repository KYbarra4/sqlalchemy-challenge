# sqlalchemy-challenge

## Query Data

View all of the classes that automap found

![sqlalchemy1](https://user-images.githubusercontent.com/113717031/205527936-009fc564-709b-4454-9536-1b5a6342010d.png)

Find the most recent date in the data set.

![sqlalchemy2](https://user-images.githubusercontent.com/113717031/205528002-3a4c7a6e-6e3f-4719-9627-196d5e21c095.png)

Design a query to retrieve the last 12 months of precipitation data and plot the results. 
Starting from the most recent data point in the database.
Calculate the date one year from the last date in data set.

![sqlalchemy3](https://user-images.githubusercontent.com/113717031/205528086-37295cac-fda8-4908-8e14-2d196412f1f4.png)

![sqlalchemy4](https://user-images.githubusercontent.com/113717031/205528269-9dc3f1a9-09e5-4859-bf53-103f5f528d3c.png)

![precipitation_data](https://user-images.githubusercontent.com/113717031/205529097-47023fa1-d706-4219-9436-790f65a94b92.png)

![sqlalchemy5](https://user-images.githubusercontent.com/113717031/205528294-8979c68a-92e1-40bb-a9c9-fb0e5da9b9c1.png)

![sqlalchemy6](https://user-images.githubusercontent.com/113717031/205528310-4639e8f9-102d-404e-8f1b-adae1de20db6.png)

![sqlalchemy7](https://user-images.githubusercontent.com/113717031/205528335-d3f2fb57-18c3-4213-9a3c-5b6836c78a81.png)

![sqlalchemy8](https://user-images.githubusercontent.com/113717031/205529168-47aa2075-65b5-4f18-821b-0bf6af57220a.png)

Using the most active station id
Query the last 12 months of temperature observation data for this station and plot the results as a histogram (bins=12)

![temperature_frequency](https://user-images.githubusercontent.com/113717031/205529197-b6001e97-74a4-4bb3-aa70-ff834d73cd3d.png)

## Climate App

1) Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
Start at the homepage.
List all the available routes.

![app_1](https://user-images.githubusercontent.com/113717031/205529507-af37915c-3d76-43d0-8d6b-e9ff1abc21a3.png)

2) Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.

![app_2](https://user-images.githubusercontent.com/113717031/205529568-6af24cac-33c1-45e8-98e6-cb2107216805.png)

3) Return a JSON list of stations from the dataset.

![app_3](https://user-images.githubusercontent.com/113717031/205529644-2730952d-09e2-4005-a5e5-ccce62926822.png)

4) Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.

![app_4](https://user-images.githubusercontent.com/113717031/205529720-eaca8da0-db30-48a9-9531-0130940fa48a.png)

5) Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

![app_5](https://user-images.githubusercontent.com/113717031/205529764-f4ab0165-fca9-4cac-886c-49fb00ac0c0d.png)

![app_6](https://user-images.githubusercontent.com/113717031/205529788-606dcfd2-ec7e-4656-8c57-1372aee5dc06.png)
