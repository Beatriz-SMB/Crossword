from graphics import *
# import re

def main():
    win = GraphWin("Palavra Cruzada",1000,800)
    win.setBackground("tan1")

    startMessage = Text(Point(500,230), "Bem Vindo(a)! \n Pressione ENTER para começar o jogo")
    startMessage.setFace("arial")
    startMessage.setFill("white")
    startMessage.setSize(18)
    startMessage.draw(win)
    
    rectangle1 = Rectangle(Point(440,300),Point(560,360))
    rectangle1.setFill("black")
    rectangle1.draw(win)
    rectangle2 = Rectangle(Point(470,360),Point(560,430))
    rectangle2.setFill("black")
    rectangle2.draw(win)
    enter = Text(Point(500,330), "Enter ↲")
    enter.setFace("arial")
    enter.setFill("white")
    enter.setSize(14)
    enter.draw(win)

    keyString = win.checkKey()
    
    while keyString != "Escape":

        keyString = win.checkKey()    

        if (keyString == "Return"):
            startMessage.undraw()
            rectangle1.undraw()
            rectangle2.undraw()
            enter.undraw()
            win.setBackground("white")
            crossword(win)

            points = 0
            
            label = Text(Point(340,150), "Resposta:")
            label.setFace("arial")
            label.draw(win)

            inputField = Entry(Point(500,150),25)
            inputField.draw(win)
            
            button(win)

            while True:
                sentence = Text(Point(500,100), sentences(points))
                sentence.setFace("arial")
                sentence.draw(win)

                win.getMouse()
                
                text = str(inputField.getText()).upper()

                inputField.setText("")

                if (text == "JAVASCRIPT"):
                    sentence.undraw()
                    javascript(win)
                    points += 1
                elif (text == "NETBEANS") and (points == 1):
                    sentence.undraw()
                    netbeans(win)
                    points += 1
                elif (text == "CSS") and (points == 2):
                    sentence.undraw()
                    css(win)
                    points += 1
                elif (text == "RUBY") and (points == 3):
                    sentence.undraw()
                    ruby(win)
                    points += 1
                elif (text == "PYTHON") and (points == 4):
                    sentence.undraw()
                    python(win)
                    points += 1
                elif (text == "HTML") and (points == 5):
                    sentence.undraw()
                    html(win)
                    points += 1
                elif (text == "MENDIX") and (points == 6):
                    sentence.undraw()
                    mendix(win)
                    points += 1
                elif (text == "VISUAL BASIC") and (points == 7):
                    sentence.undraw()
                    visualBasic(win)
                    points += 1
                else:
                    sentence.undraw()
                    points += 0
                        
def sentences(hits):

    if (hits == 0):
        return "1. Juntamente com HTML e CSS, o _____________ é uma das três principais tecnologias da World Wide Web."
    elif (hits == 1):
        return "2. O _____________ IDE permite o desenvolvimento rápido e fácil de aplicações desktop Java."
    elif (hits == 2):
        return "3. _____________ é um mecanismo para adicionar estilo (cores, fontes, espaçamento, etc.) a um documento web."
    elif (hits == 3):
        return "4. A linguagem _____________ foi concebida em 24 de fevereiro de 1993 por Yukihiro Matsumoto."
    elif (hits == 4):
        return "5. _____________ foi feita com base na linguagem ABC, possui parte da sintaxe derivada do C, compreensão de\n listas, funções anonimas e função map de Haskell."
    elif (hits == 5):
        return '6. O _____________ usa "Marcação" para anotar texto, imagem e outros conteúdos para exibição em um navegador da Web.'
    elif (hits == 6):
        return "7. _____________ é uma empresa americana de plataforma de software de baixo código que fornece ferramentas para\n construir, testar, implantar e iterar aplicativos."
    elif (hits == 7):
        return "8. A partir de 2002 a linguagem _____________ mudou em vários aspectos ganhando muitos recursos, porém continuou\n com a mesma sintaxe."
    else:
        return "Parabéns!! Você concluiu o jogo 🎉🎉"
  
