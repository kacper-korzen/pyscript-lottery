from pyscript import document as d
from js import alert, setTimeout
from random import randint
from pyodide.ffi import create_proxy
from time import sleep

selectionDiv = d.querySelector(".selection-screen")
startDiv = d.querySelector(".start-screen")
resultDiv = d.querySelector(".result-screen")
drawAnimationDiv = d.querySelector("#draw-animation")

playBtn = d.querySelector("#play-btn")
drawBtn = d.querySelector("#draw-btn")

pickedNumbers = set()


def onClickStart(e):
    startDiv.classList.add("d-none")
    startDiv.classList.remove("d-flex")
    selectionDiv.classList.remove("d-none")
    selectionDiv.classList.add("d-flex", "flex-column")


playBtn.onclick = onClickStart


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
    # showDrawingProxy = create_proxy(showDrawing)
    # setTimeout(showDrawingProxy, 1000)


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
                showRandom = create_proxy(show_random)
                setTimeout(showRandom, 300)
            else:
                span.textContent = str(final_numbers[index])
                showDrawingProxy = create_proxy(lambda: animate_number(index + 1))
                setTimeout(showDrawingProxy, 300)

        show_random()

    animate_number(0)
