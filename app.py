from js import document

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
        <input type="text" id="num1" min="1" max="49">
        <input type="text" id="num2" min="1" max="49">
        <input type="text" id="num3" min="1" max="49">
        <input type="text" id="num4" min="1" max="49">
        <input type="text" id="num5" min="1" max="49">
        <input type="text" id="num6" min="1" max="49">
    </div>
    <button id="draw-btn" class="btn btn-success" disabled>Losuj</button>

</div>
"""

