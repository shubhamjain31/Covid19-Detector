from flask import Flask,render_template,request
app = Flask(__name__)
import pickle

#open a file, where you stored the pickled data
file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()

@app.route('/',methods=["GET","POST"])
def hello_world():
	if request.method == "POST":
		mydata = request.form
		fever = int(mydata['fever'])
		age = int(mydata['age'])	
		pain = int(mydata['pain'])
		runnyNose = int(mydata['runnyNose'])
		diffBreath = int(mydata['diffBreath'])
		#code for inference
		inputFeatures = [fever,age,pain,runnyNose,diffBreath]
		infProb = clf.predict_proba([inputFeatures])[0][1]
		return render_template('show.html',inf=round((infProb)*100))
	return render_template('index.html')

@app.route('/contactus')
def contactus():
	return render_template('contactus.html')

if __name__ == '__main__':
	app.run(debug=True)