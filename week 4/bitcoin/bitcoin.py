def main():
    import sys
import requests


def main():

    args = len(sys.argv)

    if args < 2:
        sys.exit("Missing command-line argument")

    if args > 2:
        sys.exit("Too many arguments in command-line")

    try:
        btc_quantity = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    amount = btc_quantity * get_price()

    print(f"${amount:,.4f}")


def get_price():

    api_key = "c1247fd71eaf3560712153900c036f770da638ef66aae4367f0e241fe18c1455"

    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        ).json()
    except requests.RequestException:
        sys.exit("Unable to retrieve Bitcoin price")

    return float(response["data"]["priceUsd"])


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
