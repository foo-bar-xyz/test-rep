import csv
C = []
#D = {}
with open('data.csv', newline='') as csv_f:
    reader = csv.reader(csv_f, dialect='excel', delimiter=';')
    for r in reader:
        C.append(r)
#for h in C[0]:
#    D[h] = []

#for h in range(len(C[0])):
#    for i in range(1,len(C)):
#        D[C[0][h]].append(C[i][h])


class Person(object):
    def __init__(self, age, gender, loan):
        self.age = int(age)
        self.gender = gender
        self.loan = round(float(loan), 2)

    def __str__(self):
        return '<' + self.gender + ', ' + str(self.age) + ', ' + str(self.loan) + '>'

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_loan(self):
        return self.loan

persons = []
for c in range(1, len(C)):
    if not (C[c][0] == '' or C[c][1] == '' or float(C[c][2]) == 0.0):
        persons.append(Person(C[c][0], C[c][1], C[c][2]))

#for p in persons:
#    print(p)
