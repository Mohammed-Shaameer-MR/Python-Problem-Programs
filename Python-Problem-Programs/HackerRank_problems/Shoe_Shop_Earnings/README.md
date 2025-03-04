# Raghu's Shoe Shop Earnings 

## Problem Description  
Raghu is a shoe shop owner. His shop has **X** number of shoes.  

He has a list containing the size of each shoe available in the shop.  

There are **N** customers who are willing to pay **x₁** amount of money only if they get the shoe of their desired size.  

Your task is to compute the total amount of money Raghu earned.  

## Formula  
Total earnings = Sum of all successful shoe sales.  

## Input Format  
1. The first line contains **X**, the number of shoes in the shop.  
2. The second line contains the space-separated shoe sizes available.  
3. The third line contains **N**, the number of customers.  
4. The next **N** lines each contain:  
   - The shoe size the customer wants.  
   - The price they are willing to pay.  

## Output Format  
Print the total money earned by Raghu.  

## **Constraints**  
0 < X < 1000        → Number of shoes in the shop.
0 < N < 1000        → Number of customers.
20 < xᵢ < 100       → Price range of shoes.
2 < Shoe Size < 20  → Available shoe sizes

## Example  

### Input  
```
10  
2 3 4 5 6 8 7 6 5 18  
6  
6 55  
6 45  
6 55  
4 40  
18 60  
10 50  
```

### Output
```
200
```

### Processing 
- **Customer 1:** Purchased size **6** shoe for **$55**.  
- **Customer 2:** Purchased size **6** shoe for **$45**.  
- **Customer 3:** Size **6** no longer available → No purchase.  
- **Customer 4:** Purchased size **4** shoe for **$40**.  
- **Customer 5:** Purchased size **18** shoe for **$60**.  
- **Customer 6:** Size **10** not available → No purchase.  

**Total earnings:**  
55 + 45 + 40 + 60 = **$200**  
