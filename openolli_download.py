#import packages
from urllib.request import urlretrieve

#range from 2 to 11 (included), 12 is excluded
for i in range(10, 12):
	url = 'https://openolli.innoz.space/vehicle_states/2018_'+"{0:0=2d}".format(i)+'.csv'
	urlretrieve(url, '2018_0'+str(i)+'.csv')
	

