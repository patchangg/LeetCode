class ProductOfNumbers:

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.products.append(self.products[-1] * num)
        else:
            self.products = [1]

    def getProduct(self, k: int) -> int:
        if len(self.products) > k:
            return self.products[-1] // self.products[-k - 1]
        else:
            return 0

# Store the product prefix so its faster to get the product of the numbers added
# If a zero gets added, reset the products array otherwise update the array
# by adding the last element multiplied by the new number
# To get product of last k numbers = prefix_product[end] / prefix_product[end-k]
# O(1) for all functions, O(n) space where n is the amount of numbers added
productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)        # [3]
productOfNumbers.add(0)        # [3,0]
productOfNumbers.add(2)       # [3,0,2]
productOfNumbers.add(5)        # [3,0,2,5]
productOfNumbers.add(4)        # [3,0,2,5,4]
productOfNumbers.getProduct(2) # return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3) # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4) # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8)        # [3,0,2,5,4,8]
productOfNumbers.getProduct(2) # return 32. The product of the last 2 numbers is 4 * 8 = 32
