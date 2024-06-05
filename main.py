from src.functions import get_operations, sort_data, date_prettify, secure


def main():
    operations = get_operations('operations.json')
    operations = sort_data(operations)
    # for element in operations:
    #     description = element["description"]
    #     date_new = element['date']
    #     sender = secure(element['from'])
    #     reciever = secure(element['to'])
    #     amount = element['operationAmount']['amount']
    #     currency = element['operationAmount']['currency']['name']
    #     print(date_prettify(date_new), description)
    #     print(sender, '->', reciever)
    #     print(amount, currency, end='\n\n')
    print(operations)

if __name__=='__main__':
    main()