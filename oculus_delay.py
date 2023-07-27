import matplotlib.pyplot as chart
import numpy as np
import re       #regular expression


class MoogAnalytics:
    def __init__(self, file_path):
        self.raw_data = self.GetRawData(file_path)
        self.time_stamp, self.free_data_param = self.GetDataParsedToFloat(self.raw_data)
        self.cpu_freq = 10_000_000

    def GetRawData (self, file_path):
        with open(file_path) as file:
            data = file.readlines()[0].split(';')[:-1]

            data_len = len(data)

            OUTPUT_DATA = [[], []]

            for index in range(data_len):
                #print(data[index])

                first_parameter, second_parameter = data[index].split(',')

                OUTPUT_DATA[0].append(first_parameter)
                OUTPUT_DATA[1].append(second_parameter)

            return OUTPUT_DATA

    def GetDataParsedToFloat (self, data):
        return [
            np.array(data[0], dtype=float),
            np.array(data[1], dtype=float),
        ]

    def ExtractFloat (self, str_input):
        match = re.search(r'(\d+\.\d+|\d+)', str_input)
        return float(match.group()) if match else None

    def GetFramesDelays (self):
        trials = [[]]
        trials_index = 0

        for i in range(1, len(self.free_data_param)):
            delay = (self.time_stamp[i] - self.time_stamp[i-1]) / self.cpu_freq * 1000  # *1000 to get ms
            #print(delay)
            if delay > 100:
                #print(len(trials[trials_index]))
                trials_index += 1
                trials.append([])
                continue
            trials[trials_index].append(delay)

        return trials[len(trials)-3:]

    def DrawChartAsAxes (self, data, number_of_charts, index_in_figure, chart_name = "", y_axis_name = ""):
        chart.subplot(1, number_of_charts, index_in_figure)
        chart.title(chart_name)
        chart.xlabel('frame number')
        chart.ylabel(y_axis_name)

        x_axis = range(1, len(data)+1)
        y_axis = data

        chart.scatter(x_axis, y_axis, s=1)

    def DrawCharts (self):
        chart.figure()

        list_of_trials = self.GetFramesDelays()

        for sub_chart in list_of_trials:
            self.DrawChartAsAxes(
                sub_chart,
                len(list_of_trials),
                list_of_trials.index(sub_chart)+1,
                '',
                'delay between frames (ms)')

        chart.show()



Moog_Analytics = MoogAnalytics("C:\\Users\\user\\Desktop\\temp_debug.txt")
Moog_Analytics.DrawCharts()
