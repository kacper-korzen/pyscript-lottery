from pyscript import document as d
from js import alert


class StartScreen:
    pass


class NumberSelectionScreen:
    pass


class ResultScreen:
    pass


selectionDiv = d.querySelector(".selection-screen")
startDiv = d.querySelector(".start-screen")
resultDiv = d.querySelector(".result-screen")

playBtn = d.querySelector("#play-btn")
drawBtn = d.querySelector("#draw-btn")

pickedNumbers = set()


def onClickStart(e):
    startDiv.classList.remove("d-flex")
    startDiv.classList.add("d-none")
    selectionDiv.classList.remove("d-none")
    selectionDiv.classList.add("d-flex,flex-column")


playBtn.onclick = onClickStart


def is_int(value):
    try:
        int(value, 10)
        return True
    except ValueError:
        return False


def onClickSelection(e):
    for input in d.querySelectorAll("input"):
        tmp = input.value
        if is_int(tmp):
            pickedNumbers.add(int(tmp))
        else:
            alert("Sprawdź poprawność liczb!")
            pickedNumbers.clear()

    selectionDiv.classList.remove("d-flex,flex-column")
    selectionDiv.classList.add("d-none")
    resultDiv.remove("d-none")


drawBtn.onclick = onClickSelection


