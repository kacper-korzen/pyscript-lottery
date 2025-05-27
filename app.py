from pyscript import document as d
from js import alert, setTimeout

selectionDiv = d.querySelector(".selection-screen")
startDiv = d.querySelector("#start-button-container")  
resultDiv = d.querySelector(".result-screen")

playBtn = d.querySelector("#play-btn")
drawBtn = d.querySelector("#draw-btn")

pickedNumbers = set()

def show_start_button():
    loading = d.getElementById("loading-screen")
    start_btn_container = d.getElementById("start-button-container")
    loading.classList.add("d-none")
    start_btn_container.classList.remove("d-none")

# Symulacja czasu ładowania, np. 1 sekunda
setTimeout(show_start_button, 1000)

def onClickStart(e):
    startDiv.classList.add("d-none")
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
    inputs = d.querySelectorAll(".number-inputs input")
    for input in inputs:
        tmp = input.value.strip()
        if is_int(tmp):
            n = int(tmp)
            if 1 <= n <= 49:
                pickedNumbers.add(n)
            else:
                alert("Liczby muszą być z zakresu 1-49!")
                return
        else:
            alert("Sprawdź poprawność liczb!")
            return

    if len(pickedNumbers) != 6:
        alert("Wybierz 6 różnych liczb!")
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
