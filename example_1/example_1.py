# We want to track the execution of this code that generates random integers. Let's suppose that the values generated must respet some thresholds wich indicates if a value
# is a warning, an error or a critical error. Let's do it by using print
#
# python example_1.py


import random

if __name__ == "__main__":
    print("Generate some random integers")

    num_numbers = 10
    min_value = 0
    max_value = 20
    warning_threshold = 5
    error_threshold = 10
    critical_threshold = 15

    print(
        f"Numbers: {num_numbers}\nMin value: {min_value}\nMax value: {max_value}\nWaring threshold: {warning_threshold}\nError threshold: {error_threshold}\nCritical threshold: {critical_threshold}"
    )

    print("Start")
    for i in range(num_numbers):
        print(f"Iteration: {i}")
        value = random.randint(min_value, max_value)

        try:
            print("\tTry value")
            if value > critical_threshold:
                raise Exception(f"\tValue: {value} -> Critical!")
            elif value > error_threshold:
                print(f"\tValue: {value} -> Error!")
            elif value > warning_threshold:
                print(f"\tValue: {value} -> Warning!")
            else:
                print(f"\tValue: {value}")
        except Exception as e:
            print(e)
            exit()
        finally:
            print("The try except is finished")

    print("End")
else:
    pass
