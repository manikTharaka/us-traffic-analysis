import pandas as pd
import gc

cols =[
 'traffic_volume_counted_after_0000_to_0100',
 'traffic_volume_counted_after_0100_to_0200',
 'traffic_volume_counted_after_0200_to_0300',
 'traffic_volume_counted_after_0300_to_0400',
 'traffic_volume_counted_after_0400_to_0500',
 'traffic_volume_counted_after_0500_to_0600',
 'traffic_volume_counted_after_0600_to_0700',
 'traffic_volume_counted_after_0700_to_0800',
 'traffic_volume_counted_after_0800_to_0900',
 'traffic_volume_counted_after_0900_to_1000',
 'traffic_volume_counted_after_1000_to_1100',
 'traffic_volume_counted_after_1100_to_1200',
 'traffic_volume_counted_after_1200_to_1300',
 'traffic_volume_counted_after_1300_to_1400',
 'traffic_volume_counted_after_1400_to_1500',
 'traffic_volume_counted_after_1500_to_1600',
 'traffic_volume_counted_after_1600_to_1700',
 'traffic_volume_counted_after_1700_to_1800',
 'traffic_volume_counted_after_1800_to_1900',
 'traffic_volume_counted_after_1900_to_2000',
 'traffic_volume_counted_after_2000_to_2100',
 'traffic_volume_counted_after_2100_to_2200',
 'traffic_volume_counted_after_2200_to_2300',
 'traffic_volume_counted_after_2300_to_2400']

cols = ['fips_state_code','station_id'] + cols 
df = pd.read_csv("data/dot_traffic_2015.txt.gz",usecols=cols)

df = df.groupby(['fips_state_code','station_id']).sum()
gc.collect()

cols = ['fips_state_code','station_id','fips_county_code','latitude','longitude']
stations = pd.read_csv("data/dot_traffic_stations_2015.txt.gz",usecols=cols)

df = pd.merge(df,stations,on=['fips_state_code','station_id'])
gc.collect()

df.to_csv('data/county_sum.csv',index=False)
