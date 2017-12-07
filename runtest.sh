python3 -m venv env
. env/bin/activate
pip install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
export PATH=$PATH:.
python -m unittest pruebas-selenium/captcha/captcha.py
