import datetime
def generateMonthlyPathList(year, month, day):
    dia = datetime.datetime.strptime('{}{}{}'.format(year,month,day),"%Y%m%d")
    resta = datetime.timedelta(days=1)
    current_month = dia.month
    list_path = list()
    while dia.month == current_month:
        list_path.append("https://importantdata@location/{}/{}/{}/".format(dia.year,dia.month,dia.day))
        dia = dia - resta
    return list_path