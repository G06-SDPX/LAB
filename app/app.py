from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    q = request.args.get('q')
    print(q)
    return {"message": "Hello!"}, 201


@app.route('/is_prime/<int:x>')
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**(1/2)) + 1):
        if (x % i) == 0:
            return False
    return True


if __name__ == '__main__':
    app.run()
