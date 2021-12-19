# Shape is the letter that you give, v = triangle, u = circle etc
def find_area(shape):
    # write your if else statements here

    if shape == 'v':
        b = float(input("give base"))
        l = float(input("give height"))
        area = 0.5 * b* l

        # add this line at the end
        return area

    # and so on


def main():
    while(True):
        shape = input("Enter which shape")
        area = find_area(shape)
        print('The Area is', area)

main()