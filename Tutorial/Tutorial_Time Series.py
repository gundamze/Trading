
from datetime import datetime
import time

now = datetime.now()
now
now.year
now.month
now.day

datetime(year=2012, month=8,day=4,hour=17,minute=9,second=21,microsecond=832092)

""" ########################## time difference ##########################  """
from datetime import timedelta

delta = now - datetime(2015,1,1)
delta     # timedelta type is the difference between two time
delta.days
delta.seconds

start = datetime(2011, 1, 7)
start + timedelta(12)     # add 12 days

"""  ########################## string and date ########################## """
stamp = datetime(2011, 1, 3)
str(stamp)                      # from datetime to str
stamp.strftime('%Y-%m-%d')      # control format of string

######## method 1
value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')  # from string to datetime

####### method 2
from dateutil.parser import parse
parse('Jan 31, 1997 10:45 PM')        # from str to datetime, it is better, because you don't need to write the format
parse('6/12/2011', dayfirst=True)

####### method 3
pd.to_datetime(value)

"""  ########################## tuple ########################## """

# time tuple to string
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
date_str = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)

# time tuple to datetime object
time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
dt_obj = datetime(*time_tuple[0:6])

# datetime object to time tuple
dt_obj = datetime(2008, 11, 10, 17, 53, 59)
time_tuple = dt_obj.timetuple()
print repr(time_tuple)

# string to time tuple
date_str = "2008-11-10 17:53:59"
time_tuple = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print repr(time_tuple)

# timestamp to time tuple in UTC
timestamp = 1226527167.595983
time_tuple = time.gmtime(timestamp)
print repr(time_tuple)

# timestamp to time tuple in local time
timestamp = 1226527167.595983
time_tuple = time.localtime(timestamp)
print repr(time_tuple)

# time tuple in local time to timestamp
time_tuple = (2008, 11, 12, 13, 59, 27, 2, 317, 0)
timestamp = time.mktime(time_tuple)
print repr(timestamp)

# time tuple in utc time to timestamp
time_tuple_utc = (2008, 11, 12, 13, 59, 27, 2, 317, 0)
timestamp_utc = calendar.timegm(time_tuple_utc)
print repr(timestamp_utc)



"""  ########################## date range ########################## """

pd.date_range('4/1/2012', '6/1/2012', freq = '2d')     # 2d means 2 day
pd.date_range('5/2/2012 12:56:31', periods = 20, freq = '1h30min')
pd.date_range(end='5/2/2012 12:56:31', periods=10, normalize = True)    # normalize is to just remain the y-m-d
pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')   # week of month, the Friday on 3rd week of each month

"""  ########################## time shift ########################## """

ts = Series(np.random.randn(4), index=pd.date_range('1/1/2000', periods=4, freq='M'))
ts.shift(2)               # shift the value
ts.shift(-2)
ts.shift(2, freq='M')     # shift the index

"""  ########################## operation ########################## """

from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)
now + 3 * Day()
now + MonthEnd(2)     # get the end of the date

offset = MonthEnd()
offset.rollforward(now)    # get the end of the this month
offset.rollback(now)       # get the end of the previous month


"""  ########################## monthly statistics ########################## """

ts = Series(np.random.randn(20), index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts
offset = MonthEnd()
ts.groupby(offset.rollforward).mean()      # get the monthly mean

### faster way
ts.resample('M', how='mean')

"""  ########################## Period ########################## """

p = pd.Period(2007, freq='A-DEC')     # full time span from January 1, 2007 to December 31, 2007,
p
p + 5
pd.Period('2014', freq='A-DEC') - p

rng = pd.period_range('1/1/2000', '6/30/2000', freq='M')    # period is also a time of "date time"
rng
Series(np.random.randn(6), index=rng)    # period used in series

index = pd.PeriodIndex(['2001Q3', '2002Q2', '2003Q1'], freq='Q-DEC')     # create a period index
index


