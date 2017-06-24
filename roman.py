#!/Users/jejoseph/anaconda3/bin/python
import sys

def convert(number):

    denominations = [1000,500,100,50,10,5,1]
    result_list = []
    divident = number
    test = True
#     test = False

    while divident > 1:
        for index, divisor in enumerate(denominations):
            quotient = int(divident/divisor)

            if test:
                print("divident: ", divident, "divisor:", divisor, "quotient:", quotient )
            if str(divisor)[0] == "5":
                next_divisor = denominations[index + 1 ]

                if divident/next_divisor == 9:
                    quotient = int(divident/next_divisor)
                    if test:
                        print("@", "divident: ", divident, "divisor:", divisor, "quotient:", quotient )
                    result_list.append((next_divisor, -1))
                    denominations.remove(divisor)
                    denominations.remove(next_divisor)
                    if test:
                        print("@", "divident: ", divident, "divisor:", divisor, "quotient:", quotient )
                    divident = divident % next_divisor
                    break

            if quotient >= 1:
                result_list.append((divisor,quotient))
                if test:
                    print("#", "divident: ", divident, "divisor:", divisor, "quotient:", quotient )

                divident = divident % divisor
                if test:
                    print("#", "divident: ", divident, "divisor:", divisor, "quotient:", quotient )

            denominations.remove(divisor)
            break
    if divident == 1:
        result_list.append((1,1))
    result = []
    for a_tuple in result_list:
        result.append(conversion_map(a_tuple))
    if test:
        print ("result_list: ", result_list, "result:", result)
    return "".join(result)

def conversion_map(a_tuple):

    base_map = { 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    numerals_list = ["I", "V", "X", "L", "C", "D", "M"]

    if a_tuple[1] == -1:

        current_numeral = base_map[a_tuple[0]]
        curr_index = numerals_list.index(current_numeral)
        next_numeral = numerals_list[curr_index + 2]
#         print ("current_numeral:", current_numeral, "next_numeral", next_numeral)
        return  current_numeral + next_numeral

    if a_tuple[1] == 4:
        current_numeral = base_map[a_tuple[0]]
        curr_index = numerals_list.index(current_numeral)
        next_numeral = numerals_list[curr_index + 1]
        return current_numeral + next_numeral

    current_numeral = base_map[a_tuple[0]]
    return current_numeral * a_tuple[1]



def test(integer, expected):
    converted = convert(integer)
    if converted == expected:
        print("SUCCESS: ","Input:", str(integer), "Output:", converted, "Expected: ", expected )
    else:
        print("FAILURE: ","Input:", str(integer), "Output:", converted, "Expected: ", expected )


def main():
    input = int(sys.argv[1])
    print(convert(input))
    # for case in [(1,"I"), (3,"III"), (4,"IV"), (10,"X"), (99,"XCIX"), (100,"C"), (323,"CCCXXIII"), (500,"D"), (999,"CMXCIX"), (1000,"M"), (1049,"MXLIX"), (3999,"MMMCMXCIX")]:
    #     test(case[0], case[1])



if __name__ == '__main__':
    main()
    
    
