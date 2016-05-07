__author__ = 'khalid'
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot
from nltk.corpus import brown

adjectives = {word for word, pos in brown.tagged_words() if pos.startswith("JJ")}       # ADJ
adverbs = {word for word, pos in brown.tagged_words() if pos.startswith("RB")}          # ADV
conjunction = {word for word, pos in brown.tagged_words() if pos.startswith("CC")}      # CNJ
determiner = {word for word, pos in brown.tagged_words() if pos.startswith("DT")}       # DT
modalVerbs = {word for word, pos in brown.tagged_words() if pos.startswith("MD")}       # MD
nouns = {word for word, pos in brown.tagged_words() if pos.startswith("NN")}            # NN
properNouns = {word for word, pos in brown.tagged_words() if pos.startswith("NNP")}     # NNP
pronouns = {word for word, pos in brown.tagged_words() if pos.startswith("PRP")}        # PRP
prepositions = {word for word, pos in brown.tagged_words() if pos.startswith("IN")}     # IN
interjections = {word for word, pos in brown.tagged_words() if pos.startswith("NNS")}   # NNS
verbs = {word for word, pos in brown.tagged_words() if pos.startswith("VB")}            # VB
pastVerbs = {word for word, pos in brown.tagged_words() if pos.startswith("VBD")}       # VBD
presentVerbs = {word for word, pos in brown.tagged_words() if pos.startswith("VBG")}    # VBG
whDeterminer = {word for word, pos in brown.tagged_words() if pos.startswith("WP")}     # WP
resultList = []
######## Start post tagging function ######
def post_tag(commingWords):
    for i in commingWords:
        if i in adjectives:
            resultList.append(i + ': ADJ')
        if i in adverbs:
            resultList.append(i + ': ADV')
        if i in conjunction:
            resultList.append(i + ': CNJ')
        if i in determiner:
            resultList.append(i + ': DT')
        if i in modalVerbs:
            resultList.append(i + ': MD')
        if i in nouns:
            resultList.append(i + ': NN')
        if i in properNouns:
            resultList.append(i + ': NNP')
        if i in pronouns:
            resultList.append(i + ': PRP')
        if i in prepositions:
            resultList.append(i + ': IN')
        if i in interjections:
            resultList.append(i + ': NNS')
        if i in verbs:
            resultList.append(i + ': VB')
        if i in pastVerbs:
            resultList.append(i + ': VBD')
        if i in presentVerbs:
            resultList.append(i + ': VBG')
        if i in whDeterminer:
            resultList.append(i + ': WP')
        if i.isdigit():
            resultList.append(i + ' DGT')
######## End post tagging function ######
@pyqtSlot()
def on_click():
    post_tag(str(textBox.text()).lower().split())
    print(resultList)
    result.setText(', '.join(resultList))
    resultList[:] = []
######## Start GUI ######
app = QApplication(sys.argv)
w = QWidget()
btn = QPushButton("Pos Tag", w)
label1 = QLabel(w)
result = QLabel(w)
#Window handling
w.resize(400, 200)
w.setWindowTitle("Pos Tagging")
#steam button handling
btn.setToolTip("Pos Tag")
btn.resize(btn.sizeHint())
btn.move(110, 100)
#input textBox handling
textBox = QLineEdit(w)
textBox.move(60, 50)
textBox.resize(250, 40)
#Enteryour word label
label1.setText("Enter your sentence")
label1.move(100, 25)
result.move(0, 140)
result.resize(400, 20)
btn.clicked.connect(on_click)
w.show()
sys.exit(app.exec_())
######## End GUI ######
