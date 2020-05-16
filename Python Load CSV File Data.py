



# PYTHON LOAD CSV FILE DATA

# Pull in data from .csv files to be analyzed or to create charts and graphs, etc.

# Mac - create CSV file in Numbers (File > Export To > CSV)
# Mac - create Plain Text (txt) file in Pages (File > Export To > Plain Text)
# Windows - use Excel for csv and Word or Notepad for txt
# Can also use LibreOffice Calc, Atom Text Editor, etc.
# Important - put files in your working directory or path that your editor/IDE uses (must be correct path), or type in the path in open(), loadtxt(), read_csv(), etc.

import csv
import matplotlib.pyplot as plt
import numpy
import pandas

# IMPORT CSV DATA & DISPLAY DATA
# start with csvdata.csv
with open('csvdata.csv') as csvfile:
    # replace with .txt file and it should work (csvplaintext.txt)
    for i in csv.reader(csvfile):
        print(', '.join(i))
    print('')

# IMPORT CSV DATA & PLOT/CHART DATA
x, y = [], []
labels = ['region 1', 'region 2', 'region 3', 'region 4', 'region 5']
with open('csvdata.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for i in data:
        print(i)
        # if you don't cast (loop i) as int some options won't work (i.e.-assign labels to x-axis)
        x.append(int(i[0]))
        y.append(int(i[1]))
print('x {}, y {}'.format(x, y))
plt.plot(x, y)
plt.title('Graph 1')
plt.xticks(x, labels, rotation='vertical')
plt.show()

# IMPORT CSV DATA USING NUMPY
# use skiprows arg if needed
x, y = numpy.loadtxt('csvdatanumpy.csv', delimiter=',', unpack=True)
# unpack=True so x,y values can be properly assigned, etc.
print('x',list(x)); print('y',list(y))
plt.plot(x, y, 'bx', label='csv file data using numpy')
# use 'rx' for red x's on chart
plt.xlabel('x-axis values')
plt.ylabel('y-axis values')
plt.title('Graph 2')
plt.legend()
plt.show()

# IMPORT CSV DATA USING PANDAS
# make sure csv includes column labels
df = pandas.read_csv('csvdata2.csv')
print(df)
df.plot(x='A',y='B')
