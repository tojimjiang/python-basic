#km/s speed of light
km_whole = 299792.458
#kilometer conversion
miles_convert = 0.621
#kilometers to miles
miles_whole = km_whole*miles_convert
#half of the speed in miles
miles_half = miles_whole / 2
#one fourth of the speed in miles
miles_quarter = miles_half / 2
#earth speed
earth = 66600
#earth to km conversion
earth_km = earth / miles_convert
#number of seconds in one hour
hour_seconds=3600
#convert to per seond
earth_sec = earth_km / hour_seconds
#percentage of the earth as speed of light
earth_per = earth_sec / km_whole * 100
#earth's speed as a string (for the comma)
earth_s = format(earth, ',d')
#unit shorthand
k = 'kps'
m = 'mps'
#more shorthand for static data
mile_hr = ' miles per hour is equal to:'
#data/message compacting
per_sec = '/ sec):'
miles = ' (Miles '
speed = 'peed of light'
msg = speed + miles + per_sec
#recombination of words into full static massages
km_msg = 'S' + speed + ' (Kilometers ' + per_sec
miles_msg = 'S' + msg
half_msg = 'Half s' + msg
quarter_msg = 'Quarter s' + msg
earth_hr = earth_s + mile_hr
#printing first 4 statements
print(format(km_msg ,'<37s'), km_whole, k)
print(format(miles_msg ,'<37s'), miles_whole, m)
print(format(quarter_msg ,'<37s'), miles_half, m)
print(format(earth_hr, '<37s'), miles_quarter, m) 
#line break
print()
#earth's speed print function
print('The earth moves', earth_s ,'miles / hour around the sun.')
print(format(earth_hr, '<37s'), earth_sec, k)
print(format(earth_hr, '<37s'), earth_per, ' of the speed of light')
