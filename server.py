from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/play')
@app.route('/play/<int:num_boxes>')
@app.route('/play/<int:num_boxes>/<color>')
def play(color='skyblue', num_boxes=3):
	print(color)
	print(num_boxes)
	title = "Playground"
	return render_template('index.html', title=title, color=color, num_boxes=num_boxes)

# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template('index.html', title='404', phrase='Sorry! No response. Try again.', num_times=1)

if __name__ == "__main__":
	app.run(debug=True)