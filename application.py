from flask import Flask,request,render_template
import os
app = Flask(__name__)
st=''
@app.route("/")
def my_form():
	return render_template('load.html')
@app.route('/h',methods=['POST'])
def hello():
	#text=request.args.get('python_inp')
	global st
	text=request.form['javascript_data']
	values=request.form['cust_in']
	text="import sys\n"+text
	arg=values.split(",")
	cmd1=[]
	cmd='python3 /home/krishna/Desktop/firs/scrip.py'
	cmd1.append(cmd)
	cmd1=cmd1+arg
	cmd1=" ".join(cmd1)
	f=open('scrip.py','w')
	f.write(text)
	f.close()
	a=os.popen(cmd1).readlines()
	st=''.join(a)
	return st
app.run(debug=True)

