sales = [1200, 850, 2100, 1500, 950]

total_sales = sum(sales)
number_of_sales = len(sales)
average_sale = total_sales / number_of_sales
largest_sale = max(sales)

print("BUSINESS SALES REPORT")
print("---------------------")
print(f"Number of sales: {number_of_sales}")
print(f"Total revenue: ${total_sales:,.2f}")
print(f"Average sale: ${average_sale:,.2f}")
print(f"Largest sale: ${largest_sale:,.2f}")