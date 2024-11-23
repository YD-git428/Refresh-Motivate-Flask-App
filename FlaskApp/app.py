from flask import Flask
import redis
import os
import random
from dotenv import load_dotenv  

load_dotenv()

app = Flask(__name__)

# Redis connection details
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = os.getenv('REDIS_PORT', 6379)
redis_password = os.getenv('REDIS_PASSWORD')

r = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    password='my_paswd',
    decode_responses=True 
)

# Reset the view counter to zero on container restart
r.set('visits', 0)

# Function to get a random quote
def get_random_quote():
    quotes = [
        "Sometimes you get blessed in ways you've <strong>never imagined...</strong>",
        "Productivity is key <strong>even if it doesn't go in line with the script</strong>",
        "Your hardwork will only fuel up the joy you will feel when you win",
        "Imagine giving up a <strong>whole opportunity</strong> because of a problem you <strong>thought</strong> cannot be solved...",
        "There is <strong>no such thing</strong> as having no time to do something, you're simply ignoring those 15 minute windows of free time you pass by <strong>everyday</strong>",
        "Struggle shapes your success",
        "If you <strong>priorities</strong> the right things properly, then you will <strong>most likely succeed in life</strong>",
        "Once you reach the <strong>top</strong> of the mountain, you're bound to make an <strong>easier</strong> journey back down the other side"
    ]
    return random.choice(quotes)

# Main welcome page route
@app.route('/')
def Welcome_page():
    return '''
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Webpage_Background</title>
            <style>
                body {
                    text-align: center;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 80vh; /* Full viewport height */
                    background: rgb(2,0,36);
                    background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 16%, rgba(0,212,255,1) 100%);
                    font-size: 70px;
                }
                .text {
                    color: rgba(7, 5, 79, 1);
                    font-size: 70px;
                    text-decoration: none;
                    font-family: Arial, sans-serif;
                    font-weight: bold;
                }
                .container {
                    border-style: solid;
                    border-width: 5px;
                    border-color: blue;
                    padding: 80px;
                    margin-top: 100px;
                    border-radius: 100px;
                    display: inline-block;
                    background-color: rgba(131, 127, 255, 1);
                }
                .btn {
                    padding: 10px 20px;
                    margin: 10px;
                    font-size: 30px;
                    font-family: Gill Sans, sans-serif;
                    color: black;
                    font-weight: bold;
                    background-color: #1A466D;
                    text-decoration: none;
                    border-radius: 5px;
                    border: 5px groove #007BFF;
                    cursor: pointer;
                }
                .btn:hover {
                    background-color: #193B59;
                }
                .typewriter h1 {
            font-size: 70px;
            white-space: nowrap;      /* Prevent text from wrapping */
            overflow: hidden;         /* Hide overflowing text */
            border-right: 3px solid black; /* Simulate the blinking cursor */
            display: inline-block;
            animation: typing 4s steps(40, end) forwards, blink-caret 0.75s step-end infinite;
        }

        @keyframes typing {
            from { width: 0; }    /* Start with width 0 */
            to { width: 100%; }   /* Animate to full width */
        }

        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: black; }  /* Blinking cursor effect */
        }

        @keyframes blink-caret {
            from, to { border-color: transparent; }  /* Invisible caret */
            50% { border-color: black; }            /* Visible caret */
        }
            </style>
        </head>
        <body>
            <div class="container">
            <div class="typewriter">
                <h1 class="text">Welcome to my First (ever) App!!!</h1>
            </div>
                <a href='/count' class="btn">Checkout my Quotes by Simply refreshing</a>
            
            </div>
        </body>
    </html>
    '''

# Counter route
@app.route('/count')
def counter():
    count = r.incr('visits')
    quote = get_random_quote()  # Calling get_random_quote to get the quote
    return f'''
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Webpage_Background</title>
            <style>
                body {{
                    text-align: center;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 80vh; /* Full viewport height */
                    background: rgb(2,0,36);
                    background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 16%, rgba(0,212,255,1) 100%);
                    font-size: 70px;
                }}
                .text {{
                    color: rgba(7, 5, 79, 1);
                    font-size: 20px;
                    text-decoration: none;
                    font-family: Arial, sans-serif;
                    font-weight: bold;
                    }}
                .text2 {{
                position: absolute;
                top: 0;
                left: 0;
                text-align: left;
                color: white;
                font-size: 20px;
                font-weight: bold
                }}
                
                .container {{
                    border-style: solid;
                    border-width: 5px;
                    border-color: blue;
                    padding: 100px;
                    margin-top: 100px;
                    border-radius: 30px;
                    display: inline-block;
                    background-color: rgba(131, 127, 255, 1);
                    
                }}
                .quote {{
                    font-size: 70px;
                    font-style: italic;
                    font-weight: none;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
        <div class="text2">
        <p1>*just refresh the page to get more quotes :)<p1>
        </div>
            <div class="container">
                <h1 class="text">Visitor count: {count}</h1>
                <!-- Display the random quote -->
                <div class="quote">{quote}</div>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)

