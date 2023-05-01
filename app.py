from flask import Flask,render_template,request
import myMath,myChecker


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def Calc():
    app.debug = True
    if request.method == 'POST':
      fNum = request.form.get('fNum')
      sNum = request.form.get('sNum')
      symbol = request.form.get('symbol')
      if myChecker.intCheck(fNum,sNum) and myChecker.symCheck(symbol):
        answer = myMath.checkSymbol(symbol,fNum,sNum)
        return render_template('index.html', answer=answer)
      else: return render_template('index.html', answer='Please Use real numbers and symbols')
    else: return render_template('index.html')
    
