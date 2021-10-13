import datetime
import pandas as pd
import numpy as np
dti = pd.to_datetime(['1/1/2018',np.datetime64("2018-01-01"),datetime.datetime(2018, 1, 1)])
dti

dtim = pd.to_datetime(datetime.datetime.strptime('1*1*2020', '%d*%m*%Y'))
dtim2 = dtim.day_name()+ pd.offsets.BDay()
dtim2

dt = dti.tz_localize('UTC')
dt

dt.tz_convert('US/Pacific')

an_day = pd.Timestamp('2018-01-05')
an_day.day_name()

an_day2 = an_day +pd.Timedelta('2 day')
an_day2.day_name()

an_day3 = an_day + pd.offsets.BDay()
an_day3.day_name()

pd.Timestamp(datetime.datetime(2015,8,1))
pd.Timestamp('2015-09', freq='D')
pd.Timestamp("2012-05-01").days # error
pd.Timestamp("2012-05-01") 

import datetime
date = datetime.datetime.strptime("2012-05-01", '%Y-%m-%d')
date
date.day


pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]))
pd.to_datetime('2010-11/12', format= '%Y-%m/%d')
pd.to_datetime("2005/11/23").days # error


start = datetime.datetime(2011,1,1)
end = datetime.datetime(2020,1,1)
index = pd.date_range(start,end)
index

index2 = pd.bdate_range(start,end)
index2