def crossword(window):

    one = Text(Point(305,405), "1.")
    one.setFace("arial")
    one.draw(window)

    for i in range(0,300,30):
        javascript = Rectangle(Point(320+i,390),Point(350+i,420))
        javascript.draw(window)

    two = Text(Point(425,225), "2.")
    two.setFace("arial")
    two.draw(window)

    for i in range(0,240,30):
        netbeans = Rectangle(Point(410,240+i),Point(440,270+i))
        netbeans.draw(window)

    three = Text(Point(335,465), "3.")
    three.setFace("arial")
    three.draw(window)

    for i in range(0,60,30):
        css = Rectangle(Point(350+i,450),Point(380+i,480))
        css.draw(window)

    four = Text(Point(515,375), "4.")
    four.setFace("arial")
    four.draw(window)

    for i in range(0,90,30):
        ruby = Rectangle(Point(500,420+i),Point(530,450+i))
        ruby.draw(window)

    five = Text(Point(575,375), "5.")
    five.setFace("arial")
    five.draw(window)

    for i in range(0,150,30):
        python = Rectangle(Point(560,420+i),Point(590,450+i))
        python.draw(window)

    six = Text(Point(545,495), "6.")
    six.setFace("arial")
    six.draw(window)

    for i in range(0,90,30):
        html = Rectangle(Point(590+i,480),Point(620+i,510))
        html.draw(window)

    seven = Text(Point(635,467), "7.")
    seven.setFace("arial")
    seven.draw(window)

    for i in range(0,150,30):
        mendix = Rectangle(Point(620,510+i),Point(650,540+i))
        mendix.draw(window)

    eight = Text(Point(305,615), "8.")
    eight.setFace("arial")
    eight.draw(window)

    for i in range(0,360,30):
        visualbasic = Rectangle(Point(320+i,600),Point(350+i,630))
        visualbasic.draw(window)
            
def button(window):
    rectangle1 = Rectangle(Point(625,135),Point(695,165))
    rectangle1.setFill("black")
    rectangle1.draw(window)

    caption = Text(Point(660,150), "Enviar")
    caption.setFill("white")
    caption.setFace("arial")
    caption.draw(window)
 

def javascript(window):
    space = 0
    firstAnswer = ['J','A','V','A','S','C','R','I','P','T']

    while space != 300:
        for e in firstAnswer:
            s = Text(Point(335+space,405), e)
            s.draw(window)
            space += 30

def netbeans(window):
    space = 0
    secondAnswer = ['N','E','T','B','E','A','N','S']

    while space != 240:
        for e in secondAnswer:
            s = Text(Point(425,255+space), e)
            s.draw(window)
            space += 30

def css(window):
    space = 0
    thirdAnswer = ['C','S','S']

    while space != 90:
        for e in thirdAnswer:
            s = Text(Point(365+space,465), e)
            s.draw(window)
            space += 30

def ruby(window):
    space = 0
    fourthAnswer = ['R','U','B','Y']

    while space != 120:
        for e in fourthAnswer:
            s = Text(Point(515,405+space), e)
            s.draw(window)
            space += 30
    
def python(window):
    space = 0
    fifthAnswer = ['P','Y','T','H','O','N']

    while space != 180:
        for e in fifthAnswer:
            s = Text(Point(575,405+space), e)
            s.draw(window)
            space += 30
    
def html(window):
    space = 0
    sixthAnswer = ['H','T','M','L']

    while space != 120:
        for e in sixthAnswer:
            s = Text(Point(575+space,495), e)
            s.draw(window)
            space += 30
    
def mendix(window):
    space = 0
    seventhAnswer = ['M','E','N','D','I','X']   

    while space != 180:
        for e in seventhAnswer:
            s = Text(Point(635,495+space), e)
            s.draw(window)
            space += 30
    
def visualBasic(window):
    space = 0
    eighthAnswer = ['V','I','S','U','A','L','-','B','A','S','I','C']

    while space != 360:
        for e in eighthAnswer:
            s = Text(Point(335+space,615), e)
            s.draw(window)
            space += 30

if __name__=="__main__":
    main()


