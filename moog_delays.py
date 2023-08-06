import matplotlib.pyplot as chart
import numpy as np
import re


class MoogAnalytics:
    def __init__(self, file_path):
        self.raw_data = self.GetRawData(file_path)

    def GetRawData (self, file_path):
        OUTPUT_DATA = []

        with open(file_path) as file:
            for line in file:
                OUTPUT_DATA.append(float(line))

        return OUTPUT_DATA

    def GetDiffs (self):
        OUTPUT_DATA = []

        for delay in range(1, len(self.raw_data)):
            OUTPUT_DATA.append(float(self.raw_data[delay] - self.raw_data[delay-1]))

        return OUTPUT_DATA


    def DrawPointChart (self):
        chart.figure('')
        chart.subplot(1, 1, 1)
        chart.title('Moog full movement')
        chart.xlabel('"time"')
        chart.ylabel('diff between "frames"')

        data = self.GetDiffs()[8000:12000]
        #data = self.raw_data[8000:12000]

        #chart.scatter(range(len(data)), data, s=1)
        chart.plot(data)

        chart.show()





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

            if delay > 100:
                trials_index += 1
                trials.append([])
                continue

            trials[trials_index].append(delay)

        if self.chart_to_show == 'all':
            return trials
        else:
            return trials[len(trials)-self.chart_to_show:]  # X last trials

    def GetTrialsTotalTimes (self):
        trials = self.GetFramesDelays()
        delays = []

        for trial in trials:
            if trial == []: continue        # ещё один костыль. да простит меня бог кодинга

            total_time = round(sum(trial), 2)

            if total_time < 50: continue
            #if total_time > 100: continue

            delays.append(total_time)
            print(total_time)

        return delays

    def MakeChartAsAxes (self, data, number_of_charts = 1, index_in_figure = 1, chart_name = "", y_axis_name = ""):
        chart.subplot(1, number_of_charts, index_in_figure)
        chart.title('Total time: ' + str(round(sum(data), 2)) + 'ms')
        chart.xlabel('frames')
        chart.ylabel(y_axis_name)

        x_axis = range(1, len(data)+1)
        y_axis = data

        chart.scatter(x_axis, y_axis, s=1)

    def DrawChartAsAxes (self):
        chart.figure('')
        self.MakeChartAsAxes(data = self.GetTrialsTotalTimes())
        chart.title('Test')
        chart.xlabel('number of trials')
        chart.ylabel('trial total time')
        chart.show()


    def DrawCharts (self):
        list_of_trials = self.GetFramesDelays()

        chart.figure('Charts of ' + str(len(list_of_trials)) + ' last trials')

        for sub_chart in list_of_trials:
            self.MakeChartAsAxes(
                sub_chart,
                len(list_of_trials),
                list_of_trials.index(sub_chart)+1,
                '',
                'delay between frames (ms)')

        chart.show()



Moog_Analytics = MoogAnalytics("C:\\Users\\user\\Desktop\\Data\\temp_python.txt")
print(Moog_Analytics.DrawPointChart())
