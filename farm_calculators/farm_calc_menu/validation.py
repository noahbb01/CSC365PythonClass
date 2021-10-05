# !/usr/bin/env python3

def get_range(prompt, low, high, data_type='int'):
    while True:
        user_input = input(f'{prompt} (Range {low}-{high}): ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if low < number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)


# def get_positive_num(prompt, data_type='int'):


# def get_num(prompt, data_type='int')


def main():
    choice = "y"
    while choice.lower() == "y":
        # get input
        valid_number = get_range(prompt='Enter float', low=0, high=1000, data_type='float')
        print("Valid float = ", valid_number)
        print()
        valid_number = get_range(prompt='Enter int', low=0, high=1000, data_type='int')
        print("Valid integer = ", valid_number)
        print()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
