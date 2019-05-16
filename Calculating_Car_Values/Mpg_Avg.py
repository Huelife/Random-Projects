from statistics import mean

mpg = {

}
for key,value in mpg.items():
  mpg_avg  = mean(mpg[value])
  print("Current mpg avg: {}".format(mpg_avg))