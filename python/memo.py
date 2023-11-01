from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

class Question():
    def __init__(self, r_answer,question, w_answer1,w_answer2,w_answer3):
        self.r_answer=r_answer
        self.question=question
        self.w_answer1=w_answer1
        self.w_answer2=w_answer2
        self.w_answer3=w_answer3
        self.attems=0
        self.correct=0
    def got_right(self):
        print("Правильна відповідь")
    def got_wrong(self):
        print("Неправильна відповідь")
        
app=QApplication([])
window=QWidget()
window.setWindowTitle("Memo")
window.resize(500,450)

v_quastion=QLabel("Введіть запитання:")
v_quastion_e=QLineEdit()

v_correct=QLabel("Введіть вірну відповідь:")
v_correct_e=QLineEdit()

v_wrote1=QLabel("Введіть першу хибну відповідь:")
v_wrote1_e=QLineEdit()

v_wrote2=QLabel("Введіть другу хибну відповідь:")
v_wrote2_e=QLineEdit()

v_wrote3=QLabel("Введіть третю хибну відповідь:")
v_wrote3_e=QLineEdit()

d_quastion=QPushButton("Додати запитання")
clear=QPushButton("Очистити")

statistic=QLabel("Статистика")

begin=QPushButton("Начать")

layot1_v=QVBoxLayout()
layot1_v.addWidget(v_quastion)
layot1_v.addWidget(v_correct)
layot1_v.addWidget(v_wrote1)
layot1_v.addWidget(v_wrote2)
layot1_v.addWidget(v_wrote3)
layot1_v.addWidget(d_quastion)
    
layot2_v=QVBoxLayout()
layot2_v.addWidget(v_quastion_e)
layot2_v.addWidget(v_correct_e)
layot2_v.addWidget(v_wrote1_e)
layot2_v.addWidget(v_wrote2_e)
layot2_v.addWidget(v_wrote3_e)
layot2_v.addWidget(clear)

layot1_h=QHBoxLayout()
layot1_h.addLayout(layot1_v)
layot1_h.addLayout(layot2_v)

layot2_h=QHBoxLayout()
layot2_h.addWidget(begin, alignment = Qt.AlignBottom)

layot_v=QVBoxLayout()
layot_v.addLayout(layot1_h)
layot_v.addLayout(layot2_h)


window.setLayout(layot_v)


window.show()
app.exec_()

