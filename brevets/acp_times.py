"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.

max_speed = {0:34, 200:32, 400:30, 600:28, 800:28, 1000:26}
min_speed = {0:15, 200:15, 400:15, 600:11.428, 800:11.428, 1000:11.333}
def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    i=0
    open_min=0
    open_hour = 0
    if control_dist_km >= brevet_dist_km:
    	return None
    while (control_dist_km >= 200):
    	hr = 200// max_speed[i*200]
    	open_hour += hr
    	open_min += (200 / max_speed[i * 200] - hr) * 60
    	i += 1
    	control_dist_km -=  200

    hr = control_dist_km // max_speed[i * 200]
    open_hour += hr
    open_min += (control_dist_km / max_speed[i * 200] - hr) * 60
    start = arrow.get(brevet_start_time).shift(hours=+open_hour, minutes=+open_min)
    print("open hour: {}, open min: {}".format(open_hour, open_min))
    return start


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km >= brevet_dist_km:
    	return None
    if control_dist_km != 0:
    	i = 0
    	close_hour = 0
    	close_min = 0
    	while (control_dist_km >= 200):
       		hr = 200 // min_speed[i*200]
        	close_hour += hr
        	close_min += (200 / min_speed[i*200] - hr) * 60
        	i += 1
        	control_dist_km -= 200


    	hr = control_dist_km // min_speed[i * 200]
    	close_hour += hr
    	close_min += (control_dist_km / min_speed[i * 200] - hr) * 60
    	close = arrow.get(brevet_start_time).shift(hours=+close_hour, minutes=+close_min)
    else:
    	close = arrow.get(brevet_start_time).shift(hours=+1)
    
    return close

#checking soely in the program whether it works
open_time(900, 1000, arrow.get(2017,1,1))
close_time(900, 1000, arrow.get(2017,1,1))








