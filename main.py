import matplotlib.pyplot as chart
import numpy as np


def GetRawData (command_file_path, real_file_path):
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


# format: [list of COMMAND_FORWARD, list of COMMAND_SIDE, list of REAL_FORWARD, list of REAL_SIDE]
MOOG_DATA_raw = GetRawData("Command DOF.txt", "Feedback DOF.txt")

COMMAND_FORWARD = np.array(MOOG_DATA_raw[0], dtype=float)
COMMAND_SIDE    = np.array(MOOG_DATA_raw[1], dtype=float)
REAL_FORWARD    = np.array(MOOG_DATA_raw[2], dtype=float)
REAL_SIDE       = np.array(MOOG_DATA_raw[3], dtype=float)

# rendering
chart.plot(COMMAND_FORWARD[1000:2500])
chart.plot(REAL_FORWARD[1000:2500])
chart.show()

#TODO
#max diff command/real
#min value, max value
# divide to trials
#lens of trials


#with open("temp_output", "w") as output_file:
#    data = MOOG_DATA[0][1000:2000]
#    for point in data:
#        output_file.write('%.15f' % float(point) + '\n')
