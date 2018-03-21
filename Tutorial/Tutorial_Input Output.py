__author__ = 'ryan'


"""______________________________________________________________
                         csv
"""
import csv

"""##### write ######"""


csvfile = open('csvwritefile.csv', 'wb')
spamwriter = csv.writer(csvfile)
                         # delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

dataset = ['Spam'] * 5 + ['Baked Beans']   # dataset is a list
spamwriter.writerow(dataset)

dataset1 = ['Spam', 'Lovely Spam', 'Wonderful Spam']
spamwriter.writerow(dataset1)

csvfile.close()
