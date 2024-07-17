from datetime import datetime

date_format = '%d-%m-%Y'
CATEGORIES = {'I':'Income', 'E':'Expense'}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("INVALID DATE. Please enter the date in dd-m-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input('Enter the amount: '))
        if amount<=0:
            raise ValueError('AMOUNT MUST BE GREATER THAN 0')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input('Enter the category ie Income(I) or Expense(E): ').upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print('Invalid Category Income(I) or Expense(E)')
    return get_category()

def get_description():
    return input("Enter a description (optional): ")