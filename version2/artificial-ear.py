# Krumhansl-Schmuckler key-finding algorithm
# Python3

from datetime import datetime

# Tone list
tone_list = ("c_major", "c_minor", "c#_major", "c#_minor", "d_major",\
            "d_minor", "d#_major", "d#_minor", "e_major", "e_minor",\
            "f_major", "f_minor", "f#_major", "f#_minor", "g_major",\
            "g_minor", "g#_major", "g#_minor", "a_major", "a_minor",\
            "a#_major", "a#_minor", "b_major", "b_minor")
print("Input order: c, c#, d, d#, e, f, f#, g, g#, a, a#, b")

# Algorithm weights
major_profile = (6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66,\
                 2.29, 2.88)
minor_profile = (6.33, 2.68, 3.52, 5.38, 2.6, 3.53, 2.54, 4.75, 3.98, 2.69,\
                3.34, 3.17)
major_mean = 3.4825
minor_mean = 3.7092

# Handle input
durations = input("12 durations: ").split(",")
a = datetime.now()
for i in range(len(durations)):
    durations[i] = int(float(durations[i]))

# Mean of input
durations_mean = 0
for i in range(12):
    durations_mean += durations[i]
durations_mean /= 12

# Solve for all R
R_values = []
for i in range(12):
    dividend = [0, 0]
    divisor0 = [0, 0]
    divisor1 = [0, 0]
    tot_divisor = [0, 0]
    for j in range(12):
        pointer = (j+i)%12
        dividend[0] += ((major_profile[j] - major_mean) * 
                        (durations[pointer] - durations_mean))
        dividend[1] += ((minor_profile[j] - minor_mean) * 
                        (durations[pointer] - durations_mean))
        divisor0[0] += (major_profile[j] - major_mean)**2
        divisor0[1] += (minor_profile[j] - minor_mean)**2
        divisor1[0] += (durations[pointer] - durations_mean)**2
        divisor1[1] += (durations[pointer] - durations_mean)**2
    tot_divisor[0] = (divisor0[0] * divisor1[0])**(1/2)
    tot_divisor[1] = (divisor0[1] * divisor1[1])**(1/2)
    R_values.append(dividend[0] / tot_divisor[0])
    R_values.append(dividend[1] / tot_divisor[1])

max_value = max(R_values)
index = R_values.index(max_value)
tone = tone_list[index]
b = datetime.now() - a
print(tone)
print(b)
