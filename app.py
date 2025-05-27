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
    startDiv.classList.remove("d-flex")
    startDiv.classList.add("d-none")
    selectionDiv.classList.remove("d-none")
    selectionDiv.classList.add("d-flex,flex-column")


playBtn.onclick = onClickStart
