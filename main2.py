import matplotlib.pyplot as chart
import numpy as np
import re


np.set_printoptions(precision=15)


class MoogAnalytics:
    def __init__(self, file_path):
        self.rawData = self.GetRawData(file_path)
        self.first_parameter, self.second_parameter = self.GetParsedData(self.rawData)

    def GetRawData(self, file_path):
        with open(file_path) as file:
            data = file.readlines()[0].split(';')[:-1]

            data_len = len(data)

            OUTPUT_DATA = [[], []]

            for index in range(data_len):
                print(data[index])

                first_parameter, second_parameter = data[index].split(',')
                #print(second_parameter)

                #if (int(second_parameter) == 6):
                OUTPUT_DATA[0].append(first_parameter)
                OUTPUT_DATA[1].append(second_parameter)

            return OUTPUT_DATA

                #elapsed_time_ms = float(elapsed_time_str.split(':')[1].strip())
                #result_sleep_ms = float(result_sleep_str.split(':')[1].strip())

                #elapsed_time_ms = float(re.search(r'\d+', elapsed_time_str.split(':')[1].strip()).group())
                #result_sleep_ms = float(re.search(r'\d+', result_sleep_str.split(':')[1].strip()).group())

                #print(data[index])
                #if(data[index]== "10000000"): continue      #kostil
                #first_parameter, second_parameter = data[index].split(',')

                #elapsed_time_ms = self.extract_float(elapsed_time_str.split(':')[1].strip())
                #result_sleep_ms = self.extract_float(result_sleep_str.split(':')[1].strip())



                #print("elapsed_time_str: ", elapsed_time_str)
                #print("result_sleep_str: ", result_sleep_str)

                #OUTPUT_DATA[0] = first_parameter
                #OUTPUT_DATA[1] = second_parameter
                #print(result_sleep_str.split(':')[0].strip())

            #return OUTPUT_DATA

    def GetParsedData(self, data):
        return [
            np.array(data[0], dtype=float),  # elapsed time
            np.array(data[1], dtype=float),  # result sleep
        ]

    def extract_float(self, str):
        #print("IDs: ", str)
        match = re.search(r'(\d+\.\d+|\d+)', str)
        return float(match.group()) if match else None


# format: [list of COMMAND_FORWARD, list of COMMAND_SIDE, list of REAL_FORWARD, list of REAL_SIDE]
MOOG_DATA = MoogAnalytics("C:\\Users\\user\\Desktop\\temp_debug.txt")
#print(MOOG_DATA.elapsed_time)

# rendering
chart.figure()

#chart.subplot(1, 2, 1)
#chart.title('Send packet to MBC (3 trials)')
#chart.xlabel('sent times')
#chart.ylabel('time ms')
chart.scatter(MOOG_DATA.first_parameter, MOOG_DATA.second_parameter, s=1, label='')
#chart.scatter(range(len(MOOG_DATA.result_sleep)), MOOG_DATA.result_sleep, s=1, label='time get as input to func')
#chart.legend()
#chart.yticks(MOOG_DATA.first_parameter, MOOG_DATA.second_parameter, 0.01))

#print("Time: ", MOOG_DATA.first_parameter)
#print("Mode: ", MOOG_DATA.second_parameter)
#print((-MOOG_DATA.elapsed_time[-60] + MOOG_DATA.elapsed_time[-1])/MOOG_DATA.result_sleep[-60])

chart.show()

# TODO
# max diff command/real
# min value, max value
# divide to trials
# lens of trials

#print("MOOG_DATA.first len: ", len(MOOG_DATA.elapsed_time))
#print("MOOG_DATA.second len: ", len(MOOG_DATA.result_sleep))


# with open("temp_output", "w") as output_file:
#    data = MOOG_DATA[0][1000:2000]
#    for point in data:
#        output_file.write('%.15f' % float(point) + '\n')
