import matplotlib.pyplot as chart
import numpy as np


# np.set_printoptions(precision=15)


class MoogAnalytics:
    def __init__(self, command_file_path, real_file_path):
        self.rawData = self.GetRawData(command_file_path, real_file_path)
        self.commandForward, self.commandSide, self.realForward, self.realSide = self.GetParsedData(self.rawData)

    def GetRawData(self, command_file_path, real_file_path):
        with open(command_file_path) as command_file, open(real_file_path) as real_file:
            # ignore first line (columns names)
            command_data = command_file.readlines()[1::]
            real_data = real_file.readlines()[1::]

            min_len = min(len(command_data), len(real_data))

            OUTPUT_DATA_raw = [[0] * min_len for _ in range(4)]

            for index in range(min_len):
                if not command_data[index] or not real_data[index]:
                    print("empty string, warning")
                    continue

                pre_command_line = command_data[index].split('\t')
                pre_real_line = real_data[index].split('\t')

                # '%.15f'% gets 15 digits after point; 3 == forward, 4 == side
                OUTPUT_DATA_raw[0][index] = '%.15f' % float(pre_command_line[3])
                OUTPUT_DATA_raw[1][index] = '%.15f' % float(pre_command_line[4])
                OUTPUT_DATA_raw[2][index] = '%.15f' % float(pre_real_line[3])
                OUTPUT_DATA_raw[3][index] = '%.15f' % float(pre_real_line[4])

            return OUTPUT_DATA_raw

    def GetParsedData(self, data):
        return [
            np.array(data[0], dtype=float),  # commandForward
            np.array(data[1], dtype=float),  # commandSide
            np.array(data[2], dtype=float),  # realForward
            np.array(data[3], dtype=float)  # realSide
        ]


# format: [list of COMMAND_FORWARD, list of COMMAND_SIDE, list of REAL_FORWARD, list of REAL_SIDE]
MOOG_DATA = MoogAnalytics("Command DOF.txt", "Feedback DOF.txt")

# rendering
chart.figure()

chart.subplot(1, 2, 1)
chart.title('Command vs Real -- (surge & lateral)')
chart.xlabel('Time')
chart.ylabel('Surge (forward)')
chart.plot(MOOG_DATA.commandForward[1000:2500], ':', label='command surge')
chart.plot(MOOG_DATA.realForward[1000:2500], ':', label='feedback surge')
chart.plot(MOOG_DATA.commandSide[1000:2500], 'b:', label='command lateral')
chart.plot(MOOG_DATA.realSide[1000:2500], 'r:', label='feedback lateral')
chart.legend()
chart.yticks(np.arange(min(MOOG_DATA.commandForward[1000:2500]), max(MOOG_DATA.commandForward[1000:2500]+0.01), 0.01))

chart.subplot(1, 2, 2)
chart.title('Command vs Real -- (surge / lateral)')
chart.xlabel('Lateral (side)')
chart.ylabel('Surge (forward)')
chart.plot(MOOG_DATA.commandSide[1000:2500], MOOG_DATA.commandForward[1000:2500], 'g-', label='command', linewidth=1)
chart.plot(MOOG_DATA.realSide[1000:2500], MOOG_DATA.realForward[1000:2500], 'm-', label='feedback', linewidth=1)
chart.legend()
chart.yticks(np.arange(min(MOOG_DATA.commandForward[1000:2500]), max(MOOG_DATA.commandForward[1000:2500]+0.01), 0.01))

chart.show()

# TODO
# max diff command/real
# min value, max value
# divide to trials
# lens of trials


# with open("temp_output", "w") as output_file:
#    data = MOOG_DATA[0][1000:2000]
#    for point in data:
#        output_file.write('%.15f' % float(point) + '\n')
