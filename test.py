from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar'] 

class ConverterRoutesTestCase(TestCase):
    def test_index(self):
        "Tests if index route is followed correctly"
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text = True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>', html)

    def test_valid_input(self):
        """ Test to see if when post route is followed, passed in data makes it to the html as intended """
        with app.test_client() as client:
            res = client.post('/conversion', data={'convert_from': 'USD', 'convert_to': 'EUR', 'amount':'20'})
            html = res.get_data(as_text = True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<p>The result is €20.01.</p>', html)
    def test_invalid_input(self):
        """ Test to see if redirect code is received when invalid currency code is passed """
        with app.test_client() as client:
            res = client.post('/conversion', data={'convert_from': 'ABC', 'convert_to': 'USD', 'amount':'20'})
            self.assertEqual(res.status_code, 302)

    def test_invalid_code_redirect_with_flash(self):
        """ Test to see if redirect code is received when invalid currency code is passed """
        with app.test_client() as client:
            res = client.post('/conversion', data={'convert_from': 'ABC', 'convert_to': 'EUR', 'amount':'20'}, follow_redirects= True)
            html = res.get_data(as_text = True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<p>Invalid Currency Code</p>', html)