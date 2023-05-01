from flask import Flask,render_template,request
import myMath


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def Calc():
    app.debug = True
    if request.method == 'POST':
      fNum = request.form.get('fNum')
      sNum = request.form.get('sNum')
      symbol = request.form.get('symbol')
      answer = myMath.checkSymbol(symbol,fNum,sNum)
      return render_template('index.html', answer=answer)
    else: return render_template('index.html')
    
