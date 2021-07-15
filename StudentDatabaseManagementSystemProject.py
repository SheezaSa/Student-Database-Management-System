
#=============================================Student Record System===========================================
from tkinter import*
import tkcalendar #from tkcalender import*
import calendar
import pymysql
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr

class studentRecords:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Student Record System")
        self.root.geometry("1350x800+0+0")#0 0 are coordinates

        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)
        self.TabControl2 = ttk.Frame(notebook)
        notebook.add(self.TabControl1, text='School System')
        notebook.add(self.TabControl2, text='Student Details')
        
        notebook.grid()
        
        #========================================VARIABLES=================================================
        #student detail
        self.StudentID = StringVar()
        self.EnrollmentNo = StringVar()
        self.Status = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.Address = StringVar()
        self.PostCode = StringVar()
        self.Gender = StringVar()
        self.DOB = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()
        #for guidance
        self.ParentGuidance = StringVar()
        self.pgFirstName = StringVar()
        self.pgSurname = StringVar()
        self.pgAddress = StringVar()
        self.pgWorkPhone = StringVar()
        self.pgMobile = StringVar()
        self.pgEmail = StringVar()
        #about course
        self.Course = StringVar()
        self.CourseCode = StringVar()
        self.Faculty = StringVar()
        self.Dean = StringVar()
        self.Head_of_School = StringVar()
        self.ProgramLeader = StringVar()
        self.CourseTutor1 = StringVar()
        self.CourseTutor2 = StringVar()
        self.Building = StringVar()
        self.CourseFee = StringVar()
        #fees
        self.HomeStudent = StringVar()
        self.Oversea = StringVar()
        self.Accommodation = StringVar()
        self.ExchangeProg = StringVar()
        self.Scholarship = StringVar()
        #about course
        self.BA = StringVar()
        self.BSc = StringVar()
        self.MA = StringVar()
        self.MSc = StringVar()
        self.PhD = StringVar()
        #about staff
        self.DataScience = StringVar()
        self.EventDrivenPro = StringVar()
        self.ObjectOriented = StringVar()
        self.Spreadsheet = StringVar()
        self.SystemAnalysis = StringVar()
        self.InformTechnology = StringVar()
        self.DigitalGraphics = StringVar()

        self.English = StringVar()
        self.Games = StringVar()
        self.Animation = StringVar()
        self.Database1 = StringVar()
        self.Maths = StringVar()
        self.AddMaths = StringVar()
        self.Physics = StringVar()
        
        self.Media = StringVar()#Media
        self.GraphicD = StringVar()#Graphic Designing
        self.ArtiIntell = StringVar()#Artificial Intelligence
        self.Architecture = StringVar()#Computer Architecture
        self.MachLearn = StringVar()#Machine Learning
        self.SocialComput = StringVar()#Social Computing
        self.InformSecur = StringVar()#Information Security
        self.NetComm = StringVar()#Networking And Communications
        
        
        
        self.SelectedSubjects = StringVar()
        self.Module1 = StringVar()
        self.Module2 = StringVar()
        self.Module3 = StringVar()
        self.Module4 = StringVar()
        self.Module5 = StringVar()
        self.Module6 = StringVar()
        self.Module7 = StringVar()
        self.Module8 = StringVar()
        self.Module9 = StringVar()
        
        
        self.TotalScore = StringVar()
        self.Percentage = StringVar()
        self.Ranking = StringVar()
        self.ResultDate = StringVar()

        self.Subject1 = StringVar()
        self.Subject2 = StringVar()
        self.Subject3 = StringVar()
        self.Subject4 = StringVar()
        self.Subject5 = StringVar()
        self.Subject6 = StringVar()
        self.Subject7 = StringVar()
        self.Subject8 = StringVar()
        self.Subject9 = StringVar()
        
        #============================================Exit==========================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        #===========================================Reset==============================================
        def Reset():
            self.StudentID.set("")
            self.EnrollmentNo.set("")
            self.Status.set("")
            self.Firstname.set("")
            self.Surname.set("")
            self.Address.set("")
            self.PostCode.set("")
            self.Gender.set("")
            self.DOB.set("")
            self.Mobile.set("")
            self.Email.set("")
            
            self.ParentGuidance.set("")
            self.pgFirstName.set("")
            self.pgSurname.set("")
            self.pgAddress.set("")
            self.pgWorkPhone.set("")
            self.pgMobile.set("")
            self.pgEmail.set("")

            #about course
            self.Course.set("Course Selector")
            self.CourseCode.set("")
            self.Faculty.set("")
            self.Dean.set("")
            self.Head_of_School.set("")
            self.ProgramLeader.set("")
            self.CourseTutor1.set("")
            self.CourseTutor2.set("")
            self.Building .set("")
            self.CourseFee.set("")
            #fees
            self.HomeStudent.set("No")
            self.Oversea .set("No")
            self.Accommodation.set("No")
            self.ExchangeProg.set("No")
            self.Scholarship.set("No")
            #about course
            self.BA.set("0")
            self.BSc.set("0")
            self.MA.set("0")
            self.MSc.set("0")
            self.PhD.set("0")
            #about staff
            self.DataScience.set("No")
            self.EventDrivenPro.set("No")
            self.ObjectOriented.set("No")
            self.Spreadsheet.set("No")
            self.SystemAnalysis.set("No")
            self.InformTechnology.set("No")
            self.DigitalGraphics.set("No")

            self.English.set("No")
            self.Games.set("No")
            self.Animation.set("No")
            self.Database1.set("No")
            self.Maths.set("No")
            self.AddMaths.set("No")
            self.Physics.set("No")
            
            self.Media.set("No")
            self.GraphicD.set("No")
            self.ArtiIntell.set("No")
            self.Architecture.set("No")
            self.MachLearn .set("No")
            self.SocialComput .set("No")
            self.InformSecur.set("No")
            self.NetComm .set("No")


            self.Module1.set("")
            self.Module2.set("")
            self.Module3.set("")
            self.Module4.set("")
            self.Module5.set("")
            self.Module6.set("")
            self.Module7.set("")
            self.Module8.set("")
            self.Module9.set("")
            
            
            self.Ranking.set("")
            self.TotalScore.set("")
            self.Percentage.set("")
            self.ResultDate.set("")

            self.Subject1.set("")
            self.Subject2.set("")
            self.Subject3.set("")
            self.Subject4.set("")
            self.Subject5.set("")
            self.Subject6.set("")
            self.Subject7.set("")
            self.Subject8.set("")
            self.Subject9.set("")
            
            
#============================================SET SUBJECT============================================================
            
        def setSubject(event):
            if self.Subject1.get() == "Event Driven Program":
                self.EventDrivenPro.set("Core Unit")
                self.Architecture.set("No")
                self.SocialComput.set('No')
                self.txt1.configure(state = NORMAL)
                self.txt1.focus_set()
            if self.Subject1.get() == "Computer Architecture":
                self.Architecture.set("Core Unit")
                self.EventDrivenPro.set('No')
                self.SocialComput.set('No')
                self.txt1.configure(state = NORMAL)
                self.txt1.focus_set()
            if self.Subject1.get() == "Social Computing":
                self.SocialComput.set('Core Unit')
                self.Architecture.set("No")
                self.EventDrivenPro.set('No')
                self.txt1.configure(state = NORMAL)
                self.txt1.focus_set()
            elif self.Subject1.get() == "":
                self.EventDrivenPro.set("No")
                self.SocialComput.set("No")
                self.Architecture.set("No")
                self.txt1.configure(state = DISABLED)
                self.Module1.set("")



            if self.Subject2.get() == "Object Oriented":
                self.ObjectOriented.set("Core Unit")
                self.Spreadsheet.set("No")
                self.txt2.configure(state = NORMAL)
                self.txt2.focus_set()
            if self.Subject2.get() == "Spreadsheet":
                self.Spreadsheet.set("Core Unit")
                self.ObjectOriented.set("No")
                self.txt2.configure(state = NORMAL)
                self.txt2.focus_set()
            elif self.Subject2.get() == "":
                self.ObjectOriented.set("No")
                self.Spreadsheet.set("No")
                self.txt2.configure(state = DISABLED)
                self.Module2.set("")
                

            if self.Subject3.get() == "System Analysis":
                self.SystemAnalysis.set("Core Unit")
                self.InformTechnology.set("No")
                self.InformSecur.set("No")
                self.txt3.configure(state = NORMAL)
                self.txt3.focus_set()
            if self.Subject3.get() == "Information Technology":
                self.InformTechnology.set("Core Unit")
                self.SystemAnalysis.set("No")
                self.InformSecur.set("No")
                self.txt3.configure(state = NORMAL)
                self.txt3.focus_set()
            if self.Subject3.get() == "Information Security":
                self.InformSecur.set("Core Unit")
                self.InformTechnology.set("No")
                self.SystemAnalysis.set("No")
                self.txt3.configure(state = NORMAL)
                self.txt3.focus_set()
            elif self.Subject3.get() == "":
                self.InformSecur.set("No")
                self.InformTechnology.set("No")
                self.SystemAnalysis.set("No")
                self.txt3.configure(state = DISABLED)
                self.Module3.set("")



            if self.Subject4.get() == "Digital Graphics":
                self.DigitalGraphics.set("Core Unit")
                self.English.set("No")
                self.txt4.configure(state = NORMAL)
                self.txt4.focus_set()
            if self.Subject4.get() == "English":
                self.English.set("Core Unit")
                self.DigitalGraphics.set("No")
                self.txt4.configure(state = NORMAL)
                self.txt4.focus_set()
            elif self.Subject4.get() == "":
                self.English.set("No")
                self.DigitalGraphics.set("No")
                self.txt4.configure(state = DISABLED)
                self.Module4.set("")


            if self.Subject5.get() == "Games":
                self.Games.set("Core Unit")
                self.Animation.set("No")
                self.Media.set("No")
                self.GraphicD.set("No")
                self.txt5.configure(state = NORMAL)
                self.txt5.focus_set()
            if self.Subject5.get() == "Animation":
                self.Animation.set("Complete")
                self.Games.set("No")
                self.Media.set("No")
                self.GraphicD.set("No")
                self.txt5.configure(state = NORMAL)
                self.txt5.focus_set()
            if self.Subject5.get() == "Media":
                self.Media.set("Core Unit")
                self.GraphicD.set("No")
                self.Animation.set("No")
                self.Games.set("No")
                self.txt5.configure(state = NORMAL)
                self.txt5.focus_set()
            if self.Subject5.get() == "Graphic Designing":
                self.Media.set("No")
                self.GraphicD.set("Core Unit")
                self.Animation.set("No")
                self.Games.set("No")
                self.txt5.configure(state = NORMAL)
                self.txt5.focus_set()
            elif self.Subject5.get() == "":
                self.Animation.set("No")
                self.Games.set("No")
                self.Media.set("No")
                self.GraphicD.set("No")
                self.txt5.configure(state = DISABLED)
                self.Module5.set("")


            if self.Subject6.get() == "Database":
                self.Database1.set("Core Unit")
                self.Maths.set("No")
                self.txt6.configure(state = NORMAL)
                self.txt6.focus_set()
            if self.Subject6.get() == "Maths":
                self.Maths.set("Core Unit")
                self.Database1.set("No")
                self.txt6.configure(state = NORMAL)
                self.txt6.focus_set()
            elif self.Subject6.get() == "":
                self.Maths.set("No")
                self.Database1.set("No")
                self.txt6.configure(state = DISABLED)
                self.Module6.set("")


            if self.Subject7.get() == "AddMaths":
                self.AddMaths.set("Core Unit")
                self.Physics.set("No")
                self.txt7.configure(state = NORMAL)
                self.txt7.focus_set()
            if self.Subject7.get() == "Physics":
                self.Physics.set("Core Unit")
                self.AddMaths.set("No")
                self.txt7.configure(state = NORMAL)
                self.txt7.focus_set()
            elif self.Subject7.get() == "":
                self.Physics.set("No")
                self.AddMaths.set("No")
                self.txt7.configure(state = DISABLED)
                self.Module7.set("")


            if self.Subject8.get() == "DataScience":
                self.DataScience.set("Core Unit")
                self.NetComm.set("No")
                self.txt8.configure(state = NORMAL)
                self.txt8.focus_set()
            if self.Subject8.get() == "Networking and Communications":
                self.DataScience.set("No")
                self.NetComm.set("Core Unit")
                self.txt8.configure(state = NORMAL)
                self.txt8.focus_set()
            elif self.Subject8.get() == "":
                self.DataScience.set("No")
                self.NetComm.set("No")
                self.txt8.configure(state = DISABLED)
                self.Module8.set("")


            if self.Subject9.get() == "Artificial Intelligence":
                self.ArtiIntell.set("Core Unit")
                self.MachLearn.set("No")
                self.txt9.configure(state = NORMAL)
                self.txt9.focus_set()
            if self.Subject9.get() == "Machine Learning":
                self.ArtiIntell.set("No")
                self.MachLearn.set("Core Unit")
                self.txt9.configure(state = NORMAL)
                self.txt9.focus_set()
            elif self.Subject9.get() == "":
                self.ArtiIntell.set("No")
                self.MachLearn.set("No")
                self.txt9.configure(state = DISABLED)
                self.Module9.set("")

            
