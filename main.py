from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

basket = ["Оскар Шмидт", "Сергей Белов", "Джерри Уэст", "Коби Брайант", "Оскар Робертсон"]

@app.route("/")
def main():
    return render_template("index.html", people=basket)

@app.route("/str1")
def str_1():
    return render_template("str1.html")

@app.route("/str2")
def str_2():
    return render_template("str2.html")

@app.route("/str3")
def str_3():
    return render_template("str3.html")

@app.route("/str4")
def str_4():
    return render_template("str4.html")

@app.route("/str5")
def str_5():
    return render_template("str5.html")


app.run()