from flask import request, redirect, Flask
from flask_basicauth import BasicAuth
from config import port, host, debug, user, password
from secrets import choice
import string
import os
from flask import send_from_directory


app = Flask('pdftoweb')
app.config['BASIC_AUTH_USERNAME'] = user
app.config['BASIC_AUTH_PASSWORD'] = password
basic_auth = BasicAuth(app)


def pdf_to_html(filename):
    os.system(
        f"""cd pdfs && pdftohtml -s -dataurls '{filename}.pdf' && mv '{filename}-html.html' ../htmls/{filename}.html""")


@app.route('/', methods=['GET', 'POST'])
@basic_auth.required
def upload_file():
    if request.method == 'POST':
        filename = ''.join(
            [choice(string.ascii_uppercase + string.digits) for _ in range(50)])

        request.files['file'].save(f'pdfs/{filename}.pdf')
        pdf_to_html(filename)
        return redirect(f'/html/{filename}.html')

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/html/<filename>')
def get_html(filename):
    root_dir = os.getcwd()
    return send_from_directory(f'{root_dir}/htmls', f'{filename}')


@app.route('/pdf/<filename>')
def get_pdf(filename):
    root_dir = os.getcwd()
    return send_from_directory(f'{root_dir}/pdfs', f'{filename}')


if __name__ == '__main__':
    app.run(port=port, host=host, debug=debug)
