# -----------------------------
# Strategy Pattern Example
# -----------------------------

# Parent Class (Base Strategy)
class PaymentStrategy:
    # This method will be overridden in child classes
    def pay(self, amount):
        pass


# Credit Card Strategy
class CreditCardPayment(PaymentStrategy):

    # Override the parent method
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# PayPal Strategy
class PayPalPayment(PaymentStrategy):

    # Override the parent method
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


# Context Class
class PaymentContext:

    # Constructor
    def __init__(self, strategy):
        # Store current payment method
        self.strategy = strategy

    # Change payment method at runtime
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Execute payment
    def pay(self, amount):
        self.strategy.pay(amount)


# -----------------------------
# Main Program
# -----------------------------

# Create Credit Card Strategy
credit = CreditCardPayment()

# Give strategy to context
payment = PaymentContext(credit)

# Make payment
payment.pay(1000)

# Change strategy
paypal = PayPalPayment()

payment.set_strategy(paypal)

payment.pay(500)