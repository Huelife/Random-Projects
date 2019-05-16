from statistics import mean
import datetime

mpg_dict = {

}
for key,value in mpg_dict.items():
  mpg_avg  = mean(value)
  print("Current mpg avg: {}".format(mpg_avg))
