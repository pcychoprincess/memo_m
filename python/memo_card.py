from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app=QApplication([])
menu=QPushButton("Меню")
answer=QPushButton("Відповісти")
time_relax=QPushButton("Відпочити")
time=QLabel("хвилин")
minuts=QSpinBox()
minuts.setValue(30)
answer_options=QGroupBox("Варіанти відповідей")

result=QGroupBox("Результат")
right_wrong = QLabel("не знаю ще")#правильно/неправильно
correct = QLabel("apple")#правильний варіант

layout_v = QVBoxLayout()
layout_v.addWidget(right_wrong , alignment = (Qt.AlignLeft| Qt.AlignTop) )
layout_v.addWidget(correct , alignment = Qt.AlignCenter )


radiogoup=QButtonGroup()
question=QLabel()


layout1_h=QHBoxLayout()
layout2_h=QHBoxLayout()
layout3_h=QHBoxLayout()
layout4_h=QHBoxLayout()
layoutdop_h = QHBoxLayout()

layout1_v=QVBoxLayout()
layout2_v=QVBoxLayout()
layoutmain_v=QVBoxLayout()

answer1=QRadioButton("")
answer2=QRadioButton("")
answer3=QRadioButton("")
answer4=QRadioButton("")


radiogoup.addButton(answer1)
radiogoup.addButton(answer2)
radiogoup.addButton(answer3)
radiogoup.addButton(answer4)

layout1_v.addWidget(answer1)
layout1_v.addWidget(answer2)
layout2_v.addWidget(answer3)
layout2_v.addWidget(answer4)

layoutdop_h.addLayout(layout1_v)
layoutdop_h.addLayout(layout2_v)

answer_options.setLayout(layoutdop_h)
result.setLayout(layout_v)

layout1_h.addWidget(menu)
layout1_h.addStretch()
layout1_h.addWidget(time_relax)
layout1_h.addWidget(minuts)
layout1_h.addWidget(time)

layout2_h.addWidget(question)

layout3_h.addWidget(answer_options)
layout3_h.addWidget(result)
result.hide()

layout4_h.addWidget(answer)





layoutmain_v.addLayout(layout1_h, stretch=1)
layoutmain_v.addLayout(layout2_h, stretch=2)
layoutmain_v.addLayout(layout3_h, stretch=8)
layoutmain_v.addLayout(layout4_h)

def show_result():
    answer_options.hide()
    answer.setText("Наступне питання")
    result.show()
def show_question():
    answer_options.show()
    result.hide()
    answer.setText("Відповісти")
    radiogoup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    radiogoup.setExclusive(True)


    
