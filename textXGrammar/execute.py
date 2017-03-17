from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot
import os
import datetime


class Query(object):
    def __init__(self):
        self.query_set = {}

    def interpreter_for_rent_a_car(self, model):

        service_type = model.serviceType
        service_item = model.serviceItem.car
        self.query_set["serviceType"] = service_type
        self.query_set["serviceItem"] = service_item
        self.query_set["city"] = 0
        self.query_set["dayFrom"] = datetime.datetime.now().day
        self.query_set["monthFrom"] = datetime.datetime.now().month
        self.query_set["yearFrom"] = datetime.datetime.now().year
        self.query_set["hourFrom"] = int(datetime.datetime.now().time().hour + 1)
        self.query_set["minuteFrom"] = 30
        self.query_set["dayTo"] = self.query_set["dayFrom"] + 1
        self.query_set["monthTo"] = self.query_set["monthFrom"]
        self.query_set["yearTo"] = self.query_set["yearFrom"]
        self.query_set["hourTo"] = self.query_set["hourFrom"]
        self.query_set["minuteTo"] = self.query_set["minuteFrom"]
        self.query_set["carBrand"] = 0
        self.query_set["fuelType"] = 0
        self.query_set["gearbox"] = 0
        self.query_set["carClass"] = 0
        self.query_set["priceFrom"] = 0
        self.query_set["priceTo"] = 0

        parameters = model.parameters

        date_to_check = False
        for param in parameters:
            if param.city is not None:
                city = param.city
                self.query_set["city"] = city
            if param.dateFrom is not None:
                date_to_check = True
                date_from = param.dateFrom
                day_from = int(date_from.dateFrom.day)
                if date_from.dateFrom.month is not None:
                    month_from = int(date_from.dateFrom.month)
                    if (month_from == 1) | (month_from == 3) | (month_from == 5) | (month_from == 7) | (month_from == 8) \
                            | (month_from == 10) | (month_from == 12):
                        if (day_from < 1) | (day_from > 31):
                            return "Uneli ste nepostojeci dan za datum iznajmljivanja vozila."
                    elif month_from == 2:
                        if (day_from < 1) | (day_from > 28):
                            return "Uneli ste nepostojeci dan za datum iznajmljivanja vozila."
                    elif (month_from == 4) | (month_from == 6) | (month_from == 9) | (month_from == 11):
                        if (day_from < 1) | (day_from > 30):
                            return "Uneli ste nepostojeci dan za datum iznajmljivanja vozila."
                    else:
                        return "Uneli ste nepostojeci mjesec za datum iznajmljivanja vozila."
                else:
                    month_from = datetime.datetime.now().month
                if date_from.dateFrom.year is not None:
                    year_from = int(date_from.dateFrom.year)
                    if year_from < datetime.datetime.now().year:
                        return "Godina iznajmljivanja ne moze biti manja od tekuce."
                else:
                    year_from = datetime.datetime.now().year
                if year_from == datetime.datetime.now().year:
                    if month_from < datetime.datetime.now().month:
                        return "Mjesec iznajmljivanja ne moze biti manji od tekuceg."
                    elif month_from == datetime.datetime.now().month:
                        if day_from < datetime.datetime.now().day:
                            return "Dan iznajmljivanja ne moze biti manji od tekuceg."
                self.query_set["dayFrom"] = day_from
                self.query_set["monthFrom"] = month_from
                self.query_set["yearFrom"] = year_from

            if param.timeFrom is not None:
                time_from = param.timeFrom
                hour_from = int(time_from.timeFrom.hour)
                self.query_set["hourFrom"] = hour_from
                if time_from.timeFrom.minute is not None:
                    minute_from = int(time_from.timeFrom.minute)
                    self.query_set["minuteFrom"] = minute_from

            if param.dateTo is not None:
                date_to = param.dateTo
                day_to = int(date_to.dateTo.day)
                if date_to.dateTo.month is not None:
                    month_to = int(date_to.dateTo.month)
                    if (month_to == 1) | (month_to == 3) | (month_to == 5) | (month_to == 7) | (month_to == 8) | \
                            (month_to == 10) | (month_to == 12):
                        if (day_to < 1) | (day_to > 30):
                            return "Uneli ste nepostojeci dan za datum vracanja vozila."
                    elif month_to == 2:
                        if (day_to < 1) | (day_to > 28):
                            return "Uneli ste nepostojeci dan za datum vracanja vozila."
                    elif (month_to == 4) | (month_to == 6) | (month_to == 9) | (month_to == 11):
                        if (day_to < 1) | (day_to > 30):
                            return "Uneli ste nepostojeci dan za datum vracanja vozila."
                    else:
                        return "Uneli ste nepostojeci mjesec za datum vracanja vozila."
                else:
                    month_to = datetime.datetime.now().month
                if date_to.dateTo.year is not None:
                    year_to = int(date_to.dateTo.year)
                    if year_to < datetime.datetime.now().year:
                        return "Godina vracanja ne moze biti manja od tekuce."
                else:
                    year_to = datetime.datetime.now().year
                if year_to == datetime.datetime.now().year:
                    if month_to < datetime.datetime.now().month:
                        return "Datum vracanja(mjesec) ne moze biti manji od tekuceg."
                    elif month_to == datetime.datetime.now().month:
                        if day_to < datetime.datetime.now().day:
                            return "Datum vracanja(dan) ne moze biti manji od tekuceg."
                self.query_set["dayTo"] = day_to
                self.query_set["monthTo"] = month_to
                self.query_set["yearTo"] = year_to

            if date_to_check:
                date_to_check = False
                self.query_set["dayTo"] = self.query_set["dayFrom"] + 1
                self.query_set["monthTo"] = self.query_set["monthFrom"]
                self.query_set["yearTo"] = self.query_set["yearFrom"]

            if param.timeTo is not None:
                time_to = param.timeTo
                hour_to = int(time_to.timeTo.hour)
                self.query_set["hourTo"] = hour_to
                if time_to.timeTo.minute is not None:
                    minute_to = int(time_to.timeTo.minute)
                    self.query_set["minuteTo"] = minute_to

            if param.priceFrom is not None:
                price_from = int(param.priceFrom.number)
                self.query_set["priceFrom"] = price_from
            if param.priceTo is not None:
                price_to = int(param.priceTo.number)
                self.query_set["priceTo"] = price_to

            if param.itemParameters is not None:
                if param.itemParameters.carParameters is not None:
                    for itemParam in param.itemParameters.carParameters:
                        if itemParam.carBrand is not None:
                            car_brand = itemParam.carBrand.brand
                            self.query_set["carBrand"] = car_brand
                        if itemParam.fuelType is not None:
                            fuel_type = itemParam.fuelType
                            self.query_set["fuelType"] = fuel_type
                        if itemParam.gearbox is not None:
                            gearbox = itemParam.gearbox
                            self.query_set["gearbox"] = gearbox
                        if itemParam.carClass is not None:
                            car_class = itemParam.carClass
                            self.query_set["carClass"] = car_class

        return self.query_set


