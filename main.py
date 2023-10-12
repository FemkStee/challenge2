from flask import Flask, render_template, request

app = Flask(__name__)

correct_code = '1234'
code = ''

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    global code
    result = None
    start_display = True

    if request.method == 'POST':
        button_value = request.form['button_value']
        if button_value == 'C':
            code = ''
        else:
            code += button_value
        input_code = request.form['code']
        if input_code == correct_code:
            result = 'Code juist'
            start_display = None

    print(result)
    print(start_display)
    return render_template('./index.html', result=result, start_display=start_display, code=code)

if __name__ == '__main__':
    app.run(debug=True)
