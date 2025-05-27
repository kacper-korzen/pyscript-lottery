from pyscript import document as d
from js import alert


selectionDiv = d.querySelector(".selection-screen")
startDiv = d.querySelector(".start-screen")
resultDiv = d.querySelector(".result-screen")

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


drawBtn.onclick = onClickSelection


def showResult():
    draw_animation_div = d.querySelector("#draw-animation")
    draw_animation_div.innerHTML = ""

    for num in sorted(pickedNumbers):
        span = d.createElement("span")
        span.textContent = str(num)
        span.className = "badge rounded-pill bg-primary mx-1 fs-5"
        draw_animation_div.appendChild(span)
