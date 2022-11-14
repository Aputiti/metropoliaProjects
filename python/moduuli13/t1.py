from flask import Flask

app = Flask(__name__)


@app.route('/checkPrime/<user_num>')
def check_prime(user_num):
    is_not_prime_num = False
    # Assuming 1 is a prime number
    if int(user_num) >= 1:
        for i in range(2, int(user_num)):
            if int(user_num) % i == 0:
                is_not_prime_num = True
                break
    else:
        is_not_prime_num = True

    answer = {
        "Number": user_num,
        "isPrime": not is_not_prime_num
    }

    return answer


if __name__ == '__main__':
    app.run(use_reloader=True, host='localhost', port=3000)
