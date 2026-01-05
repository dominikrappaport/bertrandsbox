from random import randint


def betrandsbox(n):
    colour = {
        1: "golden",
        2: "golden",
        3: "golden",
        4: "silver",
        5: "silver",
        6: "silver",
    }
    other_coin = {1: 2, 2: 1, 3: 4, 4: 3, 5: 6, 6: 5}
    total = 0
    two_golden = 0

    for _ in range(n):
        r = randint(1, 6)
        total += colour[r] == "golden"
        two_golden += colour[r] == "golden" and colour[other_coin[r]] == "golden"

    return two_golden / total


def main():
    n = 1000

    print(
        f"Probability of second coin being golden given first coin is golden: {betrandsbox(n):.2f}"
    )


if __name__ == "__main__":
    main()
