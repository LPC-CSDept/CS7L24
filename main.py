def main():
    ##################################################
    # Comlete your code here
    ##################################################
    str = 'Python Programming'
    sub1 = str[:6]
    sub2 = str[-11:]
    merged_str = sub2 + ' ' + sub1
    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
