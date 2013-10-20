import csv
someiterable = [1,2,3,4]
with open('some.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows('ABCD')
