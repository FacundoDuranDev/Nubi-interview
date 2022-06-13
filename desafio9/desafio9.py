import datetime
def generateLastDaysPaths(date,days):
    dia = datetime.datetime.strptime(date,"%Y%m%d")
    resta = datetime.timedelta(days=1)
    list_path = list()
    for i in range(days):
        list_path.append("https://importantdata@location/{}/{}/{}/".format(dia.year,dia.month,dia.day))

        dia = dia-resta
    return list(reversed(list_path))

