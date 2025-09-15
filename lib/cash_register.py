#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize CashRegister with optional discount percentage."""
        self._discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the discount percentage."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """Set the discount percentage with validation."""
        if not isinstance(value, int):
            print("Not valid discount")
            return
        if value < 0 or value > 100:
            print("Not valid discount")
            return
        self._discount = value
    
    def add_item(self, item, price, quantity=1):
        """Add an item to the cash register."""
        # Calculate total price for this transaction
        transaction_total = price * quantity
        
        # Update total
        self.total += transaction_total
        
        # Add items to the items list
        for _ in range(quantity):
            self.items.append(item)
        
        # Add transaction to previous_transactions
        transaction = {
            'item': item,
            'price': price,
            'quantity': quantity,
            'total': transaction_total
        }
        self.previous_transactions.append(transaction)
    
    def apply_discount(self):
        """Apply the discount to the total price."""
        if self._discount == 0:
            print("There is no discount to apply.")
            return
        
        # Calculate discount amount
        discount_amount = self.total * (self._discount / 100)
        
        # Apply discount
        self.total -= discount_amount
        
        # Print success message
        print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        """Remove the last transaction from the register."""
        if not self.previous_transactions:
            return
        
        # Get the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Subtract from total
        self.total -= last_transaction['total']
        
        # Remove items from items list
        for _ in range(last_transaction['quantity']):
            if self.items:
                self.items.pop()
