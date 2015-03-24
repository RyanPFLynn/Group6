from tkinter import *
from Home import *
from honeyMumford import *
from CalResults import *
from displayStyle import *
from VARKQ import *
from storage import *

class Controller(Frame):

	learningTypeStoreage = []
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.root = master

		self.cont_frame = Frame(self.root)
		self.cont_frame.pack(side=TOP)
		self.root.geometry("800x500")

		homepage = Home(self.cont_frame)
		homepage.pack()

		self.btnHome = Button(self.cont_frame, text="Submit", command= lambda: self.gettingHomeData(homepage))
		self.btnHome.pack(side=BOTTOM)

	def gettingHomeData(self, currentframe):
		try:
			(self.studentNumber,self.yearOfStudy,self.degreeProgram) = currentframe.get_information()
			currentframe.destroy()

			honeyMumfordQuestionnaire = honeyMumford(self.cont_frame)
			self.root.geometry("800x300")
			honeyMumfordQuestionnaire.pack()

			self.number = 2
			self.btnHome["text"] = "Next" 
			self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, honeyMumfordQuestionnaire,"Honey & Mumford",1)
		except TypeError:
			pass
			
	def changeCurrentQuestion(self,number, selectedFrame, questionnaireType, numberCompleted):
		if number in range(1,8):
			if number == 2:
				selectedFrame.changeQuestion(2)
				self.number +=1
			elif number == 3:
				selectedFrame.changeQuestion(3)
				self.number +=1
			elif number == 4:
				selectedFrame.changeQuestion(4)
				self.number +=1
			elif number == 5:
				selectedFrame.changeQuestion(5)
				self.number +=1
			elif number == 6:
				selectedFrame.changeQuestion(6)
				self.number +=1

				self.honeyResults = selectedFrame.getResults()
				self.update()
				selectedFrame.destroy()
				
				self.questionnaireResults = CalResults(self.honeyResults, questionnaireType)
				self.gettingInformation(self.questionnaireResults, questionnaireType,numberCompleted)

	def gettingInformation(self,curretnFrame, questionnaireType, completedQuestionnaire):
		self.learningType = curretnFrame.getType()
		Controller.learningTypeStoreage.append(self.learningType)
		self.results = displayStyle(self.cont_frame, self.learningType, questionnaireType)
		self.results.pack()

		if completedQuestionnaire == 1:
			self.btnHome["text"] = "VARK Questionnaire"
			self.btnHome["command"] = lambda: self.nextQuestionnaire()
		else:
			self.btnHome["text"] = "Exit"
			self.btnHome["command"] = lambda: self.sendHome()
			storingInfo = storage()
			storingInfo.add_data(self.studentNumber,self.degreeProgram, self.yearOfStudy, Controller.learningTypeStoreage[0], Controller.learningTypeStoreage[1])
		self.update()

	def nextQuestionnaire(self):
		self.results.destroy()
		self.btnHome["text"] = "Next"
		self.number = 2
		self.btnHome["command"] = lambda: self.changeCurrentQuestion(self.number, varkQues,"VARK",2)
		varkQues = VARKQ(self.cont_frame)
		varkQues.pack()

	def sendHome(self):
		self.results.destroy()
		self.quit()
		self.update()
		
def main():
	root = Tk()
	root.title("Questionnaire")
	app = Controller(root)
	root.mainloop()

if __name__ == "__main__":
	main()