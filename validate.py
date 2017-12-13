from flask import Flask
from iota.transaction.validator import BundleValidator

app = Flask(__name__)


@app.route('/')
def check():
    
   trytes="XVVTDRTDGJGYTFTCGFTIYTFIT9GCGHKCC"
    # convert user trytes into bundle first 
    # which function should be used here ? the one in multisig.py ?
    
    
    
    A = BundleValidator(trytes)
    print(A.is_valid())


if __name__ == '__main__':
    app.run()
