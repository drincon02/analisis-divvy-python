
import pandas as pd
import numpy as np

# MANIPULACION DE LOS DATOS /// DATA MANIPULATION

# Asignamos a una variable todos la data original /// we assign all original data to a variable

files = ["202008-divvy-tripdata.csv", "202009-divvy-tripdata.csv", "202010-divvy-tripdata.csv",
         "202011-divvy-tripdata.csv", "202012-divvy-tripdata.csv", "202101-divvy-tripdata.csv",
         "202102-divvy-tripdata.csv", "202103-divvy-tripdata.csv", "202104-divvy-tripdata.csv",
         "202105-divvy-tripdata.csv", "202106-divvy-tripdata.csv", "202107-divvy-tripdata.csv"]

# Creamos esta funcion para unir todos los archivos a un solo archivo con todos los datos /// We create the following function to join all files into one

def join_data (file):
    y = pd.DataFrame()
    for x in file:
        z = pd.read_csv(x)
        y = pd.concat([y, z])
    return y

# Esta funcion toma un dataframe o series y elimina sus duplicados y reemplaza las celdas vacias por NaN, la funcion tambien muestra como output el porcentaje de valores nulos de cada columna
# This function takes a dataframe or series and drops duplicates, replaces empty cell for NaN and prints a dataframe with the count and percentage of null values in each column

def manage_data (data, keep_duplicates):
    dataframe = pd.DataFrame(data)
    if keep_duplicates == False:
        dataframe = dataframe.drop_duplicates(keep="first")
    else:
        dataframe = dataframe.drop_duplicates(keep=False)
    dataframe = dataframe.dropna(how="all")
    dataframe = dataframe.replace(r"^\s*$", np.NaN, regex=True)
    null_vals = dataframe.isnull().sum()
    total_mis_vals_percent = 100 * dataframe.isnull().sum() / len(dataframe)
    mis_val_df = pd.concat([null_vals, total_mis_vals_percent], axis=1)
    print(mis_val_df)
    mis_val_df_columns = mis_val_df.rename(columns={0: 'Missing Values', 1: '% of Total Values'})
    mis_val_df_columns = mis_val_df_columns[mis_val_df_columns.iloc[:, 1] != 0].sort_values('% of Total Values', ascending=False).round(2)
    return dataframe

# Esta funcion da informacion basica acerca del dataframe
# This function gives basic info about a dataframe

def basic_info (dataframe):
    print(dataframe.head(5))
    print(dataframe.columns)
    print(dataframe.describe())
    dataframe.info()

# La siguiente funcion agrupa todos los datos de un dataframe en base a una columna especifica
# The following function groups all data of a dataframe by a specific column

def Group_Fast (dataframe, column_to_group, columns_to_show, operation):
    if operation == "count":
        finalname = dataframe.groupby(str(column_to_group))[columns_to_show].count()
    elif operation == "sum":
        finalname = dataframe.groupby(str(column_to_group))[columns_to_show].sum()
    elif operation == "mean":
        finalname = dataframe.groupby(str(column_to_group))[columns_to_show].mean()
    else:
        print("Operation not supported")
        return
    finalname = finalname.to_frame(name="Normal_Count")
    finalname["Percentage"] = finalname["Normal_Count"] / finalname["Normal_Count"].sum() * 100
    return finalname

#Aqui unimos toda la data original en un solo dataframe /// Here we join all data into one dataframe
cylist_data = join_data(files)

basic_info(cylist_data)

# Dos columnas del archivos que deberian ser de tiempo y fecha no son detectadas como tal por lo que las cambiamos
# Two columns are detected like objects when they should be datetime so we change those two columns

cylist_data["started_at"] = pd.to_datetime(cylist_data["started_at"])
cylist_data["ended_at"] = pd.to_datetime(cylist_data["ended_at"])

# Eliminamos duplicados /// We drop duplicates

cylist_data = manage_data(cylist_data, False)

# Eliminamos todos los registros donde la fecha de llegada sea menor o mas temprano que la fecha de salida ya que esto seria imposible
# We drop all rows where the ended_at datetime is lower or sooner than started_at as this is impossible

cylist_data = cylist_data[cylist_data.started_at < cylist_data.ended_at]

basic_info(cylist_data)

# Eliminamos las cuatro columnsa que denotan latitud y longitud ya que no podemos usar data que tenga el potencial de
# revelar informacion personal de los usuarios y no agrega informacion al analisis


# We drop four columns that could potentially reveal personnel information about users adn dont add info to the analysis

cylist_data = cylist_data.drop(["start_lat", "start_lng", "end_lat", "end_lng"], axis=1)

# Creamos una nueva columna que indica la duracion del viaje restando la fecha de llegada a la fecha de salida
# We create a new column that shows the length of each trip by substracting the ended_at column by the started_at column

