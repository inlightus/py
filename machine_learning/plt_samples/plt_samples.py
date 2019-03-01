from matplotlib import pyplot as plt

# Basic line plot
days = range(7)
money_spent = [10, 12, 12, 10, 14, 22, 24]

# plt.plot(days, money_spent)
# plt.show()

time = range(5)
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

# ------------------------------ 
# plotting revenue v.s. time
# plt.plot(time, revenue)

# plotting costs v.s. time
# plt.plot(time, costs)

# plt.show()
# ------------------------------ 
# keywords: color, linestyle, marker
# color: color_name or HEX
# linestyle: '--'(dashed), ':'(dotted), ''(no line)
# marker: 'o'(a circle), 's'(a square), '*'(a star), 'd'(diamond)

# plt.plot(time, revenue, color='purple', linestyle='--')
# plt.plot(time, costs, color='#82edc9', marker='s')
# plt.show()
# ------------------------------
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
# plt.plot(x, y)
# # plt.axis([min_x, max_x, min_y, max_y])
# plt.axis([0, 12, 2900, 3100])
# plt.xlabel('label of x')
# plt.ylabel('label of y')
# plt.title('title')
# plt.show()

# ------------------------------
# plotting subplots
# plt.subplot(rows, columns index)
months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

# plt.subplot(1, 2, 1)
# plt.plot(months, temperature, color="skyblue")
# plt.subplot(1, 2, 2)
# plt.plot(temperature, flights_to_hawaii, "o")
#
# plt.show()

# ------------------------------
# plt.subplots_adjust()
# left: the left-side margin, with a default of 0.125
# rihgt: the right-side margin, with a default of 0.9
# bottom: the bottom margin, with a default of 0.1
# top: the top margin, with a default of 0.9
# wspace: the horizontal space between adjacent subplots, with a default of 0,2
# hspace: the vertical space between adjacent subplots with a default of 0.2
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

# plt.subplot(2, 1, 1)
# plt.plot(x, straight_line)
#
# plt.subplot(2, 2, 3)
# plt.plot(x, parabola)
#
# plt.subplot(2, 2, 4)
# plt.plot(x, cubic)
#
# plt.subplots_adjust(hspace= 0.3, wspace=0.5, bottom=0.2)
#
# plt.show()

# ------------------------------
# plt.legend([name1, name2, ...])
# loc: 0(best), 1(upper right), 2(upper left), 3(lower left), 4(lower right), 5(right), 6(center left), 7(center right), 8(lower center), 9(upper center), 10(center)

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

# plt.plot(months, hyrule)
# plt.plot(months, kakariko)
# plt.plot(months, gerudo)
#
# legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']
# plt.legend(legend_labels, loc=8)
#
# plt.show()

# ------------------------------
# Setting ticks
plt.close('all')

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]


plt.figure(figsize=(4, 10)) # plt.figure() has to come at first before any plotting has done


plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.50, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

# ------------------------------
# Saving figures
# we can save figures as png, svg, pdf etc.
plt.savefig('sample.png')

plt.show() # plt.show() has to come after plt.savefig()



