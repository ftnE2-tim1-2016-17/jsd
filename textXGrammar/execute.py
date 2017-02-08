from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot
import os
import datetime


class Query(object):

    def interpreter(self, model):

        self.city = model.city

        self.dayFrom = model.dateFrom.day.number
        self.monthFrom = model.dateFrom.month.number
        self.yearFrom = model.dateFrom.year.number
        self.hourFrom = model.timeFrom.hour.number
        self.minuteFrom = model.timeFrom.minute.number

        self.dayTo = model.dateTo.day.number
        self.monthTo = model.dateTo.month.number
        self.yearTo = model.dateTo.year.number
        self.hourTo = model.timeTo.hour.number
        self.minuteTo = model.timeTo.minute.number

        return self



def execute(path, grammar_file_name, example_file_name, export_dot, export_png):

    meta_path = os.path.join(path, grammar_file_name)
    meta_name = os.path.splitext(meta_path)[0]
    metamodel = metamodel_from_file(meta_path)

    if export_dot:
        metamodel_export(metamodel, meta_name + '.dot')
        if export_png:
            graph = pydot.graph_from_dot_file(meta_name + '.dot')
            graph[0].write_png(meta_name + '.png')

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

    return query_set