def check_query_set(query_set):
    car_brands = [
        0, "alfa_romeo", "audi", "bmw", "chevrolet", "citroen", "dacia", "fiat", "ford", "honda", "hyundai", "jaguar",
        "jeep", "kia", "lancia", "mazda", "mercedes", "nissan", "opel", "peugeot", "renault", "seat", "skoda", "suzuki",
        "volkswagen", "vw", "volvo"
    ]
    if query_set["carBrand"] not in car_brands:
        return "Uneta marka automobila nije prepoznata. Podrzane marke su: " + str(car_brands)
    day_to = query_set["dayTo"]
    month_to = query_set["monthTo"]
    year_to = query_set["yearTo"]
    day_from = query_set["dayFrom"]
    month_from = query_set["monthFrom"]
    year_from = query_set["yearFrom"]
    if year_from > year_to:
        return "Datum vracanja(godina) automobila mora biti veci od datuma iznajmljivanja."
    elif (month_from > month_to) & (year_from == year_to):
        return "Datum vracanja(mesec) automobila mora biti veci od datuma iznajmljivanja."
    elif (day_from >= day_to) & (month_from >= month_to) & (year_from == year_to):
        return "Datum vracanja(dan) automobila mora biti veci od datuma iznajmljivanja."
    if ("priceFrom" in query_set) & ("priceTo" in query_set):
        if query_set["priceTo"] != 0:
            if query_set["priceFrom"] > query_set["priceTo"]:
                return "Minimalna cena ne moze biti veca od maksimalne."
    # check for invalid return date (example: return date could be 32.1.2017)
    if ((month_to == 1) | (month_to == 3) | (month_to == 5) | (month_to == 7) | (month_to == 8) | (month_to == 10)) \
            and day_to == 32:
        query_set["dayTo"] = 1
        query_set["monthTo"] = month_to + 1
    if ((month_to == 4) | (month_to == 6) | (month_to == 9) | (month_to == 11)) and day_to == 31:
        query_set["dayTo"] = 1
        query_set["monthTo"] = month_to + 1
    # check if year is leap
    if (month_to == 2) and day_to == 29:
        query_set["dayTo"] = 1
        query_set["monthTo"] = month_to + 1
    if (month_to == 12) and (day_to == 32):
        query_set["dayTo"] = 1
        query_set["monthTo"] = 1
        query_set["yearTo"] = year_to + 1

    return query_set


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
    query_set = {}
    if model.serviceType == "iznajmljivanje":
        if model.serviceItem.car is not None:
            query_set = query.interpreter_for_rent_a_car(model)
            # if query_set has some invalid parameters, ValueError will be raise in check_query_set method
            if isinstance(query_set, dict):
                query_set = check_query_set(query_set)
                # return query_set with valid parameters
        elif model.serviceItem.realEstate is not None:
            # to be implemented
            pass
    elif model.serviceType == "kupovina":
        if model.serviceItem.car is not None:
            # to be implemented
            pass
        elif model.serviceItem.realEstate is not None:
            # to be implemented
            pass

    return query_set

