# Author: Prof. MM Ghassemi <ghassem3@msu.edu>
from flask import current_app as app
@app.route('/')
def hello():
	count = 28
	return f"""<html>
	           <h1>Hello World!</h1>
	           <p>zhujunchi's favorite number is {count}.</p>
	           </html>
	        """
