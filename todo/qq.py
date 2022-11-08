def main():

    # collect string input from the user
    HOST = input("Please enter hostname:")
    IP = input("Please enter IP Address:")
    DOMAIN = input("Please enter Domainname:")

    IP_table = []
    IP_table.append(IP)
    IP_table.append(HOST)
    IP_table.append('.')
    IP_table.append(DOMAIN)
    print(IP_table[0])

    for list_host in IP_table:
        print(list_host, end=" ")

if  __name__ == "__main__":
    main()

