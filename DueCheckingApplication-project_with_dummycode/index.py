from nodues import app, db

with app.app_context():
    db.create_all()
    
@app.route("/")   
   def home():
       return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0' )

