from flask import Flask, render_template
from HW11_Diksha_Pancholi import new_instructor_summary

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html",
                            heading="Hello Professor Rowland",
                            para_body="Thank you for your help! I loved this coursse!!"

                        )

@app.route('/Bye Bye')
def see_ya():
    return "See you in next lecture!"

@app.route('/instructor_course')
def template_demo():
    
    data = new_instructor_summary()
    return render_template("Instructor_Summary.html",
                            header1="Stevens Repository",
                            header2="Courses and student counts",
                            data=data)

app.run(debug=True)