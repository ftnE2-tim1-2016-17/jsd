from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot
import os
import datetime


class Query(object):

    def __init__(self):
        self.query_set = {}

    def interpreter(self, model):

        service_type = model.serviceType
        service_item = model.serviceItem.car

        self.query_set["serviceType"] = service_type
        self.query_set["serviceItem"] = service_item
        parameters = model.parameters
        date_from_check = False
        time_from_check = False
        date_to_check = True
        time_to_check = True

        for param in parameters:
            if param.city is not None:
                city = param.city
                self.query_set["city"] = city
            if param.dateFrom is not None:
                date_from_check = True
                date_to_check = False
                date_from = param.dateFrom
                day_from = int(date_from.dateFrom.day.number)
                if date_from.dateFrom.month is not None:
                    month_from = int(date_from.dateFrom.month.number)
                    if (month_from == 1) | (month_from == 3) | (month_from == 5) | (month_from == 7) | (month_from == 8)\
                            | (month_from == 10) | (month_from == 12):
                        if (day_from < 1) | (day_from > 30):
                            raise ValueError("Uneli ste nepostojeci dan za datum iznajmljivanja vozila.")
                    elif month_from == 2:
                        if (day_from < 1) | (day_from > 28):
                            raise ValueError("Uneli ste nepostojeci dan za datum iznajmljivanja vozila.")
                    elif (month_from == 4) | (month_from == 6) | (month_from == 9) | (month_from == 11):
                        if (day_from < 1) | (day_from > 30):
                            raise ValueError("Uneli ste nepostojeci dan za datum iznajmljivanja vozila.")
                    else:
                        raise ValueError("Uneli ste nepostojeci mjesec za datum iznajmljivanja vozila.")
                else:
                    month_from = datetime.datetime.now().month
                if date_from.dateFrom.year is not None:
                    year_from = int(date_from.dateFrom.year.number)
                    if year_from < datetime.datetime.now().year:
                        raise ValueError("Godina iznajmljivanja ne moze biti manja od tekuce.")
                else:
                    year_from = datetime.datetime.now().year
                if year_from == datetime.datetime.now().year:
                    if month_from < datetime.datetime.now().month:
                        raise ValueError("Mjesec iznajmljivanja ne moze biti manji od tekuceg.")
                    elif month_from == datetime.datetime.now().month:
                        if day_from < datetime.datetime.now().day:
                            raise ValueError("Dan iznajmljivanja ne moze biti manji od tekuceg.")
                self.query_set["dayFrom"] = day_from
                self.query_set["monthFrom"] = month_from
                self.query_set["yearFrom"] = year_from

            if not date_from_check:
                date_from_check = True
                date_to_check = False
                day_from = datetime.datetime.now().day
                month_from = datetime.datetime.now().month
                year_from = datetime.datetime.now().year
                self.query_set["dayFrom"] = day_from
                self.query_set["monthFrom"] = month_from
                self.query_set["yearFrom"] = year_from

            if param.timeFrom is not None:
                time_from = param.timeFrom
                time_from_check = True
                time_to_check = False
                hour_from = int(time_from.timeFrom.hour.number)
                self.query_set["hourFrom"] = hour_from
                if time_from.timeFrom.minute is not None:
                    minute_from = int(time_from.timeFrom.minute.number)
                else:
                    minute_from = 0
                self.query_set["minuteFrom"] = minute_from
            if not time_from_check:
                time_from_check = True
                time_to_check = False
                hour_from = int(datetime.datetime.now().time().hour + 1)
                minute_from = 30
                self.query_set["hourFrom"] = hour_from
                self.query_set["minuteFrom"] = minute_from

            if param.dateTo is not None:
                date_to_check = True
                date_to = param.dateTo
                day_to = int(date_to.dateTo.day.number)
                if date_to.dateTo.month is not None:
                    month_to = int(date_to.dateTo.month.number)
                    if (month_to == 1) | (month_to == 3) | (month_to == 5) | (month_to == 7) | (month_to == 8) | \
                            (month_to == 10) | (month_to == 12):
                        if (day_to < 1) | (day_to > 30):
                            raise ValueError("Uneli ste nepostojeci dan za datum vracanja vozila.")
                    elif month_to == 2:
                        if (day_to < 1) | (day_to > 28):
                            raise ValueError("Uneli ste nepostojeci dan za datum vracanja vozila.")
                    elif (month_to == 4) | (month_to == 6) | (month_to == 9) | (month_to == 11):
                        if (day_to < 1) | (day_to > 30):
                            raise ValueError("Uneli ste nepostojeci dan za datum vracanja vozila.")
                    else:
                        raise ValueError("Uneli ste nepostojeci mjesec za datum vracanja vozila.")
                else:
                    month_to = datetime.datetime.now().month
                if date_to.dateTo.year is not None:
                    year_to = int(date_to.dateTo.year.number)
                    if year_to < datetime.datetime.now().year:
                        raise ValueError("Godina vracanja ne moze biti manja od tekuce.")
                else:
                    year_to = datetime.datetime.now().year
                if year_to == datetime.datetime.now().year:
                    if month_to < datetime.datetime.now().month:
                        raise ValueError("Datum vracanja(mjesec) ne moze biti manji od tekuceg.")
                    elif month_to == datetime.datetime.now().month:
                        if day_to < datetime.datetime.now().day:
                            raise ValueError("Datum vracanja(dan) ne moze biti manji od tekuceg.")
                self.query_set["dayTo"] = day_to
                self.query_set["monthTo"] = month_to
                self.query_set["yearTo"] = year_to
            if not date_to_check:
                date_to_check = True
                day_to = self.query_set["dayFrom"] + 1
                month_to = datetime.datetime.now().month
                year_to = datetime.datetime.now().year
                self.query_set["dayTo"] = day_to
                self.query_set["monthTo"] = month_to
                self.query_set["yearTo"] = year_to

            if param.timeTo is not None:
                time_to = param.timeTo
                time_to_check = True
                hour_to = int(time_to.timeTo.hour.number)
                self.query_set["hourTo"] = hour_to
                if time_to.timeTo.minute is not None:
                    minute_to = int(time_to.timeTo.minute.number)
                else:
                    minute_to = 0
                self.query_set["minuteTo"] = minute_to
            if not time_to_check:
                time_from_check = True
                hour_to = self.query_set["hourFrom"]
                minute_to = self.query_set["minuteFrom"]
                self.query_set["hourTo"] = hour_to
                self.query_set["minuteTo"] = minute_to

            if param.itemParameters is not None:
                if param.itemParameters.carParameters is not None:
                    for itemParam in param.itemParameters.carParameters:
                        if itemParam.carBrand is not None:
                            carBrand = itemParam.carBrand
                        if itemParam.fuelType is not None:
                            fuelType = itemParam.fuelType
                        if itemParam.gearbox is not None:
                            gearbox = itemParam.gearbox
                        if itemParam.carClass is not None:
                            carClass = itemParam.carClass
                        if itemParam.priceFrom is not None:
                            priceFrom = itemParam.priceFrom
                        if itemParam.priceTo is not None:
                            priceTo = itemParam.priceTo

        print(self.query_set)
        return self.query_set


