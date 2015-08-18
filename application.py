from flask import Flask, render_template
from random import randint

application = Flask( __name__ ) 

@application.route( '/' ) 
def index():
  with open( 'list.txt' ) as lis:
    restaurants = lis.readlines() 
    pick = restaurants[ randint( 0, len( restaurants ) ) ].strip()  
  return render_template( 'index.html', pick=pick ) 

if __name__ == '__main__':
  application.run( debug=True ) 
