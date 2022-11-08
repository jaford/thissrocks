#Create a profit/loss calculator

def profit_loss():
# get two input integers for cost_price and selling_price
    cost_price = int(input('Enter cost price: '))
    selling_price = int(input('Enter selling price: '))

# calculate profit or loss amount and print it
    profit_price = selling_price - cost_price
    if profit_price < 0:
        print(f'Your loss is {profit_price}')
    else:
        print(f'Your profit is {profit_price}.')

profit_loss()