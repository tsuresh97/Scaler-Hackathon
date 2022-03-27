import pandas as pd
import random
# To generate mock input CSV
inputDF = pd.DataFrame()   # Loading csv as pandas newRow frame
rowsToGenerate = int(input("How many row(s) you want to generate?: "))  # Row(s) to generate

course_list = ["M.S.(Electronic)", "M.S.(Cryptography)", "M.S.(Mechanic)", "M.S.(Data structure)",
               "M.S.(Artificial Intelligence)", "M.S.(Electrical)", "M.S.(Aeronautic)", "M.S.(Bio)"]

college_name = ["Stanford University", "Harvard University", "Columbia University", "Yale University",
                "Massachusetts Institute of Technology", "Princeton University", "The University of Chicago",
                "University of Michigan", "University of Arkansas", "Duke University", "University of Florida",
                "California Institute of Technology", "University of Wisconsin-Madison", "University of Delaware",
                "Stevens Institute of Technology", "The University of Arizona", "Brown University"]


for rowID in range(1, rowsToGenerate+1):
    print("Coming into ==> "+str(rowID))
    newRow = {
                "Serial No.": str(rowID),
                "GRE Score": random.randrange(261, 340),
                "TOEFL Score": random.randrange(98, 120),
                "SOP": float(random.randrange(1, 6)),
                "LOR": float(random.randrange(1, 6)),
                "CGPA": float(random.randrange(7, 11)),
                "Research": random.randrange(0, 2),
                "Gender": random.randrange(0, 2),
                "Age": random.randrange(18, 28),
                "Course": random.randrange(0, 8),
                "College Name": college_name[random.randrange(0, 17)]
            }

    inputDF = pd.concat([inputDF, pd.DataFrame.from_records([newRow])])

inputDF.to_csv('admission_prediction.csv', index = None, header=True)