def to_lower_case(file_name):
    var = ""
    with open(file_name) as f:
        file_str = f.read()
        for line in file_str:
            line = line.lower()
            var += line

    with open(file_name, 'w') as f:
        f.write(var)


def execute(path, grammar_file_name, example_file_name, export_dot, export_png):

    meta_path = os.path.join(path, grammar_file_name)
    meta_name = os.path.splitext(meta_path)[0]
    metamodel = metamodel_from_file(meta_path)

    if export_dot:
        metamodel_export(metamodel, meta_name + '.dot')
        if export_png:
            graph = pydot.graph_from_dot_file(meta_name + '.dot')
            graph[0].write_png(meta_name + '.png')

    to_lower_case(example_file_name)
    model_path = os.path.join(path, example_file_name)
    model_name = os.path.splitext(model_path)[0]

    model = metamodel.model_from_file(model_path)

    if export_dot:
        model_export(model, model_name + '.dot')
    if export_png:
        graph = pydot.graph_from_dot_file(model_name + '.dot')
        graph[0].write_png(model_name + '.png')

    query = Query()
    query_set = query.interpreter(model)
    #provjeriri za granicne uslove kod datuma iznajmjivanja i vrcanja vozila,
    #kao i poredjenje datuma iznajmljivanja < datuma vracanja
    #return query_set


