from flask import Flask

app = Flask(__name__)
{% for row in rows %}
	
@app.route('{{ row['endpoint'] }}')
def {{ row['method'] }}():
	return "Showing {{ row['method'] }} route "
{% endfor %}


if __name__ == '__main__':
	app.run(host='{{ host }}', port={{ port }}, debug=True)