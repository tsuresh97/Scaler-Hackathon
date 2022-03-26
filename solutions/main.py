import os
import pandas as pd
import requests
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from tkinter.messagebox import showinfo
from tkinter import *
import smtplib
import tkinter.ttk as ttk
from tkinter import font


class SVMModel:
    def __init__(self):
        self.X = None
        self.Y = None
        self.standardScaler = None
        self.remove_college = []

    def importData(self, val=[]):
        dataset = pd.read_csv('admission_prediction.csv')
        if len(val) != 0:
            for i in val:
                dataset.drop(dataset.index[dataset['College Name'] == i], inplace=True)
        self.X = dataset.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9]].values
        self.Y = dataset.iloc[:, 10].values

    def doFatureScaling(self):
        self.standardScaler = StandardScaler()
        self.X = self.standardScaler.fit_transform(self.X)

    def predictMark(self, data, MAIL_ID):
        self.importData()
        self.doFatureScaling()

        classifier = SVC(kernel='rbf', random_state=0)

        classifier.fit(self.X, self.Y)

        testData = self.standardScaler.transform([data])
        result = []
        for i in range(0, 3):
            prediction = classifier.predict(testData)
            self.remove_college.append(prediction[0])
            result.append(prediction[0])
            self.importData(self.remove_college)
            self.doFatureScaling()
            classifier = SVC(kernel='rbf', random_state=0)
            classifier.fit(self.X, self.Y)
            testData = self.standardScaler.transform([data])
        self.remove_college = []

        showinfo("Report", "Our system suggest you to join \n 1. {} \n 2. {} \n 3. {}".format(result[0],
                                                                                              result[1],
                                                                                              result[2]),
                 )
        if MAIL_ID != '':
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("cserockers01@gmail.com", "$uResh@007")
                SUBJECT = "College Admission Prediction"
                TEXT = "Our system suggest you to join \n 1. {} \n 2. {} \n 3. {}".format(result[0],
                                                                                          result[1], result[2])
                message = 'Subject: {0}\n\n{1}'.format(SUBJECT, TEXT)
                s.sendmail("cserockers01@gmail.com", [MAIL_ID], message)
                s.quit()
                print("Mail sent...!")

            except:
                print("Invalid mail ID")


"""
UI PART
"""


