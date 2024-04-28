from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QButtonGroup,QMessageBox,QRadioButton, QGroupBox
from random import shuffle,randint
app =QApplication([])

class QuestionClass():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

main_win = QWidget()
main_win.setWindowTitle('Memory Card')

lineH1= QHBoxLayout()
lineV1= QVBoxLayout()
lineV2= QVBoxLayout()

RadioGroupBox = QGroupBox('Варианты ответов')

b1 = QRadioButton('Вариант 1')
b2 = QRadioButton('Вариант 2')
b3 = QRadioButton('Вариант 3')
b4 = QRadioButton('Вариант 4')

lineV1.addWidget(b1,alignment= Qt.AlignCenter)
lineV1.addWidget(b2,alignment= Qt.AlignCenter)
lineV2.addWidget(b3,alignment= Qt.AlignCenter)
lineV2.addWidget(b4,alignment= Qt.AlignCenter)

lineH1.addLayout(lineV1)
lineH1.addLayout(lineV2)

RadioGroupBox.setLayout(lineH1)

mLine_H1 = QHBoxLayout()
mLine_H2 = QHBoxLayout()
mLine_H3 = QHBoxLayout()

question = QLabel('Чурки не люди!')
ansButton = QPushButton('Ответить')

mLine_H1.addWidget(question,alignment = Qt.AlignCenter)
mLine_H2.addWidget(RadioGroupBox)
mLine_H3.addWidget(ansButton)

#RadioGroupBox.hide()

AnsBox = QGroupBox('Результат:')
YesNoLabel = QLabel('тут будет верно/неверно')
CorrectAns = QLabel('Тут верный ответ')

lineVAnsBox = QVBoxLayout()
lineVAnsBox.addWidget(YesNoLabel)
lineVAnsBox.addWidget(CorrectAns)
AnsBox.setLayout(lineVAnsBox)

mLine_H2.addWidget(AnsBox)
AnsBox.hide()

mLineV = QVBoxLayout()

mLineV.addLayout(mLine_H1)
mLineV.addLayout(mLine_H2)
mLineV.addLayout(mLine_H3)

main_win.setLayout(mLineV)

RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

AnsBox.hide()


def show_results():
    RadioGroupBox.hide()
    AnsBox.show()
    ansButton.setText('Следующий вопрос')

def show_question():
    AnsBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)
    ansButton.setText('Ответить')

# def TEST():
#     if ansButton.text() == 'Ответить':
#         show_results()
#     else:
#         show_question()

answers = [b1,b2,b3,b4]

def ask(q: QuestionClass):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    CorrectAns.setText(q.right_answer)
    show_question()

def show_correct(result):
    YesNoLabel.setText(result)
    show_results()

def check():
    if answers[0].isChecked():
        show_correct('Верно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно!')
    print('Рейтинг:',main_win.score/main_win.total*100,'%')

question_list = []

question_list.append(QuestionClass('Какой ты скибиди туалет?','семён','чурка','нигерс','aaaaa'))
question_list.append(QuestionClass('в каком году был крестовый поход?','хз','я не знаю','я гомосек','я не душнила'))
question_list.append(QuestionClass('в каком году наполеон напал на русь матушку?','1812','1806','хз','2023'))
question_list.append(QuestionClass('Когда я родился?','17 февраля','24 ноября','17 апреля','30 августа'))
question_list.append(QuestionClass('Каким спортам занимаются нормальные парни?','Хобихорсингом','Волейболом','Футболом','киберспорт'))
question_list.append(QuestionClass('рассизм это круто?','нет,осуждаю','да','нейтрально','я гей'))
question_list.append(QuestionClass('Дота для дырявых?','конечно,на своём опыте узнал','да','нет','1000 -7'))
question_list.append(QuestionClass('ревием это?','скил сфа','песня такая','ультимэйт пуджа','мой отец'))
question_list.append(QuestionClass('я выйграл отца в танки, как он на это отреагирует ?','Я твою мать е**л','молодец','горжусь тобой,мой чемпион','я в тильд'))
question_list.append(QuestionClass('когда я александр я настоящий...?','андер','педик','ангел','мой батя'))

main_win.total = 0
main_win.score = 0

def next_question():
    main_win.total += 1
    print('Статистика:',main_win.total,'-Всего вопросов верно:',main_win.score)


    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if 'Ответить' == ansButton.text():
        check()
    else:
        next_question()



ansButton.clicked.connect(click_OK)

next_question()
main_win.show()
app.exec_()