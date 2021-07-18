# How to use

A simple serivce that generates an HTML link from a PDF, to use with tools like instapaper :(

1. Install `git`, `python3`, `pip3` and `pdftohtml` or `poppler-utils` (should be in your repos package manager)
2. `git clone git@github.com:George3d6/pdftoweb.git && cd pdftoweb`
3. `pip3 install -r requirements.txt --user`
4. `cp config.py.template config.py`
5. `nano config.py` and change values for username and password
6. `python3 server.py`
7. Got to the url (ideally put an nginx over it and configure ssl with e.g. letsencrypt) and you can now upload pdfs and be redirect to links to them converted to htmls
*Note: you might have to increase nginx/apache file limit, conversion and upload of large pdfs might take a while*