from pyscript import document as d
from js import alert, setTimeout
from random import randint
from pyodide.ffi import create_once_callable

selectionDiv = d.querySelector(".selection-screen")
resultDiv = d.querySelector(".result-screen")
drawAnimationDiv = d.querySelector("#draw-animation")
drawResultDiv = d.querySelector("#draw-result")
winMesDiv = d.querySelector("#win-message")
drawBtnsDiv = d.querySelector("#draw-buttons")

playBtn = d.querySelector("#play-btn")
drawBtn = d.querySelector("#draw-btn")
newNumbersBtn = d.querySelector("#btn-new-numbers")
redrawBtn = d.querySelector("#btn-redraw")

pickedNumbers = set()
randomNumbers = set()
win = False

def is_int(value):
    try:
        int(value, 10)
        return True
    except ValueError:
        return False


def onClickSelection(e):
    pickedNumbers.clear()
    for input_element in d.querySelectorAll("input"):
        tmp = input_element.value.strip()
        if is_int(tmp):
            num = int(tmp)
            if 1 <= num <= 49:
                pickedNumbers.add(num)
            else:
                alert("Liczby muszą być w zakresie 1-49!")
                return
        else:
            alert("Sprawdź poprawność liczb!")
            return

    if len(pickedNumbers) != 6:
        alert("Wybierz dokładnie 6 różnych liczb!")
        return

    selectionDiv.classList.remove("d-flex", "flex-column")
    selectionDiv.classList.add("d-none")
    resultDiv.classList.remove("d-none")
    showResult()
    showDrawing()


drawBtn.onclick = onClickSelection


def showResult():
    pickedNumbersDiv = d.querySelector("#picked-numbers")
    pickedNumbersDiv.innerHTML = ""

    for num in sorted(pickedNumbers):
        span = d.createElement("span")
        span.textContent = str(num)
        span.className = "badge rounded-pill bg-primary mx-1 fs-5"
        pickedNumbersDiv.appendChild(span)


def showDrawing():
    drawDiv = d.querySelector("#draw-animation")
    drawDiv.innerHTML = ""

    global randomNumbers
    randomNumbers = set()
    while len(randomNumbers) < 6:
        randomNumbers.add(randint(1, 49))

    final_numbers = sorted(randomNumbers)

    spans = []
    for _ in range(6):
        span = d.createElement("span")
        span.className = "badge rounded-pill bg-primary mx-1 fs-5"
        drawDiv.appendChild(span)
        spans.append(span)

    def animate_number(index):
        if index >= len(spans):
            return

        span = spans[index]
        count = 0

        def show_random():
            nonlocal count
            if count < 3:
                rand_num = randint(1, 49)
                span.textContent = str(rand_num)
                count += 1
                showRandom = create_once_callable(show_random)
                setTimeout(showRandom, 300)
            else:
                span.textContent = str(final_numbers[index])
                showDrawingProxy = create_once_callable(
                    lambda: animate_number(index + 1)
                )
                setTimeout(showDrawingProxy, 300)

        show_random()

    animate_number(0)

    checkWin()
    winResult = create_once_callable(showIfWin)
    setTimeout(winResult, 7500)


def checkWin():
    global win
    count = 0

    for num in pickedNumbers:
        if num in randomNumbers:
            count += 1

    if count > 3:
        win = True


def showIfWin():
    if win is True:
        winMesDiv.classList.remove("d-none")
    else:
        drawResultDiv.classList.remove("d-none")

    drawBtnsDiv.classList.remove("d-none")


def onClickNewNumbers(e):
    resultDiv.classList.add('d-none')
    selectionDiv.classList.remove('d-none')
    drawBtnsDiv.classList.add("d-none")
    drawResultDiv.classList.add("d-none")

redrawBtn.onclick = onClickNewNumbers