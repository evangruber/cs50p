def main():
    x, y, z = input("Expression: ").split(" ")

    x, z = float(x), float(z)

    match y:
        case "+":
            print(f"{x + z:.1f}")
        case "-":
            print(f"{x - z:.1f}")
        case "*":
            print(f"{x * z:.1f}")
        case "/":
            print(f"{x / z:.1f}")

main()
