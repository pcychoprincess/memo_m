from PyQt5.QtCore import Qt#функциональный модуль
from PyQt5.QtWidgets import*#За окно
from memo_card import*
from memo import*
from random import shuffle # перемішуватимемо відповіді у картці питання


window_=QWidget()
w,h=600,500
window_.resize(w,h)
window_.setWindowTitle("MemoryCard")
x,y=50,50
window_.move(x,y)



frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'





radio_list = [answer1, answer2, answer3, answer4]
shuffle(radio_list)






radio_list[0].setText(frm_right)
radio_list[1].setText(frm_wrong1)
radio_list[2].setText(frm_wrong2)
radio_list[3].setText(frm_wrong3)

question.setText(frm_question)




qustio=[]

def start():
    frm_question =
    
def check_result():
    correct = radio_list[0].isChecked() # у цьому радіобаттоні лежить наша відповідь!
    if correct:
        right_wrong.setText("Правильно")
        show_result()
    else:
        right_wrong.setText("Неправильно")
        show_result()
def click_answer():
   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
   if answer.text() == 'Відповісти':
       check_result()
def create_q():#добавляем вопрос в список для отображения потом на экране
    frm_right=v_correct_e.text()
    frm_question=v_quastion_e.text()
    frm_wrong1=v_wrote1_e.text()
    frm_wrong2=v_wrote2_e.text()    
    frm_wrong3=v_wrote3_e.text() 
    qu=Question(frm_right,frm_question,frm_wrong1,frm_wrong2,frm_wrong3)
    quastio.append(qu)

window_.setLayout(layoutmain_v)


answer.clicked.connect(click_answer)
d_quastion.clicked.connect(create_q)

window_.hide()
window.show()
app.exec_()

