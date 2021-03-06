#mpg_avg.py: My car's mpg and the date it was calculated

from statistics import mean

#dictionary for mpg by date
mpg_dict = {
  "04/12/18": 18.3,
  "04/14/18": 21.6,
  "04/20/18": 18.6,
  "04/27/18": 16.1,
  "05/17/18": 17.8,
  "06/01/18": 18.6,
  "06/24/18": 19.0,
  "07/13/18": 18.6,
  "08/03/18": 18.7,
  "08/24/18": 18.8,
  "10/07/18": 18.6,
  "10/29/18": 17.9,
  "11/10/18": 19.1,
  "11/30/18": 18.0,
  "12/11/18": 14.3,
  "12/17/18": 16.0,
  "12/26/18": 19.3,
  "01/04/19": 18.7,
  "01/17/19": 17.6,
  "01/24/19": 19.2,
  "01/31/19": 19.7,
  "02/13/19": 21.6,
  "02/28/19": 22.9,
  "03/13/19": 22.3,
  "04/02/19": 21.2,
  "04/17/19": 20.9,
  "05/02/19": 22.5,
  "05/21/19": 22.1,
}

#adding all mpg values, averaging them, and printing them
mpg_add = [mpg_dict[key] for key in mpg_dict]
mpg_avg  = round((mean(mpg_add)),1)

print("Current mpg avg: {}.".format(mpg_avg))
