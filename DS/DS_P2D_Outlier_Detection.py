
# Outlier Detection 
import pandas as pd
InputFileName = 'IP_DATA_CORE.csv'
OutputFileName = 'Retrieve_Router_Location.csv'
sFileName = '/content/IP_DATA_CORE.csv'
IP_DATA_ALL = pd.read_csv(sFileName,header=0,low_memory=False,usecols=['Country','Place.Name','Latitude','Longitude'], encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place.Name': 'Place_Name'}, inplace=True)
LondonData = IP_DATA_ALL.loc[IP_DATA_ALL['Place_Name']=='London']
AllData = LondonData[['Country', 'Place_Name','Latitude']]
print('All Data')
print(AllData)
MeanData = AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
StdData = AllData.groupby(['Country', 'Place_Name'])['Latitude'].std()
print('Outliers')
UpperBound = float(MeanData + StdData)
print('Higher than ', UpperBound)
OutliersHigher = AllData[AllData.Latitude > UpperBound]
print(OutliersHigher)
LowerBound = float(MeanData - StdData)
print('Lower than ', LowerBound)
OutliersLower = AllData[AllData.Latitude < LowerBound]
print(OutliersLower)
print('Not Outliers')
OutliersNot = AllData[(AllData.Latitude >= LowerBound) & (AllData.Latitude <= UpperBound)]
print(OutliersNot)