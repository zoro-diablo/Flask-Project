from flask import Flask, request, render_template
api=Flask(__name__)

@api.route('/')
def home():
    return render_template('input.html')

@api.route('/add', methods=['GET','POST'])
def addition():
    num1=request.form['num1'] #100
    num2=request.form['num2'] #200

    if num1.isdigit() and num2.isdigit():
        a=int(num1)
        b=int(num2)
        res=a+b #300

        return render_template("result.html",result=res)
    else:
        res="Only digits are allowed"
        return render_template("result.html",result=res)

if __name__== '__main__':
    api.run(debug=True,host='0.0.0.0',port=5000)