cylist_data["trip_length"] = cylist_data.ended_at - cylist_data.started_at
basic_info(cylist_data)

# Creamos dos columnas nuevas que indican el dia de la semana en letras y el numero del mes
# We create two columns that indicate the day of the week in letters and the number of the month

cylist_data["day_of_week"] = cylist_data["started_at"].dt.day_name()
cylist_data["month"] = cylist_data["started_at"].dt.month

# ANALISIS DE DATOS /// DATA_ANALYSIS

# Separamos la data en dos grandes grupos, los registros que vienen de un usuario que es miembro
# y los registros que vienen de un usuario casual

# We split the joint data into two groups, one group that has all trips that are done by a member
# and another group that has all trips done by a casual user


cylist_members = cylist_data[cylist_data.member_casual == "member"]
cylist_casual = cylist_data[cylist_data.member_casual == "casual"]

# Para ver el numero de viajes por tipo de usuarios agrupamos la data unida por la columna "member_casual"
# To see the number of trips each user type did we group the joint data by the "member_casual" column

numbers_of_ride = Group_Fast(cylist_data, "member_casual", "ride_id","count")
print(numbers_of_ride)

# Para observar el tipo de bicicleta que usar cada tipo de usuario agrupamos la data separada previamente por la columna
# "rideable_type"

# To observe the type of bike used by each user type we group the previously split data by the "rideably_type" column

members_bycicles = Group_Fast(cylist_members, "rideable_type", "ride_id", "count")
casual_bycicles = Group_Fast(cylist_casual, "rideable_type", "ride_id", "count")
print(casual_bycicles)
print(members_bycicles)

# Ahora queremos conocer el promedio de la duracion del viaje para cada tipo de usuario
# Now we wanna see each user type average trip_length

duration_trip_members = np.array([cylist_members.trip_length.mean(numeric_only=False), cylist_members.trip_length.std(numeric_only=False)])
print(duration_trip_members)
duration_trip_casual = np.array([cylist_casual.trip_length.mean(numeric_only=False), cylist_casual.trip_length.std(numeric_only=False)])
print(duration_trip_casual)
difference_duration = duration_trip_members - duration_trip_casual
print(difference_duration)

# Ahora queremos conocer el numero de viaje por cada dia de la semana para cada tipo de usuario
# Now we wanna know the number of trips made in each day of the week by each user type

Total_Days = Group_Fast(cylist_data, "day_of_week", "ride_id","count")
print(Total_Days)
Members_Days = Group_Fast(cylist_members, "day_of_week", "ride_id", "count")
print(Members_Days)
Casual_Days = Group_Fast(cylist_casual, "day_of_week", "ride_id", "count")
print(Casual_Days)

# Ahora veremos cual es la duracion de viaje promedio de cada dia de la semana
# Here we'll see whats the average trip length for each day of the week

Daily_Trip_Length = Group_Fast(cylist_data, "day_of_week", "trip_length", "mean")
print(Daily_Trip_Length)
Members_Trip_Length = Group_Fast(cylist_members, "day_of_week", "trip_length", "mean")
print(Members_Trip_Length)
Casual_Trip_Length = Group_Fast(cylist_data, "day_of_week", "trip_length", "mean")
print(Casual_Trip_Length)

# Ahora veremos cual es la duracion de viaje promedio de cada mes
# Here we'll see whats the average trip length for each month

Monthly_Trip_Length = Group_Fast(cylist_data, "month", "trip_length", "mean")
print(Monthly_Trip_Length)
Monthly_Members_Trip_Length = Group_Fast(cylist_members, "month", "trip_length", "mean")
print(Monthly_Members_Trip_Length)
Monthly_Casuals_Trip_Length = Group_Fast(cylist_casual, "month", "trip_length", "mean")
print(Monthly_Casuals_Trip_Length)

# Con ya toda la data analizada vamos a llevar todos nuestros dataframes a csv para usarlos en PowerBi
# Now that we've finished our analysis we'll take all our dataframes to csv format to use them in PowerBi

cylist_data.to_csv("Cycling_Full_Data.csv")
Monthly_Casuals_Trip_Length.to_csv("Monthly_Casuals_Trip_Length.csv")
Monthly_Members_Trip_Length.to_csv("Monthly_Members_Trip_Length.csv")
Casual_Trip_Length.to_csv("Casual_Trip_Length.csv")
Members_Trip_Length.to_csv("Members_Trip_Length.csv")
Members_Days.to_csv("Members_days.csv")
Casual_Days.to_csv("Casual_Days.csv")
members_bycicles.to_csv("members_bycicles.csv")
casual_bycicles.to_csv("casual_bycicles.csv")
pd.DataFrame(duration_trip_casual).to_csv("duration_trip_casual.csv")
pd.DataFrame(duration_trip_members).to_csv("duration_trip_members.csv")
pd.DataFrame(difference_duration).to_csv("difference_duration.csv")
