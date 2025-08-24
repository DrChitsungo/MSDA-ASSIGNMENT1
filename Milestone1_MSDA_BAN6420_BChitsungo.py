#Milestone Assignment 1: Policy Management System for Mashfords Insurance Company

from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, List

class PolicyholderStatus(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    INACTIVE = "inactive"

class ProductStatus(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DISCONTINUED = "discontinued"

class PaymentStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"
    LATE = "late"
    PENALTY_APPLIED = "penalty_applied"

class Policyholder:
    def __init__(self, policyholder_id: int, name: str, status: PolicyholderStatus = PolicyholderStatus.ACTIVE):
        if not policyholder_id or policyholder_id <= 0:
            raise ValueError("Policyholder ID must be a positive integer")
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")

        self.policyholder_id = policyholder_id
        self.name = name.strip()
        self.status = status
        self.created_date = datetime.now()
        self.policies: List['Policy'] = []

    def suspend(self, reason: str = ""):
        if self.status == PolicyholderStatus.SUSPENDED:
            print(f"Policyholder {self.name} is already suspended.")
            return False

        self.status = PolicyholderStatus.SUSPENDED
        print(f"Policyholder {self.name} suspended. Reason: {reason}")
        return True

    def reactivate(self):
        if self.status == PolicyholderStatus.ACTIVE:
            print(f"Policyholder {self.name} is already active.")
            return False

        self.status = PolicyholderStatus.ACTIVE
        print(f"Policyholder {self.name} reactivated.")
        return True

    def deactivate(self):
        self.status = PolicyholderStatus.INACTIVE
        print(f"Policyholder {self.name} deactivated.")

    def is_active(self) -> bool:
        return self.status == PolicyholderStatus.ACTIVE

    def add_policy(self, policy: 'Policy'):
        if policy not in self.policies:
            self.policies.append(policy)

    def get_active_policies(self) -> List['Policy']:
        return [policy for policy in self.policies if policy.is_active()]

    def __str__(self):
        return f"Policyholder[ID={self.policyholder_id}, Name={self.name}, Status={self.status.value}]"


class Product:
    def __init__(self, product_id: int, name: str, premium: float, status: ProductStatus = ProductStatus.ACTIVE):
        if not product_id or product_id <= 0:
            raise ValueError("Product ID must be a positive integer")
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        if premium < 0:
            raise ValueError("Premium cannot be negative")

        self.product_id = product_id
        self.name = name.strip()
        self.premium = premium
        self.status = status
        self.created_date = datetime.now()

    def update(self, name: Optional[str] = None, premium: Optional[float] = None):
        changes_made = []

        if name and name.strip():
            old_name = self.name
            self.name = name.strip()
            changes_made.append(f"name: {old_name} -> {self.name}")

        if premium is not None:
            if premium < 0:
                raise ValueError("Premium cannot be negative")
            old_premium = self.premium
            self.premium = premium
            changes_made.append(f"premium: {old_premium} -> {self.premium}")

        if changes_made:
            print(f"Product {self.product_id} updated: {', '.join(changes_made)}")
        else:
            print(f"No changes made to product {self.product_id}")

    def suspend(self, reason: str = ""):
        if self.status == ProductStatus.SUSPENDED:
            print(f"Product {self.name} is already suspended.")
            return False

        self.status = ProductStatus.SUSPENDED
        print(f"Product {self.name} suspended. Reason: {reason}")
        return True

    def discontinue(self):
        self.status = ProductStatus.DISCONTINUED
        print(f"Product {self.name} discontinued.")

    def reactivate(self):
        if self.status == ProductStatus.ACTIVE:
            print(f"Product {self.name} is already active.")
            return False

        self.status = ProductStatus.ACTIVE
        print(f"Product {self.name} reactivated.")
        return True

    def is_active(self) -> bool:
        return self.status == ProductStatus.ACTIVE

    def __str__(self):
        return f"Product[ID={self.product_id}, Name={self.name}, Premium=${self.premium:.2f}, Status={self.status.value}]"


class Policy:
    def __init__(self, policy_id: int, policyholder: Policyholder, product: Product,
                 start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        if not policy_id or policy_id <= 0:
            raise ValueError("Policy ID must be a positive integer")
        if not isinstance(policyholder, Policyholder):
            raise ValueError("Invalid policyholder")
        if not isinstance(product, Product):
            raise ValueError("Invalid product")

        self.policy_id = policy_id
        self.policyholder = policyholder
        self.product = product
        self.start_date = start_date or datetime.now()
        self.end_date = end_date or (self.start_date + timedelta(days=365))  # Default 1 year
        self.is_cancelled = False

        # Add this policy to the policyholder's policies
        policyholder.add_policy(self)

    def cancel(self):
        self.is_cancelled = True
        print(f"Policy {self.policy_id} cancelled.")

    def is_active(self) -> bool:
        now = datetime.now()
        return (not self.is_cancelled and
                self.start_date <= now <= self.end_date and
                self.policyholder.is_active() and
                self.product.is_active())

    def renew(self, duration_days: int = 365):
        if self.is_cancelled:
            raise ValueError("Cannot renew a cancelled policy")

        self.end_date = self.end_date + timedelta(days=duration_days)
        print(f"Policy {self.policy_id} renewed until {self.end_date.strftime('%Y-%m-%d')}")

    def __str__(self):
        return (f"Policy[ID={self.policy_id}, Holder={self.policyholder.name}, "
                f"Product={self.product.name}, Active={self.is_active()}]")


class Payment:
    def __init__(self, payment_id: int, policy: Policy, amount: float,
                 due_date: Optional[datetime] = None, payment_date: Optional[datetime] = None,
                 status: PaymentStatus = PaymentStatus.PENDING):
        if not payment_id or payment_id <= 0:
            raise ValueError("Payment ID must be a positive integer")
        if not isinstance(policy, Policy):
            raise ValueError("Invalid policy")
        if amount <= 0:
            raise ValueError("Payment amount must be positive")

        self.payment_id = payment_id
        self.policy = policy
        self.amount = amount
        self.due_date = due_date or (datetime.now() + timedelta(days=30))  # Default 30 days from now
        self.payment_date = payment_date
        self.status = status
        self.penalty_amount = 0.0
        self.created_date = datetime.now()

    @property
    def total_amount(self) -> float:
        return self.amount + self.penalty_amount

    def process_payment(self, payment_amount: Optional[float] = None):
        if self.status == PaymentStatus.PAID:
            print(f"Payment {self.payment_id} is already paid.")
            return False

        amount_to_pay = payment_amount or self.total_amount

        if amount_to_pay < self.total_amount:
            print(f"Insufficient payment amount. Required: ${self.total_amount:.2f}, Provided: ${amount_to_pay:.2f}")
            return False

        self.status = PaymentStatus.PAID
        self.payment_date = datetime.now()
        print(f"Payment {self.payment_id} of ${amount_to_pay:.2f} processed for {self.policy.policyholder.name}.")
        return True

    def send_reminder(self):
        if self.status == PaymentStatus.PAID:
            print(f"Payment {self.payment_id} already paid.")
            return

        days_until_due = (self.due_date - datetime.now()).days
        if days_until_due > 0:
            print(
                f"Reminder: Payment {self.payment_id} for {self.policy.policyholder.name} is due in {days_until_due} days.")
        else:
            print(
                f"URGENT: Payment {self.payment_id} for {self.policy.policyholder.name} is overdue by {abs(days_until_due)} days.")

    def check_overdue(self):
        if self.status == PaymentStatus.PAID:
            return False

        if datetime.now() > self.due_date:
            days_overdue = (datetime.now() - self.due_date).days
            if days_overdue <= 30:
                self.status = PaymentStatus.OVERDUE
            else:
                self.status = PaymentStatus.LATE
            return True
        return False

    def apply_penalty(self, penalty_rate: float = 0.1):
        if self.status not in [PaymentStatus.OVERDUE, PaymentStatus.LATE]:
            print(f"No penalty applicable for payment {self.payment_id}. Status: {self.status.value}")
            return False

        if self.status == PaymentStatus.PENALTY_APPLIED:
            print(f"Penalty already applied to payment {self.payment_id}.")
            return False

        self.penalty_amount = self.amount * penalty_rate
        self.status = PaymentStatus.PENALTY_APPLIED
        print(
            f"Penalty of ${self.penalty_amount:.2f} applied to payment {self.payment_id} for {self.policy.policyholder.name}.")
        return True

    def is_paid(self) -> bool:
        return self.status == PaymentStatus.PAID

    def __str__(self):
        due_str = self.due_date.strftime('%Y-%m-%d')
        paid_str = self.payment_date.strftime('%Y-%m-%d') if self.payment_date else "Not paid"
        return (f"Payment[ID={self.payment_id}, Holder={self.policy.policyholder.name}, "
                f"Product={self.policy.product.name}, Amount=${self.total_amount:.2f}, "
                f"Due={due_str}, Paid={paid_str}, Status={self.status.value}]")


class InsuranceManager:
    def __init__(self):
        self.policyholders: List[Policyholder] = []
        self.products: List[Product] = []
        self.policies: List[Policy] = []
        self.payments: List[Payment] = []

    def add_policyholder(self, policyholder: Policyholder):
        if policyholder not in self.policyholders:
            self.policyholders.append(policyholder)
            print(f"Policyholder {policyholder.name} added to system.")

    def add_product(self, product: Product):
        if product not in self.products:
            self.products.append(product)
            print(f"Product {product.name} added to system.")

    def create_policy(self, policy_id: int, policyholder_id: int, product_id: int) -> Optional[Policy]:
        policyholder = self.find_policyholder(policyholder_id)
        product = self.find_product(product_id)

        if not policyholder:
            print(f"Policyholder with ID {policyholder_id} not found.")
            return None

        if not product:
            print(f"Product with ID {product_id} not found.")
            return None

        if not policyholder.is_active():
            print(f"Cannot create policy for inactive policyholder {policyholder.name}.")
            return None

        if not product.is_active():
            print(f"Cannot create policy for inactive product {product.name}.")
            return None

        policy = Policy(policy_id, policyholder, product)
        self.policies.append(policy)
        print(f"Policy {policy_id} created for {policyholder.name} with product {product.name}.")
        return policy

    def create_payment(self, payment_id: int, policy_id: int, amount: Optional[float] = None) -> Optional[Payment]:
        policy = self.find_policy(policy_id)
        if not policy:
            print(f"Policy with ID {policy_id} not found.")
            return None

        payment_amount = amount or policy.product.premium
        payment = Payment(payment_id, policy, payment_amount)
        self.payments.append(payment)
        print(f"Payment {payment_id} created for ${payment_amount:.2f}.")
        return payment

    def find_policyholder(self, policyholder_id: int) -> Optional[Policyholder]:
        return next((ph for ph in self.policyholders if ph.policyholder_id == policyholder_id), None)

    def find_product(self, product_id: int) -> Optional[Product]:
        return next((p for p in self.products if p.product_id == product_id), None)

    def find_policy(self, policy_id: int) -> Optional[Policy]:
        return next((p for p in self.policies if p.policy_id == policy_id), None)

    def find_payment(self, payment_id: int) -> Optional[Payment]:
        return next((p for p in self.payments if p.payment_id == payment_id), None)

    def process_overdue_payments(self):
        overdue_count = 0
        for payment in self.payments:
            if payment.check_overdue():
                overdue_count += 1

        if overdue_count > 0:
            print(f"\n{overdue_count} payments marked as overdue.")
        else:
            print("\nNo overdue payments found.")

    def get_summary(self):
        active_policyholders = len([ph for ph in self.policyholders if ph.is_active()])
        active_products = len([p for p in self.products if p.is_active()])
        active_policies = len([p for p in self.policies if p.is_active()])
        pending_payments = len([p for p in self.payments if not p.is_paid()])

        print(f"\n=== INSURANCE SYSTEM SUMMARY ===")
        print(f"Active Policyholders: {active_policyholders}/{len(self.policyholders)}")
        print(f"Active Products: {active_products}/{len(self.products)}")
        print(f"Active Policies: {active_policies}/{len(self.policies)}")
        print(f"Pending Payments: {pending_payments}/{len(self.payments)}")
        print(f"================================")


def main():
    # Create insurance manager
    manager = InsuranceManager()

    print("=== Setting up Insurance Management System ===\n")

    # Create products
    try:
        health_insurance = Product(101, "Health Insurance", 500.0)
        car_insurance = Product(102, "Car Insurance", 300.0)
        life_insurance = Product(103, "Life Insurance", 200.0)

        manager.add_product(health_insurance)
        manager.add_product(car_insurance)
        manager.add_product(life_insurance)

    except ValueError as e:
        print(f"Error creating product: {e}")
        return

    # Create policyholders
    try:
        bezzel = Policyholder(1, "Bezzel Chitsungo")
        shellah = Policyholder(2, "Shellah Murwira")
        mukudzei = Policyholder(3, "Mukudzei Zuruvi")

        manager.add_policyholder(bezzel)
        manager.add_policyholder(shellah)
        manager.add_policyholder(mukudzei)

    except ValueError as e:
        print(f"Error creating policyholder: {e}")
        return

    print("\n=== Creating Policies ===")
    # Create policies
    manager.create_policy(1001, 1, 101)
    manager.create_policy(1002, 2, 101)
    manager.create_policy(1003, 1, 102)
    manager.create_policy(1004, 3, 103)

    print("\n=== Creating and Processing Payments ===")
    # Create payments
    payment1 = manager.create_payment(2001, 1001)  # Bezzel's health insurance
    payment2 = manager.create_payment(2002, 1002)  # Shellah's health insurance
    payment3 = manager.create_payment(2003, 1003)  # Bezzel's car insurance
    manager.create_payment(2004, 1004)

    # Process some payments
    if payment1:
        payment1.process_payment()
    if payment3:
        payment3.process_payment()

    print("\n=== Current Status ===")
    # Display current status
    for payment in manager.payments:
        print(payment)

    print("\n=== Demonstrating Management Features ===")

    # Demonstrate policyholder management
    bezzel.suspend("Missed premium payments")
    bezzel.reactivate()

    # Demonstrate product management
    car_insurance.update(name="Auto Insurance Premium", premium=350.0)
    life_insurance.suspend("Under review")
    life_insurance.reactivate()

    # Demonstrate overdue payment handling
    print("\n=== Payment Management Demo ===")
    if payment2:
        # Simulate overdue payment
        payment2.due_date = datetime.now() - timedelta(days=5)  # 5 days overdue
        payment2.check_overdue()
        payment2.send_reminder()
        payment2.apply_penalty()
        print(f"Updated payment: {payment2}")

        # Process payment with penalty
        payment2.process_payment()

    # Process all overdue payments
    manager.process_overdue_payments()

    # Display system summary
    manager.get_summary()

    print("\n=== Final System State ===")
    print("\nPolicyholders:")
    for ph in manager.policyholders:
        print(f"  {ph}")
        for policy in ph.get_active_policies():
            print(f"    └── {policy}")

    print("\nProducts:")
    for product in manager.products:
        print(f"  {product}")

    print("\nAll Payments:")
    for payment in manager.payments:
        print(f"  {payment}")


if __name__ == "__main__":
    main()