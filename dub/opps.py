class Student:
    def __init__(self,name,maths,english,science):
        self.name=name
        self.maths=maths
        self.english=english
        self.science=science
    
    def marks_report(self):
        print("Marks obtained in Maths:",self.maths)
        print("english obtained in Maths:",self.english)
        print("Science obtained in Maths:",self.science)
        print("--------------------------")
        print("average marks Obtained:",(self.maths+self.english+self.science)//3)

s1=Student("Nikhil",60,30,77)
s1.marks_report()
