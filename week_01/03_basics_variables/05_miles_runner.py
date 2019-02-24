'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''

distance_run_in_miles = 12/1.6
ttl_secs =  30*60 + 30

miles_p_sec = ttl_secs/distance_run_in_miles

miles_p_hr = miles_p_sec/60
print(f"Runner's average speed is {miles_p_hr} miles per hour")

