from pyscript import document

class StartScreen():
    pass

class NumberSelectionScreen():
    pass

class ResultScreen():
    pass



result_html = """
<div class="result-screen">
    <h2>Twoje liczby</h2>
    <div id="draw-animation">

    </div>
    <div id="win-message" style="display:none">Wygrałeś!</div>
</div>
"""

selection_html = """
<div class="selection-screen">
    <h2>Wybierz 6 swoich szczęścliwych liczb(1-49):</h2>
    <div class="number-inputs">
        <input type="number" id="num1" min="1" max="49" value="1">
        <input type="number" id="num2" min="1" max="49" value="1">
        <input type="number" id="num3" min="1" max="49" value="1">
        <input type="number" id="num4" min="1" max="49" value="1">
        <input type="number" id="num5" min="1" max="49" value="1">
        <input type="number" id="num6" min="1" max="49" value="1">
    </div>
    <button id="draw-btn" class="btn btn-success" disabled>Losuj</button>

</div>
"""

app_div = document.querySelector("#app")

def changeingScreens():
    while True:
        play_btn = document.querySelector("#play-btn") 
        if play_btn:
            play_btn.onclick = lambda e: setattr(app_div, 'innerHTML', selection_html)


        draw_btn = document.querySelector("#draw-btn")
        if draw_btn:
            draw_btn.onclick = lambda e: setattr(app_div, 'innerHTML', result_html)