#=============================================COURSE DATA===========================================================

        def CourseData(event):
            if self.Course.get() == "BSc Serious Game":
                self.CourseCode.set("BScSG354")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Einstein Zamura")
                self.Head_of_School.set("Mark Zukerberg Anthony")
                self.ProgramLeader.set("Dr. Peter Stone")
                self.CourseTutor1.set("Dr. Rose Royce")
                self.CourseTutor2.set("Dr. Maria Ansari")
                self.Building.set("A Block")
                self.CourseFee.set("900$")

            if self.Course.get() == "BSc Computer Science":
                self.CourseCode.set("BScCS01")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof.Haris Ahmed")
                self.Head_of_School.set("Mark Zukerberg Anthony")
                self.ProgramLeader.set("Dr. Peter Stone")
                self.CourseTutor1.set("Dr. Ayesha Sohail")
                self.CourseTutor2.set("Prof. Dumbledore")
                self.Building.set("B Block")
                self.CourseFee.set("1500$")

            if self.Course.get() == "BA Animation":
                self.CourseCode.set("BAAN01")
                self.Faculty.set("School of Art")
                self.Dean.set("Prof.Waqar Ahmed")
                self.Head_of_School.set("Mark Zukerberg Anthony")
                self.ProgramLeader.set("Dr. Helen Forngal")
                self.CourseTutor1.set("Dr. Rebecca Aison")
                self.CourseTutor2.set("Prof. Emma Stone")
                self.Building.set("Art Block")
                self.CourseFee.set("1000$")

            if self.Course.get() == "BSc Information System":
                self.CourseCode.set("BScIS01")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof.Bill Gates")
                self.Head_of_School.set("Mark Zukerberg Anthony")
                self.ProgramLeader.set("Dr. Peter Stone")
                self.CourseTutor1.set("Dr. Ayesha Sohail")
                self.CourseTutor2.set("Dr. Rehan Aslam")
                self.Building.set("C Block")
                self.CourseFee.set("1200$")

            if self.Course.get() == "BSc Computing":
                self.CourseCode.set("BScCO01")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Snapes")
                self.Head_of_School.set("Mark Zukerberg Anthony")
                self.ProgramLeader.set("Dr. Anna Suzan")
                self.CourseTutor1.set("Dr.Felix Wales")
                self.CourseTutor2.set("Dr. Rose Royce")
                self.Building.set("D Block")
                self.CourseFee.set("1100$")

            if self.Course.get() == "BSc Computer Game":
                self.CourseCode.set("BScCG01")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Collen")
                self.Head_of_School.set("Mark Zukerberg Anthony")
                self.ProgramLeader.set("Dr. Anna Suzan")
                self.CourseTutor1.set("Dr. Sana Ayyan")
                self.CourseTutor2.set("Dr. James Fin")
                self.Building.set("E Block")
                self.CourseFee.set("900$")

            if self.Course.get() == "BSc Computer Animation":
                self.CourseCode.set("BScCA01")
                self.Faculty.set("School of Creative Art and Science")
                self.Dean.set("Prof. Meryem Hollway")
                self.Head_of_School.set("Dr. Fatima Ayyub")
                self.ProgramLeader.set("Dr. Anna Suzan")
                self.CourseTutor1.set("Dr.Malachy Dahmer")
                self.CourseTutor2.set("Prof. Louis Patridge")
                self.Building.set("F Block")
                self.CourseFee.set("1200$")


            if self.Course.get() == "BSc Software Engineering":
                self.CourseCode.set("BScSE01")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Joseph Wakai")
                self.Head_of_School.set("Dr. Hafsa Siddiqui")
                self.ProgramLeader.set("Dr. Naomi Teesa")
                self.CourseTutor1.set("Dr.Leen Dahmer")
                self.CourseTutor2.set("Prof. Sadia Noman")
                self.Building.set("G Block")
                self.CourseFee.set("1400$")

            if self.Course.get() == "BSc Data Science":
                self.CourseCode.set("BScDS01")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Joseph Wakai")
                self.Head_of_School.set("Prof. Hafsa Ayyan")
                self.ProgramLeader.set("Dr. Naomi Teesa")
                self.CourseTutor1.set("Dr.Leen Dahmer")
                self.CourseTutor2.set("Prof. Sadia Noman")
                self.Building.set("H Block")
                self.CourseFee.set("1200$")

            if self.Course.get() == "BSc Artificial Intelligence":
                self.CourseCode.set("BScSE01")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Hammad Khan")
                self.Head_of_School.set("Dr. Xing Yu")
                self.ProgramLeader.set("Dr. Teresa Suzan")
                self.CourseTutor1.set("Dr.Leen Dahmer")
                self.CourseTutor2.set("Prof. Sadia Noman")
                self.Building.set("I Block")
                self.CourseFee.set("1200$")


            if self.Course.get() == "M.Sc. Data Science":
                self.CourseCode.set("MScDS02")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Yusuf Ahmed")
                self.Head_of_School.set("Dr. Xing Yu")
                self.ProgramLeader.set("Dr. Helena Bonham")
                self.CourseTutor1.set("Dr.Carter Faz")
                self.CourseTutor2.set("Prof. Halima Sadia")
                self.Building.set("H Block")
                self.CourseFee.set("1700$")

            if self.Course.get() == "M.Sc. Software Engineering":
                self.CourseCode.set("MScSE02")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Dakota Hollister")
                self.Head_of_School.set("Dr. Xing Yu")
                self.ProgramLeader.set("Prof. Justin Hale")
                self.CourseTutor1.set("Dr.Zubairi")
                self.CourseTutor2.set("Prof.Asif Raza Khan")
                self.Building.set("G Block")
                self.CourseFee.set("1600$")

            if self.Course.get() == "M.Sc. Artificial Intelligence":
                self.CourseCode.set("MScAI02")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof.Ifra Mughal")
                self.Head_of_School.set("Dr. Xing Yu")
                self.ProgramLeader.set("Dr.Yashraj Kumar")
                self.CourseTutor1.set("Dr.Sonia Atif")
                self.CourseTutor2.set("Dr.Hajra binte Asif")
                self.Building.set("I Block")
                self.CourseFee.set("2000$")

            if self.Course.get() == "M.A. Animation":
                self.CourseCode.set("MAAM02")
                self.Faculty.set("School of Art")
                self.Dean.set("Prof. Lupin San")
                self.Head_of_School.set("Dr.Jaziba Shahid")
                self.ProgramLeader.set("Dr.Aaira Sultan")
                self.CourseTutor1.set("Dr.Fabiha Tahir")
                self.CourseTutor2.set("Prof.Hadiq Zafar")
                self.Building.set("Art Block")
                self.CourseFee.set("1500$")

            if self.Course.get() == "Ph.D. Computer Science":
                self.CourseCode.set("PhDCS03")
                self.Faculty.set("School of Computer Science")
                self.Dean.set("Prof. Hammad Khan")
                self.Head_of_School.set("Dr. Xing Yu")
                self.ProgramLeader.set("Dr. Teresa Suzan")
                self.CourseTutor1.set("Dr.Leen Dahmer")
                self.CourseTutor2.set("Prof. Sadia Noman")
                self.Building.set("B Block")
                self.CourseFee.set("1800$")

            if self.Course.get() == "Ph.D. Statistics":
                self.CourseCode.set("PhDST03")
                self.Faculty.set("School of Data and Analytics")
                self.Dean.set("Prof.Cho Chang")
                self.Head_of_School.set("Dr.Layra Jab")
                self.ProgramLeader.set("Dr. Javeria Javed")
                self.CourseTutor1.set("Dr.Mehak Faisa")
                self.CourseTutor2.set("Prof.Anas Mirza")
                self.Building.set("G Block")
                self.CourseFee.set("1000$")

            
        #=====================================ADD MODULE SCORE========================================================

        def AddModulescore():
            if self.Module1.get() == "":
                self.Module1.set("0")
            if self.Module2.get() == "":
                self.Module2.set("0")
            if self.Module3.get() == "":
                self.Module3.set("0")
            if self.Module4.get() == "":
                self.Module4.set("0")
            if self.Module5.get() == "":
                self.Module5.set("0")
            if self.Module6.get() == "":
                self.Module6.set("0")
            if self.Module7.get() == "":
                self.Module7.set("0")
            if self.Module8.get() == "":
                self.Module8.set("0")
            if self.Module9.get() == "":
                self.Module9.set("0")
            


            Unit1 = float(self.Module1.get())
            Unit2 = float(self.Module2.get())
            Unit3 = float(self.Module3.get())
            Unit4 = float(self.Module4.get())
            Unit5 = float(self.Module5.get())
            Unit6 = float(self.Module6.get())
            Unit7 = float(self.Module7.get())
            Unit8 = float(self.Module8.get())
            Unit9 = float(self.Module9.get())
            

            if (Unit1<0 or Unit1>100) or (Unit2<0 or Unit2>100) or (Unit3<0 or Unit3>100) or (Unit4<0 or Unit4>100)\
               or (Unit5<0 or Unit5>100) or (Unit6<0 or Unit6>100) or (Unit7<0 or Unit7>100) or (Unit8<0 or Unit8>100)\
               or (Unit9<0 or Unit9>100) :
                tkinter.messagebox.showerror('Error',"Score must be in the valid range")

            else:
                UnitTotal = (Unit1 + Unit2 + Unit3 + Unit4 + Unit5 + Unit6 + Unit7 + Unit8 + Unit9)
                self.TotalScore.set(int(UnitTotal))

                UnitPercentage = ((Unit1 + Unit2 + Unit3 + Unit4 + Unit5 + Unit6 + Unit7 + Unit8 + Unit9)/900)*100
                self.Percentage.set(int(UnitPercentage))
                    
                if (UnitTotal >= 800):
                    self.Ranking.set("1st Class")
                elif (UnitTotal >= 700):
                    self.Ranking.set("2nd Class")
                elif (UnitTotal >= 600):
                    self.Ranking.set("3rd Class")
                elif (UnitTotal >= 500):
                    self.Ranking.set("4th Class")
                elif (UnitTotal >= 400):
                    self.Ranking.set("CoHE")
                elif (UnitTotal >=300):
                    self.Ranking.set("CoHE")#CoHE stands for Certificate of Higher Education
                elif (UnitTotal <= 300):
                    self.Ranking.set("Fail")

    #=====================================WorkingwithDATABASE====================================================
    #=======================================DataConnectivity=====================================================
    #==========================================ADD DATA==========================================================
        def addData(): #total(82)
            try: 
                    if self.StudentID.get() == "" :
                        tkinter.messagebox.showerror("Error","Student ID cannot be null")
                    else:
                        
                        std = False
                        fname = False
                        sname=False                       
                        pcd=False
                        mob=False
                        enr=False
                        pfname=False
                        psname=False
                        pwp=False
                        pmob=False
                        

                        if self.StudentID.get() != "":
                            if self.StudentID.get().isdigit() :
                                std=True
                            if not std:
                                tkinter.messagebox.showerror("Error","Enter Correct ID")
                        else:
                            tkinter.messagebox.showerror("Error","Student Id field is empty")


                        if self.StudentID.get().isdigit() :
                            if self.Firstname.get() != "":
                                if self.Firstname.get().isalpha():
                                    fname = True
                                if not fname:
                                    tkinter.messagebox.showerror("Error","Enter Correct First Name")
                            else:
                                tkinter.messagebox.showerror("Error","firstname field is empty")
                                

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha():                           
                                if self.Surname.get() != "":
                                    if self.Surname.get().isalpha():
                                        sname = True
                                    if not sname:
                                        tkinter.messagebox.showerror("Error","Enter Correct Surname")
                                else:
                                    tkinter.messagebox.showerror("Error","surname field is empty")



                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha():
                                if self.Address.get() == "":
                                    tkinter.messagebox.showerror("Error","address field is empty")
                            
                        


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "":
                                if self.PostCode.get() != "":
                                    if self.PostCode.get().isalnum() :
                                        pcd=True
                                    if not pcd:
                                        tkinter.messagebox.showerror("Error","Enter Correct Postcode")
                                else:
                                    tkinter.messagebox.showerror("Error","postcode field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum():        
                                if self.Gender.get() == "":
                                    tkinter.messagebox.showerror("Error","gender field is empty")
                                    


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "":
                                if self.DOB.get == "":
                                    tkinter.messagebox.showerror("Error","DOB field is empty")

                                         
                                                
                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "":
                                if self.Mobile.get() != "":
                                    if self.Mobile.get().isdigit() :
                                        mob=True
                                    if not mob:
                                        tkinter.messagebox.showerror("Error","Enter Correct Mobile number")
                                else:
                                    tkinter.messagebox.showerror("Error","mobile field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() :
                                if self.Email.get() == "":
                                    tkinter.messagebox.showerror("Error","email field is empty")


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "":                        
                                if self.EnrollmentNo.get() != "":
                                    if self.EnrollmentNo.get().isalnum() :
                                        enr=True
                                    if not enr:
                                        tkinter.messagebox.showerror("Error","Enter Correct Enrollment No")
                                else:
                                    tkinter.messagebox.showerror("Error","Enrollment field is empty")


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() :
                                if self.Status.get() == "":
                                    tkinter.messagebox.showerror("Error","status field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "":
                                if self.ParentGuidance.get() == "":
                                    tkinter.messagebox.showerror("Error","parent/guidance field is empty")

                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "":
                        
                                if self.pgFirstName.get() != "":
                                    if self.pgFirstName.get().isalpha() :
                                        pfname=True
                                    if not pfname:
                                        tkinter.messagebox.showerror("Error","Enter Correct Name")
                                else:
                                    tkinter.messagebox.showerror("Error","Guidance name field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() :                                         
                                if self.pgSurname.get() != "":
                                    if self.pgSurname.get().isalpha() :
                                        psname=True
                                    if not psname:
                                        tkinter.messagebox.showerror("Error","Enter Correct Surname")
                                else:
                                    tkinter.messagebox.showerror("Error","Guidance Surname field is empty")
                                    
                                    
                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() :
                                if self.pgAddress.get == "":
                                    tkinter.messagebox.showerror("Error","guidance address field is empty")
                                    
                                                                                    
                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() and self.pgAddress.get != "":
                                if self.pgWorkPhone != "":
                                    if self.pgWorkPhone.get().isdigit() :
                                        pwp=True
                                    if not pwp:
                                        tkinter.messagebox.showerror("Error","Enter Correct Workphone No")
                                else:
                                    tkinter.messagebox.showerror("Error","Enter Correct Workphone No")


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() and self.pgAddress.get != "" and \
                           self.pgWorkPhone.get().isdigit() :                                                                    
                                if self.pgMobile.get() != "":
                                    if self.pgMobile.get().isdigit() :
                                        pmob=True
                                    if not pmob:
                                        tkinter.messagebox.showerror("Error","Enter Correct Mobile No")
                                else:
                                    tkinter.messagebox.showerror("Error","Enter Correct Mobile No")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() and self.pgAddress.get != "" and \
                           self.pgWorkPhone.get().isdigit() and self.pgMobile.get().isdigit() :                                                       
                               if self.pgEmail.get() == "":
                                   tkinter.messagebox.showerror("Error","guidance email field is empty")
                                                                                            

                        
                        

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and self.Surname.get().isalpha()\
                           and self.Address.get()!="" and self.PostCode.get().isalnum() and self.Gender.get()!="" and \
                           self.DOB.get()!="" and self.Mobile.get().isdigit() and self.Email.get()!="" and\
                           self.EnrollmentNo.get().isalnum() and self.Status.get()!="" and \
                           self.ParentGuidance.get()!="" and self.pgFirstName.get().isalpha() and self.pgSurname.get().isalpha()\
                           and self.pgAddress.get()!= "" and self.pgWorkPhone.get().isdigit() and self.pgMobile.get().isdigit() \
                           and self.pgEmail.get() !="":
                            
                            sqlCon = pymysql.connect(host = "localhost",user = "root",
                                                     password="5qsT@#yuni",database="studentranking")#password of database
                            cur = sqlCon.cursor()
                            cur.execute("insert into studentranking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                            ,(

                            self.StudentID.get(),
                            self.Firstname.get(),
                            self.Surname.get(),
                            self.Address.get(),
                            self.PostCode.get(),
                            self.Gender.get(),
                            self.DOB.get(),
                            self.Mobile.get(),
                            self.Email.get(),
                            self.EnrollmentNo.get(),
                            self.Status.get(),
                            self.ParentGuidance.get(),
                            self.pgFirstName.get(),
                            self.pgSurname.get(),
                            self.pgAddress.get(),
                            self.pgWorkPhone.get(),
                            self.pgMobile.get(),
                            self.pgEmail.get(),
                            self.Course.get(),
                            self.CourseCode.get(),
                            self.Faculty.get(),
                            self.Dean.get(),
                            self.Head_of_School.get(),
                            self.ProgramLeader.get(),
                            self.CourseTutor1.get(),
                            self.CourseTutor2.get(),
                            self.Building.get(),
                            self.CourseFee.get(),
                            self.HomeStudent.get(),
                            self.Oversea.get(),
                            self.Accommodation.get(),
                            self.ExchangeProg.get(),
                            self.Scholarship.get(),
                            
                            self.BA.get(),
                            self.BSc.get(),
                            self.MA.get(),
                            self.MSc.get(),
                            self.PhD.get(),

                            self.DataScience.get(),
                            self.EventDrivenPro.get(),
                            self.ObjectOriented.get(),
                            self.Spreadsheet.get(),
                            self.SystemAnalysis.get(),
                            self.InformTechnology.get(),
                            self.DigitalGraphics.get(),

                            self.English.get(),
                            self.Games.get(),
                            self.Animation.get(),
                            self.Database1.get(),
                            self.Maths.get(),
                            self.AddMaths.get(),
                            self.Physics.get(),

                            self.Media.get(),
                            self.GraphicD.get(),
                            self.ArtiIntell.get(),
                            self.Architecture.get(),
                            self.MachLearn .get(),
                            self.SocialComput.get(),
                            self.InformSecur.get(),
                            self.NetComm.get(),
                            

                            self.Module1.get(),
                            self.Module2.get(),
                            self.Module3.get(),
                            self.Module4.get(),
                            self.Module5.get(),
                            self.Module6.get(),
                            self.Module7.get(),
                            self.Module8.get(),
                            self.Module9.get(),

                            self.Subject1.get(),
                            self.Subject2.get(),
                            self.Subject3.get(),
                            self.Subject4.get(),
                            self.Subject5.get(),
                            self.Subject6.get(),
                            self.Subject7.get(),
                            self.Subject8.get(),
                            self.Subject9.get(),
                            
                            
                            self.TotalScore.get(),
                            self.Percentage.get(),
                            self.Ranking.get(),
                            self.ResultDate.get(),

                            ))

                            sqlCon.commit()
                            sqlCon.close()
                            DisplayData()
                            tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")
                        

                           


            except Exception as err:#handling IntegrityError exception
                tkinter.messagebox.showerror("Error",err)
            

    #============================================UPDATE===========================================================

        def update():#82
            try:
                if self.StudentID.get() == "" :
                        tkinter.messagebox.showerror("Error","Student ID cannot be null")
                else: 
                        std = False
                        fname = False
                        sname=False                       
                        pcd=False
                        mob=False
                        enr=False
                        pfname=False
                        psname=False
                        pwp=False
                        pmob=False
                        

                        if self.StudentID.get() != "":
                            if self.StudentID.get().isdigit() :
                                std=True
                            if not std:
                                tkinter.messagebox.showerror("Error","Enter Correct ID")
                        else:
                            tkinter.messagebox.showerror("Error","Student Id field is empty")


                        if self.StudentID.get().isdigit() :
                            if self.Firstname.get() != "":
                                if self.Firstname.get().isalpha():
                                    fname = True
                                if not fname:
                                    tkinter.messagebox.showerror("Error","Enter Correct First Name")
                            else:
                                tkinter.messagebox.showerror("Error","firstname field is empty")
                                

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha():                           
                                if self.Surname.get() != "":
                                    if self.Surname.get().isalpha():
                                        sname = True
                                    if not sname:
                                        tkinter.messagebox.showerror("Error","Enter Correct Surname")
                                else:
                                    tkinter.messagebox.showerror("Error","surname field is empty")



                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha():
                                if self.Address.get() == "":
                                    tkinter.messagebox.showerror("Error","address field is empty")
                            
                        


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "":
                                if self.PostCode.get() != "":
                                    if self.PostCode.get().isalnum() :
                                        pcd=True
                                    if not pcd:
                                        tkinter.messagebox.showerror("Error","Enter Correct Postcode")
                                else:
                                    tkinter.messagebox.showerror("Error","postcode field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum():        
                                if self.Gender.get() == "":
                                    tkinter.messagebox.showerror("Error","gender field is empty")
                                    


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "":
                                if self.DOB.get == "":
                                    tkinter.messagebox.showerror("Error","DOB field is empty")

                                         
                                                
                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "":
                                if self.Mobile.get() != "":
                                    if self.Mobile.get().isdigit() :
                                        mob=True
                                    if not mob:
                                        tkinter.messagebox.showerror("Error","Enter Correct Mobile number")
                                else:
                                    tkinter.messagebox.showerror("Error","mobile field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() :
                                if self.Email.get() == "":
                                    tkinter.messagebox.showerror("Error","email field is empty")


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "":                        
                                if self.EnrollmentNo.get() != "":
                                    if self.EnrollmentNo.get().isalnum() :
                                        enr=True
                                    if not enr:
                                        tkinter.messagebox.showerror("Error","Enter Correct Enrollment No")
                                else:
                                    tkinter.messagebox.showerror("Error","Enrollment field is empty")


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() :
                                if self.Status.get() == "":
                                    tkinter.messagebox.showerror("Error","status field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "":
                                if self.ParentGuidance.get() == "":
                                    tkinter.messagebox.showerror("Error","parent/guidance field is empty")

                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "":
                                if self.pgFirstName.get() != "":
                                    if self.pgFirstName.get().isalpha() :
                                        pfname=True
                                    if not pfname:
                                        tkinter.messagebox.showerror("Error","Enter Correct Name")
                                else:
                                    tkinter.messagebox.showerror("Error","Guidance name field is empty")
                                    
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() :                                         
                                if self.pgSurname.get() != "":
                                    if self.pgSurname.get().isalpha() :
                                        psname=True
                                    if not psname:
                                        tkinter.messagebox.showerror("Error","Enter Correct Surname")
                                else:
                                    tkinter.messagebox.showerror("Error","Guidance Surname field is empty")
                                    
                                    
                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() :
                                if self.pgAddress.get == "":
                                    tkinter.messagebox.showerror("Error","guidance address field is empty")
                                    
                                                                                    
                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() and self.pgAddress.get != "":
                                if self.pgWorkPhone != "":
                                    if self.pgWorkPhone.get().isdigit() :
                                        pwp=True
                                    if not pwp:
                                        tkinter.messagebox.showerror("Error","Enter Correct Workphone No")
                                else:
                                    tkinter.messagebox.showerror("Error","guidance workphone field is empty")


                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() and self.pgAddress.get != "" and \
                           self.pgWorkPhone.get().isdigit() :                                                                    
                                if self.pgMobile.get() != "":
                                    if self.pgMobile.get().isdigit() :
                                        pmob=True
                                    if not pmob:
                                        tkinter.messagebox.showerror("Error","Enter Correct Mobile No")
                                else:
                                    tkinter.messagebox.showerror("Error","guidance mobile field is empty")
                                    

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and \
                           self.Surname.get().isalpha() and self.Address.get() != "" and \
                           self.PostCode.get().isalnum() and self.Gender.get() != "" and \
                           self.DOB.get != "" and self.Mobile.get().isdigit() and self.Email.get() != "" and \
                           self.EnrollmentNo.get().isalnum() and self.Status.get() != "" and \
                           self.ParentGuidance.get() != "" and self.pgFirstName.get().isalpha() and \
                           self.pgSurname.get().isalpha() and self.pgAddress.get != "" and \
                           self.pgWorkPhone.get().isdigit() and self.pgMobile.get().isdigit() :                                                       
                               if self.pgEmail.get() == "":
                                   tkinter.messagebox.showerror("Error","guidance email field is empty")
                                                                                                
                        

                        if self.StudentID.get().isdigit() and self.Firstname.get().isalpha() and self.Surname.get().isalpha()\
                           and self.Address.get()!="" and self.PostCode.get().isalnum() and self.Gender.get()!="" and \
                           self.DOB.get()!="" and self.Mobile.get().isdigit() and self.Email.get()!="" and\
                           self.EnrollmentNo.get().isalnum() and self.Status.get()!="" and \
                           self.ParentGuidance.get() !="" and self.pgFirstName.get().isalpha() and self.pgSurname.get().isalpha()\
                           and self.pgAddress.get()!= "" and self.pgWorkPhone.get().isdigit() and self.pgMobile.get().isdigit() \
                           and self.pgEmail.get() !="":

                
                           sqlCon = pymysql.connect(host = "localhost",user = "root",
                                            password="5qsT@#yuni",database="studentranking")#password of database
                           cur = sqlCon.cursor()
                           cur.execute("Update studentranking SET firstname=%s,surname=%s, address=%s, \
                                    postcode=%s, gender=%s, dob=%s, mobile=%s, email=%s,enrollmentno=%s,status=%s, \
                                    parent=%s, pfirstname=%s,psurname=%s, paddress=%s, pworkphone=%s, pmobile=%s, \
                                    pemail=%s, course=%s, coursecode=%s, faculty=%s,deanoffac=%s, hos=%s, proleader=%s,\
                                    coursetutor1=%s,coursetutor2=%s, building=%s, coursefee=%s,homestd=%s,overseastd=%s,\
                                    accommodation=%s, exchange=%s, scholarship=%s, ba=%s, bsc=%s, ma=%s, msc=%s, phd=%s, \
                                    datasci=%s, eventdriprog=%s, objectori=%s, spreadsheet=%s, sysanalysis=%s,\
                                    infotech=%s,digitalgrap=%s, english=%s, games=%s, animation=%s, database1=%s, \
                                    maths1=%s, addmaths1=%s,physics=%s,media=%s,graphicdesign=%s,artificialintel=%s,\
                                    architecture=%s,machinelearn=%s,socialcomputing=%s,informationsecur=%s,\
                                    networkingcomm=%s,module1=%s, module2=%s, module3=%s, module4=%s, \
                                    module5=%s, module6=%s, module7=%s, module8=%s,module9=%s,subject1=%s,subject2=%s, \
                                    subject3=%s,subject4=%s,subject5=%s,subject6=%s,subject7=%s,subject8=%s,subject9=%s,\
                                    totalscore=%s,percentage=%s, ranking=%s, dateofrank=%s \
                                    where studentid = %s",(

                   
                           self.Firstname.get(),
                           self.Surname.get(),
                           self.Address.get(),
                           self.PostCode.get(),
                           self.Gender.get(),
                           self.DOB.get(),
                           self.Mobile.get(),
                           self.Email.get(),
                           self.EnrollmentNo.get(),
                           self.Status.get(),
                           self.ParentGuidance.get(),
                           self.pgFirstName.get(),
                           self.pgSurname.get(),
                           self.pgAddress.get(),
                           self.pgWorkPhone.get(),
                           self.pgMobile.get(),
                           self.pgEmail.get(),
                           self.Course.get(),
                           self.CourseCode.get(),
                           self.Faculty.get(),
                           self.Dean.get(),
                           self.Head_of_School.get(),
                           self.ProgramLeader.get(),
                           self.CourseTutor1.get(),
                           self.CourseTutor2.get(),
                           self.Building.get(),
                           self.CourseFee.get(),
                           self.HomeStudent.get(),
                           self.Oversea.get(),
                           self.Accommodation.get(),
                           self.ExchangeProg.get(),
                           self.Scholarship.get(),
                                
                           self.BA.get(),
                           self.BSc.get(),
                           self.MA.get(),
                           self.MSc.get(),
                           self.PhD.get(),

                           self.DataScience.get(),
                           self.EventDrivenPro.get(),
                           self.ObjectOriented.get(),
                           self.Spreadsheet.get(),
                           self.SystemAnalysis.get(),
                           self.InformTechnology.get(),
                           self.DigitalGraphics.get(),

                           self.English.get(),
                           self.Games.get(),
                           self.Animation.get(),
                           self.Database1.get(),
                           self.Maths.get(),
                           self.AddMaths.get(),
                           self.Physics.get(),

                           self.Media.get(),
                           self.GraphicD.get(),
                           self.ArtiIntell.get(),
                           self.Architecture.get(),
                           self.MachLearn .get(),
                           self.SocialComput.get(),
                           self.InformSecur.get(),
                           self.NetComm.get(),
                          

                           self.Module1.get(),
                           self.Module2.get(),
                           self.Module3.get(),
                           self.Module4.get(),
                           self.Module5.get(),
                           self.Module6.get(),
                           self.Module7.get(),
                           self.Module8.get(),
                           self.Module9.get(),
                           

                           self.Subject1.get(),
                           self.Subject2.get(),
                           self.Subject3.get(),
                           self.Subject4.get(),
                           self.Subject5.get(),
                           self.Subject6.get(),
                           self.Subject7.get(),
                           self.Subject8.get(),
                           self.Subject9.get(),
                           
                           self.TotalScore.get(),
                           self.Percentage.get(),
                           self.Ranking.get(),
                           self.ResultDate.get(),

                           self.StudentID.get()

                           ))

                           sqlCon.commit()
                           DisplayData()
                           sqlCon.close()
                           tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Updated")

            except Exception as err:
                tkinter.messagebox.showerror("Error",err)

        #===========================================DELETE========================================================

        def deletedb():
            
            if self.StudentID.get() != "":
                sqlCon = pymysql.connect(host = "localhost",user = "root",
                                         password="5qsT@#yuni", database="studentranking")#password of database
                cur = sqlCon.cursor()
                cur.execute("delete from studentranking where studentid=%s", self.StudentID.get())

                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Deleted")
                Reset()
            else:
                tkinter.messagebox.showerror("Error","No Record to delete")
                                             
        #========================================DISPLAY DATA===================================================   

        def DisplayData():
           sqlCon = pymysql.connect(host = "localhost",user = "root",
                                    password="5qsT@#yuni", database="studentranking")#password of database
           cur = sqlCon.cursor()
           cur.execute("SELECT * FROM studentranking")
           result = cur.fetchall()
           if len(result)!=0:
               self.Student_Record.delete(*self.Student_Record.get_children())
               for row in result:
                   self.Student_Record.insert('',END,values=row)
               sqlCon.commit()
           sqlCon.close()
           
        #=====================================STU INFO===========================================================   

        def stuInfo(event):
           viewInfo = self.Student_Record.focus()
           learnerData = self.Student_Record.item(viewInfo)
           row = learnerData ['values']

           self.StudentID.set(row[0])
           self.Firstname.set(row[1])
           self.Surname.set(row[2])
           self.Address.set(row[3])
           self.PostCode.set(row[4])
           self.Gender.set(row[5])
           self.DOB.set(row[6])
           self.Mobile.set(row[7])
           self.Email.set(row[8])
           self.EnrollmentNo.set(row[9])
           self.Status.set(row[10])
           
           self.ParentGuidance.set(row[11])
           self.pgFirstName.set(row[12])
           self.pgSurname.set(row[13])
           self.pgAddress.set(row[14])
           self.pgWorkPhone.set(row[15])
           self.pgMobile.set(row[16])
           self.pgEmail.set(row[17])
           self.Course.set(row[18])
           self.CourseCode.set(row[19])
           self.Faculty.set(row[20])
           self.Dean.set(row[21])
           self.Head_of_School.set(row[22])
           self.ProgramLeader.set(row[23])
           self.CourseTutor1.set(row[24])
           self.CourseTutor2.set(row[25])
           self.Building.set(row[26])
           self.CourseFee.set(row[27])
           self.HomeStudent.set(row[28])
           self.Oversea.set(row[29])
           self.Accommodation.set(row[30])
           self.ExchangeProg.set(row[31])
           self.Scholarship.set(row[32])
                
           self.BA.set(row[33])
           self.BSc.set(row[34])
           self.MA.set(row[35])
           self.MSc.set(row[36])
           self.PhD.set(row[37])

           self.DataScience.set(row[38])
           self.EventDrivenPro.set(row[39])
           self.ObjectOriented.set(row[40])
           self.Spreadsheet.set(row[41])
           self.SystemAnalysis.set(row[42])
           self.InformTechnology.set(row[43])
           self.DigitalGraphics.set(row[44])

           self.English.set(row[45])
           self.Games.set(row[46])
           self.Animation.set(row[47])
           self.Database1.set(row[48])
           self.Maths.set(row[49])
           self.AddMaths.set(row[50])
           self.Physics.set(row[51])

           self.Media.set(row[52])
           self.GraphicD.set(row[53])
           self.ArtiIntell.set(row[54])
           self.Architecture.set(row[55])
           self.MachLearn .set(row[56])
           self.SocialComput.set(row[57])
           self.InformSecur.set(row[58])
           self.NetComm.set(row[59])
           

           self.Module1.set(row[60])
           self.Module2.set(row[61])
           self.Module3.set(row[62])
           self.Module4.set(row[63])
           self.Module5.set(row[64])
           self.Module6.set(row[65])
           self.Module7.set(row[66])
           self.Module8.set(row[67])
           self.Module9.set(row[68])

           self.Subject1.set(row[69])
           self.Subject2.set(row[70])
           self.Subject3.set(row[71])
           self.Subject4.set(row[72])
           self.Subject5.set(row[73])
           self.Subject6.set(row[74])
           self.Subject7.set(row[75])
           self.Subject8.set(row[76])
           self.Subject9.set(row[77])
           
           self.TotalScore.set(row[78])
           self.Percentage.set(row[79])
           self.Ranking.set(row[80])
           self.ResultDate.set(row[81])
           

        #=========================================SEARCH=========================================================

        def searchDB():
            try:
                if self.StudentID.get() == "":
                   tkinter.messagebox.showerror("Error","StudentID cannot be null")    
                else:
                    sqlCon = pymysql.connect(host = "localhost",user = "root",
                                            password="5qsT@#yuni",database="studentranking")#password of database
                    cur = sqlCon.cursor()
                    cur.execute("SELECT* FROM studentranking WHERE studentid=%s",self.StudentID.get())

                    row = cur.fetchone()
                
                    self.StudentID.set(row[0])
                    self.Firstname.set(row[1])
                    self.Surname.set(row[2])
                    self.Address.set(row[3])
                    self.PostCode.set(row[4])
                    self.Gender.set(row[5])
                    self.DOB.set(row[6])
                    self.Mobile.set(row[7])
                    self.Email.set(row[8])
                    self.EnrollmentNo.set(row[9])
                    self.Status.set(row[10])
                
                    self.ParentGuidance.set(row[11])
                    self.pgFirstName.set(row[12])
                    self.pgSurname.set(row[13])
                    self.pgAddress.set(row[14])
                    self.pgWorkPhone.set(row[15])
                    self.pgMobile.set(row[16])
                    self.pgEmail.set(row[17])
                    self.Course.set(row[18])
                    self.CourseCode.set(row[19])
                    self.Faculty.set(row[20])
                    self.Dean.set(row[21])
                    self.Head_of_School.set(row[22])
                    self.ProgramLeader.set(row[23])
                    self.CourseTutor1.set(row[24])
                    self.CourseTutor2.set(row[25])
                    self.Building.set(row[26])
                    self.CourseFee.set(row[27])
                    self.HomeStudent.set(row[28])
                    self.Oversea.set(row[29])
                    self.Accommodation.set(row[30])
                    self.ExchangeProg.set(row[31])
                    self.Scholarship.set(row[32])
                        
                    self.BA.set(row[33])
                    self.BSc.set(row[34])
                    self.MA.set(row[35])
                    self.MSc.set(row[36])
                    self.PhD.set(row[37])

                    self.DataScience.set(row[38])
                    self.EventDrivenPro.set(row[39])
                    self.ObjectOriented.set(row[40])
                    self.Spreadsheet.set(row[41])
                    self.SystemAnalysis.set(row[42])
                    self.InformTechnology.set(row[43])
                    self.DigitalGraphics.set(row[44])

                    self.English.set(row[45])
                    self.Games.set(row[46])
                    self.Animation.set(row[47])
                    self.Database1.set(row[48])
                    self.Maths.set(row[49])
                    self.AddMaths.set(row[50])
                    self.Physics.set(row[51])
                   

                    self.Media.set(row[52])
                    self.GraphicD.set(row[53])
                    self.ArtiIntell.set(row[54])
                    self.Architecture.set(row[55])
                    self.MachLearn .set(row[56])
                    self.SocialComput.set(row[57])
                    self.InformSecur.set(row[58])
                    self.NetComm.set(row[59])
           

                    self.Module1.set(row[60])
                    self.Module2.set(row[61])
                    self.Module3.set(row[62])
                    self.Module4.set(row[63])
                    self.Module5.set(row[64])
                    self.Module6.set(row[65])
                    self.Module7.set(row[66])
                    self.Module8.set(row[67])
                    self.Module9.set(row[68])
                    

                    self.Subject1.set(row[69])
                    self.Subject2.set(row[70])
                    self.Subject3.set(row[71])
                    self.Subject4.set(row[72])
                    self.Subject5.set(row[73])
                    self.Subject6.set(row[74])
                    self.Subject7.set(row[75])
                    self.Subject8.set(row[76])
                    self.Subject9.set(row[77])
                
           
                    self.TotalScore.set(row[78])
                    self.Percentage.set(row[79])
                    self.Ranking.set(row[80])
                    self.ResultDate.set(row[81])
                    
                    sqlCon.commit()
                    sqlCon.close()
                    
            except Exception as err:
                tkinter.messagebox.showinfo("MySQL Connection","Record Not Found")
                Reset()
            
        #===========================================FRAMES========================================================
         
        MainFrame = Frame(self.TabControl1, bd=10, width=1350, height=700, relief=RIDGE) 
        MainFrame.grid(padx=5, pady=10)

        Tab2Frame = Frame(self.TabControl2, bd=10, width=2000, height=830,bg="cadetblue", relief=RIDGE)
        Tab2Frame.grid(padx=10)


        TopFrame1 = Frame(MainFrame, bd=10, width=1570, height=120, bg="cadetblue", relief=RIDGE)
        TopFrame1.grid()

        TopFrame3 = Frame(MainFrame, bd=10, width=1340, height=500, relief=RIDGE) 
        TopFrame3.grid()
        
        RightFrame1 = Frame(TopFrame3, bd=5, width=320, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        RightFrame1.pack(side=RIGHT, pady=1)

        InnerRightFrame = Frame(RightFrame1, bd=5, width=310, height=300, padx=2, relief=RIDGE)
        InnerRightFrame.pack(side=TOP, pady=2)

        CalendarFrame = Frame(InnerRightFrame,bd=5, width=310, height=300, padx=2, relief=RIDGE)
        CalendarFrame.pack(side=TOP, pady=1)

        UnitsFrame = Frame(InnerRightFrame,bd=5, width=310, height=300, padx=2, relief=RIDGE)
        UnitsFrame.pack(side=TOP, pady=1)

        ResultFrame = Frame(InnerRightFrame,bd=5, width=330, height=50, padx=2, relief=RIDGE)
        ResultFrame.pack(side=TOP, pady=1)

        ResultFrameLeft = Frame(ResultFrame, bd=0, width=130, height=50, padx=2, relief=RIDGE)
        ResultFrameLeft.grid(row=0, column=0, pady=1)

        ResultFrameRight = Frame(ResultFrame, bd=0, width=200, height=50, padx=2, relief=RIDGE)
        ResultFrameRight.grid(row=0, column=1)

        UnitNo = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, relief=RIDGE)
        UnitNo.grid(row=0, column=0, pady=2)
        UnitSubject = Frame(UnitsFrame, bd=1, width=210, height=300, padx=2, pady=4, relief=RIDGE)
        UnitSubject.grid(row=0, column=1, pady=2)
        UnitScore = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, pady=3, relief=RIDGE)
        UnitScore.grid(row=0, column=2, pady=1)
        #==============================================================================================

        LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        LeftFrame.pack(side=RIGHT, pady=0)
        CourseFrame = Frame(LeftFrame, bd=5, width=600, height=180, padx=4, relief=RIDGE)
        CourseFrame.pack(side=TOP, pady=2)

        LeftFrame2 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, bg="cadetblue", relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        StudentStatusFrame = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        StudentStatusFrame.pack(side=LEFT)
        DegreeFrame = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2, relief=RIDGE)
        DegreeFrame.pack(side=RIGHT)

        ButtonFrame = Frame(LeftFrame, bd=5, width=320, height=50, padx=3, relief=RIDGE)
        ButtonFrame.pack(side=LEFT, pady=3)
        

        RightFrame2 = Frame(TopFrame3, bd=5, width=300, height=400, padx=2, bg="cadetblue", relief=RIDGE)
        RightFrame2.pack(side=LEFT, pady=5)
        StudentFrame = Frame(RightFrame2, bd=5, width=280, height=50, padx=2, relief=RIDGE)
        StudentFrame.pack(side=TOP, pady=3)
        ParentFrame = Frame(RightFrame2, bd=5, width=280, height=50, padx=3, relief=RIDGE)
        ParentFrame.pack(side=TOP)
        #===================================TAB2 FRAME================================================
        
        TopFrame12 = Frame(Tab2Frame, bd=2, width=1520, height=180,bg="cadetblue", relief=RIDGE)
        TopFrame12.grid()#mainframe ka andar wala frame

        TopFrame12a = Frame(TopFrame12, bd=15, width=1000, height=100,padx=10,pady=135, relief=RIDGE)
        TopFrame12a.grid(row=0, column=1)#right frame

        TopFrame12b = Frame(TopFrame12, bd=2, width=400, height=100,padx=1, relief=RIDGE)
        TopFrame12b.grid(row=0, column=0)#left frame

        
        #=======================================MAIN TITLE===================================================
        
        self.lblTitle = Label(TopFrame1, font=('arial',60,'bold'), text="STANFORD UNIVERSITY"
                              ,bd=5,justify=CENTER,bg="white", fg="cadetblue")                                                                              
        self.lblTitle.grid(padx=295)

        #==========================================STUDENT DETAILS=====================================================

        self.lblStudentID = Label(StudentFrame, font=('arial',12,'bold'), text='Student ID', bd=5, anchor="w",
                                                      justify=LEFT)
        self.lblStudentID.grid(row=0,column=0, sticky =W, padx=5, pady=5)
        self.txtStudentID = Entry(StudentFrame, font=('arial',12,'bold'),bd=5,width=35, justify="left",
                                  textvariable=self.StudentID)
        self.txtStudentID.grid(row=0,column=1)


        self.lblFirstname = Label(StudentFrame, font=('arial',12,'bold'), text='First Name', bd=7,justify=LEFT)
        self.lblFirstname.grid(row=1,column=0, sticky =W, padx=5)
        self.txtFirstname = Entry(StudentFrame, font=('arial',12,'bold'),bd=5,width=35, justify="left",
                                  textvariable=self.Firstname)
        self.txtFirstname.grid(row=1,column=1)


        self.lblSurname = Label(StudentFrame, font=('arial',12,'bold'), text='Surname', bd=5)                                               
        self.lblSurname.grid(row=2,column=0, sticky =W, padx=5)
        self.txtSurname = Entry(StudentFrame, font=('arial',12,'bold'),bd=5,width=35,textvariable=self.Surname)
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress = Label(StudentFrame, font=('arial',12,'bold'), text='Address', bd=5)                                               
        self.lblAddress.grid(row=3,column=0, sticky =W, padx=5)
        self.txtAddress = Entry(StudentFrame, font=('arial',12,'bold'),bd=5,width=35,textvariable=self.Address)
        self.txtAddress.grid(row=3,column=1)

        self.lblPostCode = Label(StudentFrame, font=('arial',12,'bold'), text='PostCode', bd=5)                                               
        self.lblPostCode.grid(row=4,column=0, sticky =W, padx=5)
        self.txtPostCode = Entry(StudentFrame, font=('arial',12,'bold'),bd=5,width=35,textvariable=self.PostCode)
        self.txtPostCode.grid(row=4,column=1)

        self.lblGender = Label(StudentFrame, font=('arial',12,'bold'), text='Gender', bd=5)                                               
        self.lblGender.grid(row=5,column=0, sticky =W, padx=5)
        
        self.cboGender = ttk.Combobox(StudentFrame, textvariable = self.Gender, width=34,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboGender['value']= ('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)
        
#========================================DOB============================================================

        self.lblDOB = Label(StudentFrame, font=('arial',12,'bold'), text='DOB', bd=5)                                               
        self.lblDOB.grid(row=6,column=0, sticky =W, padx=5)
        self.txtDOB = DateEntry(StudentFrame, font=('arial',12,'bold'),bd=5,width=34, borderwidth=2,
                                date_pattern='dd/mm/yy',textvariable=self.DOB)
        self.txtDOB.grid(row=6,column=1)


        self.lblMobile = Label(StudentFrame, font=('arial',12,'bold'),text="Mobile",bd=5)
        self.lblMobile.grid(row=7, column=0, sticky=W, padx=5)
        self.txtMobile = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width=35
                                ,textvariable = self.Mobile)
        self.txtMobile.grid(row=7,column=1)

        self.lblEmail = Label(StudentFrame, font=('arial',12,'bold'),text="Email",bd=5)
        self.lblEmail.grid(row=8, column=0, sticky=W, padx=5)
        self.txtEmail = Entry(StudentFrame, font=('arial',12,'bold'),bd=5, width=35
                                ,textvariable = self.Email)
        self.txtEmail.grid(row=8,column=1)


        self.lblEnrollmentNo = Label(StudentFrame, font=('arial',12,'bold'), text='Enrollment No',
                                     bd=5, anchor="w",justify=LEFT)
        self.lblEnrollmentNo.grid(row=9,column=0, sticky =W, padx=5, pady=5)
        self.txtEnrollmentNo = Entry(StudentFrame, font=('arial',12,'bold'),bd=5,width=35, justify="left",
                                  textvariable=self.EnrollmentNo)
        self.txtEnrollmentNo.grid(row=9,column=1)


        self.lblStatus = Label(StudentFrame, font=('arial',12,'bold'), text='Status', bd=5)                                               
        self.lblStatus.grid(row=10,column=0, sticky =W, padx=5)
        
        self.cboStatus = ttk.Combobox(StudentFrame, textvariable = self.Status, width=34,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboStatus['value']= ('','Married','Single')
        self.cboStatus.current(0)
        self.cboStatus.grid(row=10, column=1)
        
#==============================================GUIDANCE DETAILS============================================================

        self.lblParentGuidance = Label(ParentFrame, font=('arial',12,'bold'), text='Parent or Guidance', bd=5)                                               
        self.lblParentGuidance.grid(row=0,column=0, sticky =W, padx=5)
        
        self.cboParentGuidance = ttk.Combobox(ParentFrame, textvariable = self.ParentGuidance, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboParentGuidance['value']= ('','Mother','Father','Brother','Sister','Guidance')
        self.cboParentGuidance.current(0)
        self.cboParentGuidance.grid(row=0, column=1)

        self.lblFirstname = Label(ParentFrame, font=('arial',12,'bold'), text='First Name', bd=7,justify=LEFT)
        self.lblFirstname.grid(row=1,column=0, sticky =W, padx=5)
        self.txtFirstname = Entry(ParentFrame, font=('arial',12,'bold'),bd=5,width=31, justify="left",
                                  textvariable=self.pgFirstName)
        self.txtFirstname.grid(row=1,column=1)


        self.lblSurname = Label(ParentFrame, font=('arial',12,'bold'), text='Surname', bd=5)                                               
        self.lblSurname.grid(row=2,column=0, sticky =W, padx=5)
        self.txtSurname = Entry(ParentFrame, font=('arial',12,'bold'),bd=5,width=31,textvariable=self.pgSurname)
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress = Label(ParentFrame, font=('arial',12,'bold'), text='Address', bd=5)                                               
        self.lblAddress.grid(row=3,column=0, sticky =W, padx=5)
        self.txtAddress = Entry(ParentFrame, font=('arial',12,'bold'),bd=5,width=31,textvariable=self.pgAddress)
        self.txtAddress.grid(row=3,column=1)

        self.lblWorkPhone = Label(ParentFrame, font=('arial',12,'bold'), text='Work Phone no', bd=5)                                               
        self.lblWorkPhone.grid(row=4,column=0, sticky =W, padx=5)
        self.txtWorkPhone = Entry(ParentFrame, font=('arial',12,'bold'),bd=5,width=31,
                                  textvariable=self.pgWorkPhone)
        self.txtWorkPhone.grid(row=4,column=1)

        self.lblMobile = Label(ParentFrame, font=('arial',12,'bold'), text='Mobile', bd=5)                                               
        self.lblMobile.grid(row=5,column=0, sticky =W, padx=5)
        self.txtMobile= Entry(ParentFrame, font=('arial',12,'bold'),bd=5,width=31,textvariable=self.pgMobile)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail = Label(ParentFrame, font=('arial',12,'bold'), text='Email', bd=5)                                               
        self.lblEmail.grid(row=6,column=0, sticky =W, padx=5)
        self.txtEmail = Entry(ParentFrame, font=('arial',12,'bold'),bd=5,width=31,textvariable=self.pgEmail)
        self.txtEmail.grid(row=6,column=1,pady=3)
        #=====================================COURSE DETAILS========================================================

        self.Course.set("Course Selector")
        self.lblCourse = Label(CourseFrame, font=('arial',12,'bold'), text='Course', bd=6)                                               
        self.lblCourse.grid(row=0,column=0, sticky =W)

        self.cboCourse= ttk.Combobox(CourseFrame, textvariable = self.Course, width=58,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboCourse['value']= ('BSc Serious Game','BSc Computer Science','BA Animation',
                                  'BSc Information System','BSc Computing','BSc Computer Game',
                                  'BSc Computer Animation','BSc Software Engineering', 'BSc Data Science',
                                  'BSc Artificial Intelligence','M.Sc. Data Science','M.Sc. Software Engineering',
                                  'M.Sc. Artificial Intelligence','M.A. Animation',
                                  'Ph.D. Computer Science','Ph.D. Statistics' )
        self.cboCourse.grid(row=0, column=1)
        self.cboCourse.bind('<<ComboboxSelected>>',CourseData)
        
        self.lblCourseCode = Label(CourseFrame, font=('arial',12,'bold'), text='Course Code', bd=6)                                               
        self.lblCourseCode.grid(row=1,column=0, sticky =W, padx=5)
        self.txtCourseCode = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify="left",
                                   textvariable=self.CourseCode)
        self.txtCourseCode.grid(row=1,column=1)

        self.lblFaculty = Label(CourseFrame, font=('arial',12,'bold'), text='Faculty Name', bd=6)                                               
        self.lblFaculty.grid(row=2,column=0, sticky =W)
        self.txtFaculty = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.Faculty)
        self.txtFaculty.grid(row=2,column=1)

        self.lblDean = Label(CourseFrame, font=('arial',12,'bold'), text='Dean of Faculty', bd=6)                                               
        self.lblDean.grid(row=3,column=0, sticky =W)
        self.txtDean = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.Dean)
        self.txtDean.grid(row=3,column=1)

        self.lblHoS = Label(CourseFrame, font=('arial',12,'bold'), text='Head of School', bd=6)                                               
        self.lblHoS.grid(row=4,column=0)
        self.txtHoS = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.Head_of_School)
        self.txtHoS.grid(row=4,column=1)

        self.lblProgramLeader = Label(CourseFrame, font=('arial',12,'bold'), text='Program Leader', bd=6)                                               
        self.lblProgramLeader.grid(row=5,column=0)
        self.txtProgramLeader = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.ProgramLeader)
        self.txtProgramLeader.grid(row=5,column=1)

        self.lblCourseTutor1 = Label(CourseFrame, font=('arial',12,'bold'), text='Course Tutor1', bd=6)                                               
        self.lblCourseTutor1.grid(row=6,column=0, sticky=W)
        self.txtCourseTutor1 = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.CourseTutor1)
        self.txtCourseTutor1.grid(row=6,column=1)

        
        self.lblCourseTutor2 = Label(CourseFrame, font=('arial',12,'bold'), text='Course Tutor2', bd=6)                                               
        self.lblCourseTutor2.grid(row=7,column=0, sticky=W)
        self.txtCourseTutor2 = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.CourseTutor2)
        self.txtCourseTutor2.grid(row=7,column=1)
        

        self.lblBuilding = Label(CourseFrame, font=('arial',12,'bold'), text='Building', bd=6)                                               
        self.lblBuilding.grid(row=8,column=0, sticky=W)
        self.txtBuilding = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.Building)
        self.txtBuilding.grid(row=8,column=1)

        self.lblCourseFee = Label(CourseFrame, font=('arial',12,'bold'), text='Course Fee', bd=6)                                               
        self.lblCourseFee.grid(row=9,column=0, sticky=W)
        self.txtCourseFee = Entry(CourseFrame, font=('arial',12,'bold'),bd=5,width=59,justify = "left",
                                   textvariable=self.CourseFee)
        self.txtCourseFee.grid(row=9,column=1)

        #=======================================STUDENT STATUS============================================

        self.lblHomeStudent = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Home Student', bd=6)                                               
        self.lblHomeStudent .grid(row=0,column=0, sticky =W)

        self.cboHomeStudent = ttk.Combobox(StudentStatusFrame, textvariable = self.HomeStudent, width=18,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboHomeStudent ['value']= ('No','Yes')
        self.cboHomeStudent.current(0)
        self.cboHomeStudent .grid(row=0, column=1,pady=8)
        

        self.lblOversea = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Oversea', bd=6)                                               
        self.lblOversea .grid(row=1,column=0, sticky =W)

        self.cboOversea = ttk.Combobox(StudentStatusFrame, textvariable = self.Oversea, width=18,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboOversea ['value']= ('No','Yes')
        self.cboOversea.current(0)
        self.cboOversea .grid(row=1, column=1,pady=8)
        

        self.lblAccommodation = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Accommodation', bd=6)                                               
        self.lblAccommodation .grid(row=2,column=0, sticky =W)

        self.cboAccommodation = ttk.Combobox(StudentStatusFrame, textvariable = self.Accommodation, width=18,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboAccommodation ['value']= ('No','Yes')
        self.cboAccommodation.current(0)
        self.cboAccommodation .grid(row=2, column=1,pady=8)


        self.lblExchangeProg = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Exchange Prog', bd=10)                                               
        self.lblExchangeProg .grid(row=3,column=0, sticky =W)

        self.cboExchangeProg = ttk.Combobox(StudentStatusFrame, textvariable = self.ExchangeProg, width=18,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboExchangeProg['value']= ('No','Yes')
        self.cboExchangeProg.current(0)
        self.cboExchangeProg .grid(row=3, column=1)

        
        self.lblScholarship = Label(StudentStatusFrame, font=('arial',12,'bold'), text='Scholarship', bd=10)                                               
        self.lblScholarship.grid(row=4,column=0, sticky =W)

        self.cboScholarship = ttk.Combobox(StudentStatusFrame, textvariable = self.Scholarship, width=18,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboScholarship['value']= ('No','Yes')
        self.cboScholarship.current(0)
        self.cboScholarship .grid(row=4, column=1)

        #========================================DEGREE=====================================================

        self.lblBA = Label(DegreeFrame, font=('arial',12,'bold'), text='Bachelor of Art', bd=10)                                               
        self.lblBA .grid(row=0,column=0, sticky =W)

        self.SpBA = Spinbox(DegreeFrame,from_=0, to=20, width=12, font=('arial',14,'bold'),
                                       textvariable = self.BA)
        self.SpBA .grid(row=0, column=1,pady=5)
        

        self.lblBSc = Label(DegreeFrame, font=('arial',12,'bold'), text='Bachelor of Science', bd=10)                                               
        self.lblBSc .grid(row=1,column=0, sticky =W)

        self.SpBSc = Spinbox(DegreeFrame,from_=0, to=20, width=12, font=('arial',14,'bold'),
                                       textvariable = self.BSc)
        self.SpBSc .grid(row=1, column=1,pady=5)
        

        self.lblMA = Label(DegreeFrame, font=('arial',12,'bold'), text='Master of Art', bd=10,anchor='e')                                               
        self.lblMA .grid(row=2,column=0, sticky =W)

        self.SpMA = Spinbox(DegreeFrame,from_=0, to=20, width=12, font=('arial',14,'bold'),
                                       textvariable = self.MA)
        self.SpMA .grid(row=2, column=1,pady=5)


        self.lblMSc = Label(DegreeFrame, font=('arial',12,'bold'), text='Master of Science', bd=10)                                               
        self.lblMSc.grid(row=3,column=0, sticky =W)

        self.SpMSc = Spinbox(DegreeFrame,from_=0, to=20, width=12, font=('arial',14,'bold'),
                                       textvariable = self.MSc)
        self.SpMSc .grid(row=3, column=1,pady=5)


        self.lblPhD = Label(DegreeFrame, font=('arial',12,'bold'), text='Doctor of Philosophy', bd=10)                                               
        self.lblPhD .grid(row=4,column=0, sticky =W)

        self.SpPhD = Spinbox(DegreeFrame,from_=0, to=20, width=12, font=('arial',14,'bold'),
                                       textvariable = self.PhD)
        self.SpPhD.grid(row=4, column=1,pady=5)

        #======================================CalendarFrame=========================================================
        #=====================================GET SELECTED DATE=================================================
        def getSelectedDate():
            nowDate = cal.get_date()
            self.ResultDate.set(nowDate)
            AddModulescore()
            
        cal = Calendar(CalendarFrame, selectmode='day', date_pattern='dd-mm-yy', font=('arial',9,'bold'),
                       padx=100)
        cal.grid(row=0, column=0)

        #=======================================UNIT NO=========================================================

        self.lblNo = Label(UnitNo, font=('arial',12,'bold'), text='No',padx=1)                                               
        self.lblNo.grid(row=0,column=0, sticky =W)
        
        self.lbl1 = Label(UnitNo, font=('arial',12,'bold'), text='1',padx=2, pady=3)                                               
        self.lbl1.grid(row=1,column=0, sticky =W)
        
        self.lbl2 = Label(UnitNo, font=('arial',12,'bold'), text='2',padx=2, pady=3)                                               
        self.lbl2.grid(row=2,column=0, sticky =W)
        
        self.lbl3 = Label(UnitNo, font=('arial',12,'bold'), text='3',padx=2, pady=3)                                               
        self.lbl3.grid(row=3,column=0, sticky =W)
        
        self.lbl4 = Label(UnitNo, font=('arial',12,'bold'), text='4',padx=2, pady=3)                                               
        self.lbl4.grid(row=4,column=0, sticky =W)
        
        self.lbl5 = Label(UnitNo, font=('arial',12,'bold'), text='5',padx=2, pady=3)                                               
        self.lbl5.grid(row=5,column=0, sticky =W)
        
        self.lbl6 = Label(UnitNo, font=('arial',12,'bold'), text='6',padx=2, pady=3)                                               
        self.lbl6.grid(row=6,column=0, sticky =W)
        
        self.lbl7 = Label(UnitNo, font=('arial',12,'bold'), text='7',padx=2, pady=3)                                               
        self.lbl7.grid(row=7,column=0, sticky =W)
        
        self.lbl8 = Label(UnitNo, font=('arial',12,'bold'), text='8',padx=2, pady=3)                                               
        self.lbl8.grid(row=8,column=0, sticky =W)

        self.lbl9 = Label(UnitNo, font=('arial',12,'bold'), text='9',padx=2, pady=3)                                               
        self.lbl9.grid(row=9,column=0, sticky =W)#
        
        #=========================================UNIT SUBJECTS================================================

        self.lblSelectUnit = Label(UnitSubject, font=('arial',14,'bold'), text='Select the Subject')                                               
        self.lblSelectUnit.grid(row=0,column=0, sticky =W)

        self.cboSubject1 = ttk.Combobox(UnitSubject, textvariable = self.Subject1, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject1['value']= ('','Event Driven Program','Computer Architecture',
                                    'Social Computing')
        self.cboSubject1.current(0)
        self.cboSubject1.grid(row=1, column=0, padx=2, pady=3)
        self.cboSubject1.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject2 = ttk.Combobox(UnitSubject, textvariable = self.Subject2, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject2['value']= ('','Object Oriented',"Spreadsheet")
        self.cboSubject2.current(0)
        self.cboSubject2.grid(row=2, column=0, padx=2, pady=3)
        self.cboSubject2.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject3 = ttk.Combobox(UnitSubject, textvariable = self.Subject3, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject3['value']= ('','System Analysis',"Information Technology",'Information Security')
        self.cboSubject3.current(0)
        self.cboSubject3.grid(row=3, column=0, padx=2, pady=3)
        self.cboSubject3.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject4 = ttk.Combobox(UnitSubject, textvariable = self.Subject4, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject4['value']= ('','Digital Graphics',"English")
        self.cboSubject4.current(0)
        self.cboSubject4.grid(row=4, column=0, padx=2, pady=3)
        self.cboSubject4.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject5 = ttk.Combobox(UnitSubject, textvariable = self.Subject5, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject5['value']= ('','Games','Animation','Media','Graphic Designing')
        self.cboSubject5.current(0)
        self.cboSubject5.grid(row=5, column=0, padx=2, pady=3)
        self.cboSubject5.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject6 = ttk.Combobox(UnitSubject, textvariable = self.Subject6, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject6['value']= ('','Database','Maths')
        self.cboSubject6.current(0)
        self.cboSubject6.grid(row=6, column=0, padx=2, pady=3)
        self.cboSubject6.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject7 = ttk.Combobox(UnitSubject, textvariable = self.Subject7, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject7['value']= ('','AddMaths',"Physics")
        self.cboSubject7.current(0)
        self.cboSubject7.grid(row=7, column=0, padx=2, pady=3)
        self.cboSubject7.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject8 = ttk.Combobox(UnitSubject, textvariable = self.Subject8, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject8['value']= ('','DataScience','Networking and Communications')
        self.cboSubject8.current(0)
        self.cboSubject8.grid(row=8, column=0, padx=2, pady=3)
        self.cboSubject8.bind('<<ComboboxSelected>>',setSubject)

        self.cboSubject9 = ttk.Combobox(UnitSubject, textvariable = self.Subject9, width=22,
                                       font=('arial',10,'bold'), state = 'readonly')
        self.cboSubject9['value']= ('','Artificial Intelligence',"Machine Learning")
        self.cboSubject9.current(0)
        self.cboSubject9.grid(row=9, column=0, padx=2, pady=3)
        self.cboSubject9.bind('<<ComboboxSelected>>',setSubject)#


        #=========================================UNIT SCORE==================================================

        self.lblSUnit = Label(UnitScore, font=('arial',12,'bold'), text='Score')                                               
        self.lblSUnit.grid(row=0,column=0, sticky =W)

        self.txt1 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module1,
                          state=DISABLED)
        self.txt1.grid(row=1,column=0, padx=2, pady=2)

        self.txt2 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module2,
                          state=DISABLED)
        self.txt2.grid(row=2,column=0, padx=2, pady=2)

        self.txt3 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module3,
                          state=DISABLED)
        self.txt3.grid(row=3,column=0, padx=2, pady=2)

        self.txt4 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module4,
                          state=DISABLED)
        self.txt4.grid(row=4,column=0, padx=2, pady=2)

        self.txt5 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module5,
                          state=DISABLED)
        self.txt5.grid(row=5,column=0, padx=2, pady=2)

        self.txt6 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module6,
                          state=DISABLED)
        self.txt6.grid(row=6,column=0, padx=2, pady=2)

        self.txt7 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module7,
                          state=DISABLED)
        self.txt7.grid(row=7,column=0, padx=2, pady=4)

        self.txt8 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module8,
                          state=DISABLED)
        self.txt8.grid(row=8,column=0, padx=2, pady=3)

        self.txt9 = Entry(UnitScore, font=('arial',12,'bold'), width=5, textvariable=self.Module9,
                          state=DISABLED)
        self.txt9.grid(row=9,column=0, padx=2, pady=3)

        

        #===================================TotalScore/Ranking/Date=================================================
        self.lblTotalScore = Label(ResultFrameLeft, font=('arial',13,'bold'), text='Total Score')                                               
        self.lblTotalScore.grid(row=0,column=0, sticky =W)
        self.txtTotalScore  = Entry(ResultFrameRight, font=('arial',13,'bold'),width=19,textvariable=self.TotalScore)
        self.txtTotalScore.grid(row=0,column=0)

        self.lblPercentage = Label(ResultFrameLeft, font=('arial',13,'bold'), text='Percentage')                                               
        self.lblPercentage.grid(row=1,column=0, sticky =W)
        self.txtPercentage  = Entry(ResultFrameRight, font=('arial',13,'bold'),width=19,textvariable=self.Percentage)
        self.txtPercentage.grid(row=1,column=0)
        
        self.lblRanking = Label(ResultFrameLeft, font=('arial',13,'bold'), text='Ranking')                                               
        self.lblRanking.grid(row=2,column=0, sticky =W)
        self.txtRanking  = Entry(ResultFrameRight, font=('arial',13,'bold'),width=19,textvariable=self.Ranking)
        self.txtRanking.grid(row=2,column=0)

        self.lblDateRanked = Label(ResultFrameLeft, font=('arial',13,'bold'), text='Date')                                               
        self.lblDateRanked .grid(row=3,column=0, sticky =W)
        self.txtDateRanked  = Entry(ResultFrameRight, font=('arial',13,'bold'),width=19,textvariable=self.ResultDate)
        self.txtDateRanked .grid(row=3,column=0)
        #=========================================SUBJECTS======================================================


        self.lblSelectedSubjects = Label(TopFrame12b, font=('arial',15,'bold'), text='Selected Subjects',
                                  bd=5,justify=CENTER)
        self.lblSelectedSubjects.grid(row=0,column=0)
        

        #datscience
        self.lblDataScience = Label(TopFrame12b, font=('arial',12,'bold'), text='Data Science',bd=7)                                               
        self.lblDataScience.grid(row=1,column=0, sticky =W)

        self.cboDataScience = ttk.Combobox(TopFrame12b, textvariable = self.DataScience, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboDataScience['values']= ('No','Core Unit','Yes','Complete')
        self.cboDataScience.current(0)
        self.cboDataScience.grid(row=1, column=1)
        
        #Eventdriven pro
        self.lblEventDrivenPro = Label(TopFrame12b, font=('arial',12,'bold'), text='Event Driven Prog',bd=7)                                               
        self.lblEventDrivenPro.grid(row=2,column=0, sticky =W)

        self.cboEventDrivenPro = ttk.Combobox(TopFrame12b, textvariable = self.EventDrivenPro, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboEventDrivenPro['values']= ('No','Core Unit','Yes','Complete')
        self.cboEventDrivenPro.current(0)
        self.cboEventDrivenPro.grid(row=2, column=1)
        #objectoriented
        self.lblObjectOriented = Label(TopFrame12b, font=('arial',12,'bold'), text='Object Oriented',bd=7,
                                       anchor='w',justify=LEFT)                                               
        self.lblObjectOriented .grid(row=3,column=0, sticky =W)

        self.cboObjectOriented  = ttk.Combobox(TopFrame12b, textvariable = self.ObjectOriented , width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboObjectOriented ['values']= ('No','Core Unit','Yes','Complete')
        self.cboObjectOriented .current(0)
        self.cboObjectOriented .grid(row=3, column=1)
        
        #spreadsheet
        self.lblSpreadsheet = Label(TopFrame12b, font=('arial',12,'bold'), text='Spreadsheet',bd=7)                                               
        self.lblSpreadsheet.grid(row=4,column=0, sticky =W)

        self.cboSpreadsheet = ttk.Combobox(TopFrame12b, textvariable = self.Spreadsheet, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboSpreadsheet['values']= ('No','Core Unit','Yes','Complete')
        self.cboSpreadsheet.current(0)
        self.cboSpreadsheet.grid(row=4, column=1)
        
        #SystemAnalysis
        self.lblSystemAnalysis = Label(TopFrame12b, font=('arial',12,'bold'), text='System Analysis',bd=7)
                                                                                     
        self.lblSystemAnalysis.grid(row=5,column=0, sticky =W)

        self.cboSystemAnalysis = ttk.Combobox(TopFrame12b, textvariable = self.SystemAnalysis, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboSystemAnalysis['values']= ('No','Core Unit','Yes','Complete')
        self.cboSystemAnalysis.current(0)
        self.cboSystemAnalysis.grid(row=5, column=1)

        #InformTechnology
        self.lblInformTechnology = Label(TopFrame12b, font=('arial',12,'bold'), text='Inform Technology',bd=7)
                                                                                        
        self.lblInformTechnology.grid(row=6,column=0, sticky =W)

        self.cboInformTechnology = ttk.Combobox(TopFrame12b, textvariable = self.InformTechnology, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboInformTechnology['values']= ('No','Core Unit','Yes','Complete')
        self.cboInformTechnology.current(0)
        self.cboInformTechnology.grid(row=6, column=1)

        #DigitalGraphics
        self.lblDigitalGraphics = Label(TopFrame12b, font=('arial',12,'bold'), text='Digital Graphics',bd=7)
                                                                                        
        self.lblDigitalGraphics .grid(row=7,column=0, sticky =W)

        self.cboDigitalGraphics  = ttk.Combobox(TopFrame12b, textvariable = self.DigitalGraphics, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboDigitalGraphics ['values']= ('No','Core Unit','Yes','Complete')
        self.cboDigitalGraphics .current(0)
        self.cboDigitalGraphics .grid(row=7, column=1)

        #English
        self.lblEnglish = Label(TopFrame12b, font=('arial',12,'bold'), text='English',bd=7)                                                                              
        self.lblEnglish.grid(row=8,column=0, sticky =W)

        self.cboEnglish = ttk.Combobox(TopFrame12b, textvariable = self.English, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboEnglish ['values']= ('No','Core Unit','Yes','Complete')
        self.cboEnglish.current(0)
        self.cboEnglish.grid(row=8, column=1)

        #Games
        self.lblGames = Label(TopFrame12b, font=('arial',12,'bold'), text='Games',bd=7)                                                                              
        self.lblGames.grid(row=9,column=0, sticky =W)

        self.cboGames = ttk.Combobox(TopFrame12b, textvariable = self.Games, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboGames ['values']= ('No','Core Unit','Yes','Complete')
        self.cboGames.current(0)
        self.cboGames.grid(row=9, column=1)

        #Animation
        self.lblAnimation = Label(TopFrame12b, font=('arial',12,'bold'), text='Animation',bd=7)                                                                              
        self.lblAnimation.grid(row=10,column=0, sticky =W)

        self.cboAnimation= ttk.Combobox(TopFrame12b, textvariable = self.Animation, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboAnimation['values']= ('No','Core Unit','Yes','Complete')
        self.cboAnimation.current(0)
        self.cboAnimation.grid(row=10, column=1)

        #Database
        self.lblDatabase1 = Label(TopFrame12b, font=('arial',12,'bold'), text='Database',bd=6)                                                                              
        self.lblDatabase1.grid(row=11,column=0, sticky =W)

        self.cboDatabase1= ttk.Combobox(TopFrame12b, textvariable = self.Database1, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboDatabase1['values']= ('No','Core Unit','Yes','Complete')
        self.cboDatabase1.current(0)
        self.cboDatabase1.grid(row=11, column=1)

        #maths
        self.lblMaths = Label(TopFrame12b, font=('arial',12,'bold'), text='Maths',bd=6)                                                                              
        self.lblMaths.grid(row=12,column=0, sticky =W)

        self.cboMaths= ttk.Combobox(TopFrame12b, textvariable = self.Maths, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboMaths['values']= ('No','Core Unit','Yes','Complete')
        self.cboMaths.current(0)
        self.cboMaths.grid(row=12, column=1)

        #AddMaths
        self.lblAddMaths = Label(TopFrame12b, font=('arial',12,'bold'), text='AddMaths',bd=6)                                                                              
        self.lblAddMaths.grid(row=13,column=0, sticky =W)

        self.cboAddMaths= ttk.Combobox(TopFrame12b, textvariable = self.AddMaths, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboAddMaths['values']= ('No','Core Unit','Yes','Complete')
        self.cboAddMaths.current(0)
        self.cboAddMaths.grid(row=13, column=1)

        #physics
        self.lblPhysics = Label(TopFrame12b, font=('arial',12,'bold'), text='Physics ',bd=6)                                                                              
        self.lblPhysics .grid(row=14,column=0, sticky =W)

        self.cboPhysics = ttk.Combobox(TopFrame12b, textvariable = self.Physics , width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboPhysics ['values']= ('No','Core Unit','Yes','Complete')
        self.cboPhysics .current(0)
        self.cboPhysics .grid(row=14, column=1)

        #Media
        self.lblMedia = Label(TopFrame12b, font=('arial',12,'bold'), text='Media',bd=6)                                                                              
        self.lblMedia.grid(row=15,column=0, sticky =W)

        self.cboMedia= ttk.Combobox(TopFrame12b, textvariable = self.Media, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboMedia['values']= ('No','Core Unit','Yes','Complete')
        self.cboMedia.current(0)
        self.cboMedia.grid(row=15, column=1)

        #Graphic Designing
        self.lblGraphicD = Label(TopFrame12b, font=('arial',12,'bold'), text='Graphic Designing',bd=6)                                                                              
        self.lblGraphicD.grid(row=16,column=0, sticky =W)

        self.cboGraphicD= ttk.Combobox(TopFrame12b, textvariable = self.GraphicD, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboGraphicD['values']= ('No','Core Unit','Yes','Complete')
        self.cboGraphicD.current(0)
        self.cboGraphicD.grid(row=16, column=1)

        #Artificial Intelligence
        self.lblArtiIntell = Label(TopFrame12b, font=('arial',12,'bold'), text='Artificial Intelligence',bd=6)                                                                              
        self.lblArtiIntell .grid(row=17,column=0, sticky =W)

        self.cboArtiIntell = ttk.Combobox(TopFrame12b, textvariable = self.ArtiIntell , width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboArtiIntell ['values']= ('No','Core Unit','Yes','Complete')
        self.cboArtiIntell .current(0)
        self.cboArtiIntell .grid(row=17, column=1)

        #Architecture
        self.lblArchitecture = Label(TopFrame12b, font=('arial',12,'bold'), text='Comp Architecture',bd=6)                                                                              
        self.lblArchitecture.grid(row=18,column=0, sticky =W)

        self.cboArchitecture= ttk.Combobox(TopFrame12b, textvariable = self.Architecture, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboArchitecture['values']= ('No','Core Unit','Yes','Complete')
        self.cboArchitecture.current(0)
        self.cboArchitecture.grid(row=18, column=1)

        #Machine Learning
        self.lblMachLearn = Label(TopFrame12b, font=('arial',12,'bold'), text='Machine Learning',bd=6)                                                                              
        self.lblMachLearn.grid(row=19,column=0, sticky =W)

        self.cboMachLearn= ttk.Combobox(TopFrame12b, textvariable = self.MachLearn, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboMachLearn['values']= ('No','Core Unit','Yes','Complete')
        self.cboMachLearn.current(0)
        self.cboMachLearn.grid(row=19, column=1)

        #social computing
        self.lblSocialComput = Label(TopFrame12b, font=('arial',12,'bold'), text='Social Computing',bd=6)                                                                              
        self.lblSocialComput.grid(row=20,column=0, sticky =W)

        self.cboSocialComput= ttk.Combobox(TopFrame12b, textvariable = self.SocialComput, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboSocialComput['values']= ('No','Core Unit','Yes','Complete')
        self.cboSocialComput.current(0)
        self.cboSocialComput.grid(row=20, column=1)

        #Information Security
        self.lblInformSecur = Label(TopFrame12b, font=('arial',12,'bold'), text='Information Security',bd=6)                                                                              
        self.lblInformSecur.grid(row=21,column=0, sticky =W)

        self.cboInformSecur = ttk.Combobox(TopFrame12b, textvariable = self.InformSecur, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboInformSecur ['values']= ('No','Core Unit','Yes','Complete')
        self.cboInformSecur .current(0)
        self.cboInformSecur .grid(row=21, column=1)

        #Networking and Communications
        self.lblNetComm = Label(TopFrame12b, font=('arial',12,'bold'), text='Network and Comm',bd=6)                                                                              
        self.lblNetComm .grid(row=22,column=0, sticky =W)

        self.cboNetComm = ttk.Combobox(TopFrame12b, textvariable = self.NetComm, width=30,
                                       font=('arial',12,'bold'), state = 'readonly')
        self.cboNetComm['values']= ('No','Core Unit','Yes','Complete')
        self.cboNetComm.current(0)
        self.cboNetComm .grid(row=22, column=1)


        #=====================================Table Treeview========================================================

        scroll_x = ttk.Scrollbar(TopFrame12a, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(TopFrame12a, orient=VERTICAL)

        self.Student_Record = ttk.Treeview(TopFrame12a, height=22, columns=("studentid","firstname","surname",
        "address","postcode","gender","dob","mobile","email","enrollmentno"),
        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_Record.xview)
        scroll_y.config(command=self.Student_Record.yview)
        

        self.Student_Record.heading("studentid", text="Student ID")
        self.Student_Record.heading("firstname", text="Firstname")
        self.Student_Record.heading("surname", text="Surname")
        self.Student_Record.heading("address", text="Address")
        self.Student_Record.heading("postcode", text="Post Code")
        self.Student_Record.heading("gender", text="Gender")
        self.Student_Record.heading("dob", text="DOB")
        self.Student_Record.heading("mobile", text="Mobile")
        self.Student_Record.heading("email", text="Email")
        self.Student_Record.heading("enrollmentno", text="Enrollment No")

        self.Student_Record['show']='headings'

        self.Student_Record.column("studentid",width=85)
        self.Student_Record.column("firstname", width=95)
        self.Student_Record.column("surname", width=95)
        self.Student_Record.column("address", width=205)
        self.Student_Record.column("postcode", width=85)
        self.Student_Record.column("gender",width=85)
        self.Student_Record.column("dob", width=85)
        self.Student_Record.column("mobile", width=85)
        self.Student_Record.column("email", width=95)
        self.Student_Record.column("enrollmentno", width=100)

        self.Student_Record.pack(fill=BOTH, expand = 1)
        self.Student_Record.bind("<ButtonRelease-1>",stuInfo)
        DisplayData()
        
        #====================================BUTTON FRAME======================================================
        try:
            
            self.btnAddNewStudent = Button(ButtonFrame, pady=1, padx=11, bd=4, font=('arial',16,'bold')
                                       ,bg="cadetblue",width=5, text="AddNew", command=addData).grid(row=0, column=0, padx=1)
        except Exception as err:
             tkinter.messagebox.showerror("Error",err)
                

        self.btnUpdate = Button(ButtonFrame, pady=1, padx=11, bd=4, font=('arial',16,'bold')
                                       ,bg="cadetblue",width=5, text="Update", command=update).grid(row=0, column=1, padx=1)

        self.btnDelete = Button(ButtonFrame, pady=1, padx=11, bd=4, font=('arial',16,'bold')
                                       ,bg="cadetblue",width=5, text="Delete", command=deletedb).grid(row=0, column=2, padx=1)

        self.btnReset = Button(ButtonFrame, pady=1, padx=11, bd=4, font=('arial',16,'bold')
                                       ,bg="cadetblue",width=5, text="Reset", command=Reset).grid(row=0, column=3, padx=1)
 

        self.btnSearch = Button(ButtonFrame, pady=1, padx=11, bd=4, font=('arial',16,'bold')
                                       ,bg="cadetblue",width=5, text="Search",command=searchDB).grid(row=0, column=4, padx=1)
        
        self.btnResult = Button(ButtonFrame, pady=1, padx=11, bd=4, font=('arial',16,'bold')
                                       ,bg="cadetblue",width=5, text="Result", command=getSelectedDate).grid(row=0, column=5, padx=1)


        self.btnExit = Button(ButtonFrame, pady=1, padx=11, bd=4, font=('arial',16,'bold')
                                       ,bg="cadetblue",width=5, text="Exit", command=iExit).grid(row=0, column=6, padx=1)
        
#======================================For DOB==========================================================
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry
from tkcalendar import*

#==============================================================================================================

if __name__ == '__main__':
    root = Tk()
    application = studentRecords(root)
    root.mainloop()
        
        