class UI:
    def __init__(self):
        self.top = Tk()
        self.top.geometry("500x600")
        try:
            self.top.iconbitmap('../Images/Scaler_Academy_logo.ico')
        except:
            self.top.iconbitmap('Scaler_Academy_logo.ico')

        self.top.title("College Admission Prediction")
        self.top.configure(bg="#7979F5")  # 856ff8

        self.gender_user_input = StringVar(self.top, "0")
        self.research_user_input = StringVar(self.top, "1")
        self.gre_user_choice = StringVar(self.top)
        self.toefl_user_choice = StringVar(self.top)
        self.sop_user_choice = StringVar(self.top)
        self.lor_user_choice = StringVar(self.top)
        self.cgpa_user_choice = StringVar(self.top)
        self.age_user_choice = StringVar(self.top)
        self.course_user_choice = StringVar(self.top, "         Select         ")
        self.email_user_choice = StringVar(self.top)

        course_list = ["M.S.(Electronic)", "M.S.(Cryptography)", "M.S.(Mechanic)", "M.S.(Data structure)",
                       "M.S.(Artificial Intelligence)", "M.S.(Electrical)", "M.S.(Aeronautic)", "M.S.(Bio)"]
        self.course_list = StringVar(self.top)
        self.course_list.set(course_list[0])

        self.form_label = Label(self.top, text="Please fill the form", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 14, 'bold')).place(x=210, y=10)
        self.gre_label = Label(self.top, text="GRE Score", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=50)
        self.toefl_label = Label(self.top, text="TOEFL Score", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=90)
        self.sop_label = Label(self.top, text="SOP", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=130)
        self.lor_label = Label(self.top, text="LOR", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=170)
        self.cgpa_label = Label(self.top, text="CGPA", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=210)
        self.research_label = Label(self.top, text="Research", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=250)
        self.gender_label = Label(self.top, text="Gender", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=290)
        self.age_label = Label(self.top, text="Age", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=340)
        self.course_label = Label(self.top, text="Course", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=390)
        self.email_label = Label(self.top, text="Email", fg='#ffffff', bg="#7979F5", font=("Century Gothic", 12, 'bold')).place(x=30, y=430)

        self.gre_input = Entry(self.top, textvariable=self.gre_user_choice, width = 20, fg='#ffffff', bg="#7979F5",
                               font=("Century Gothic", 12, 'bold')).place(x=280, y=50)
        self.toefl_input = Entry(self.top, textvariable=self.toefl_user_choice, width = 20, fg='#ffffff', bg="#7979F5",
                               font=("Century Gothic", 12, 'bold')).place(x=280, y=90)
        self.sop_input = Entry(self.top, textvariable=self.sop_user_choice, width = 20, fg='#ffffff', bg="#7979F5",
                               font=("Century Gothic", 12, 'bold')).place(x=280, y=130)
        self.lor_input = Entry(self.top, textvariable=self.lor_user_choice, width = 20, fg='#ffffff', bg="#7979F5",
                               font=("Century Gothic", 12, 'bold')).place(x=280, y=170)
        self.cgpa_input = Entry(self.top, textvariable=self.cgpa_user_choice, width = 20, fg='#ffffff', bg="#7979F5",
                               font=("Century Gothic", 12, 'bold')).place(x=280, y=210)
        s = ttk.Style()  # Creating style element
        s.configure('Wild.TRadiobutton',  # First argument is the name of style. Needs to end with: .TRadiobutton
                    background='#ffffff',  # Setting background to our specified color above
                    foreground='#7979F5')  # You can define colors like this also

        self.research_input = Radiobutton(self.top, text="Yes", variable=self.research_user_input, bg="#7979F5",
                    value=0, font=("Century Gothic", 12, 'bold'))
        self.research_input.place(x=290, y=250)
        self.research_input = Radiobutton(self.top, text="No", variable=self.research_user_input, bg="#7979F5",
                    value=1, font=("Century Gothic", 12, 'bold'))
        self.research_input.place(x=370, y=250)

        self.gender_input = Radiobutton(self.top, text="Male", variable=self.gender_user_input, bg="#7979F5",
                    value=0, font=("Century Gothic", 12, 'bold'))
        self.gender_input.place(x=290, y=290)
        self.gender_input = Radiobutton(self.top, text="Female", variable=self.gender_user_input, bg="#7979F5",
                    value=1, font=("Century Gothic", 12, 'bold'))
        self.gender_input.place(x=370, y=290)

        self.age_input = Entry(self.top, textvariable=self.age_user_choice, width = 20, fg='#ffffff', bg="#7979F5",
                               font=("Century Gothic", 12, 'bold')).place(x=280, y=340)
        self.course_input = OptionMenu(self.top, self.course_user_choice, *course_list)
        self.course_input.config(font=("Century Gothic", 10, 'bold'), fg='#ffffff', bg="#7979F5")  # set the button font

        self.course_input.place(x=280, y=380)
        self.email_input = Entry(self.top, textvariable=self.email_user_choice, width = 20, fg='#ffffff', bg="#7979F5",
                               font=("Century Gothic", 12, 'bold')).place(x=280, y=430)

        self.show_result = Button(self.top, text="Show Result", font=("Century Gothic", 12, 'bold'),
                                  fg='#ffffff', bg="#22FF00",
                                  width=30, command=self.callback)
        self.show_result.place(x=140, y=520)
        self.center(self.top)
        self.top.mainloop()

    def center(self, win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def download_file(self, url, filename):
        ''' Downloads file from the url and save it as filename '''
        # check if file already exists
        if not os.path.isfile(filename):
            print('Downloading File')
            response = requests.get(url)
            # Check if the response is ok (200)
            if response.status_code == 200:
                # Open file and write the content
                with open(filename, 'wb') as file:
                    # A chunk of 128 bytes
                    for chunk in response:
                        file.write(chunk)
        else:
            print('File exists')

    def callback(self):
        gender_user_input = self.gender_user_input.get()
        research_user_input = self.gender_user_input.get()
        gre_user_choice = self.gre_user_choice.get()
        toefl_user_choice = self.toefl_user_choice.get()
        sop_user_choice = self.sop_user_choice.get()
        lor_user_choice = self.lor_user_choice.get()
        cgpa_user_choice = self.cgpa_user_choice.get()
        age_user_choice = self.age_user_choice.get()
        email_user_choice = self.email_user_choice.get()

        course_user_choice = self.course_user_choice.get()
        course_list = {
            "M.S.(Electronic)": 0, "M.S.(Cryptography)": 1, "M.S.(Mechanic)" :2,
            "M.S.(Data structure)": 3,
            "M.S.(Artificial Intelligence)": 4,  "M.S.(Electrical)": 5, "M.S.(Aeronautic)": 6,
            "M.S.(Bio)": 7
        }
        course_user_choice = course_list[course_user_choice]
        SVMObject = SVMModel()
        SVMObject.predictMark(
            [float(gre_user_choice), float(toefl_user_choice), float(sop_user_choice),
             float(lor_user_choice), float(cgpa_user_choice), float(research_user_input),
             float(gender_user_input), float(age_user_choice), str(course_user_choice)],
            email_user_choice)  # 'devendra.pmu@gmail.com'
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://clean-composite-251123.firebaseio.com/', None)
        data = {'GRE': gre_user_choice,
                'TOEFL': toefl_user_choice,
                'SOP': sop_user_choice,
                'LOR': lor_user_choice,
                'CGPA': cgpa_user_choice,
                'Research': research_user_input,
                'Gender': gender_user_input,
                'Age': course_user_choice,
                'Email': email_user_choice
                }
        result = firebase.post('/clean-composite-251123', data)
        print(result)


class Splash:
    def __init__(self):
        os.system("gdown --id 13XNeFRUD-EkdvxA_lQKx2KoByrHdLeXA")
        self.top = Tk()
        self.top.geometry("600x200")
        self.top.configure(bg="#7979F5")  # 856ff8

        try:
            self.top.iconbitmap('../Images/Scaler_Academy_logo.ico')
        except:
            self.top.iconbitmap('Scaler_Academy_logo.ico')

        self.top.title("College Admission Prediction")
        self.center(self.top)
        self.form_label = Label(self.top, text="Fetching prediction data from server....", fg='#ffffff',
                                bg="#7979F5", font=("Century Gothic", 20, 'bold')).place(x=70, y=80)

        self.top.after(4000, self.hai)
        self.top.mainloop()

    def center(self, win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def hai(self):
        self.top.destroy()
        UI()

Splash()