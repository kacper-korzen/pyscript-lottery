from pyscript import document as d


class StartScreen:
    pass


class NumberSelectionScreen:
    pass


class ResultScreen:
    pass


playBtn = d.querySelector("#play-btn")
selectionDiv = d.querySelector(".selection-screen")
startDiv = d.querySelector(".start-screen")


def onClickStart(e):
    selectionDiv.style.display = "block"
    startDiv.classList.remove("d-flex")
    startDiv.classList.add("d-none");


playBtn.onclick = onClickStart
