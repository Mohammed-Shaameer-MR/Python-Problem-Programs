class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    def run(self):
        print("\nWelcome to Calculator!")
        print("Commands: add, sub, mul, div followed by two numbers")
        print("Example: add 5 4")
        print("Type 'exit' to quit\n")

        while True:
            cmd = input("Enter command: ").strip().lower()

            if cmd == 'exit':
                print("Bye Bye Bye!")
                break

            parts = cmd.split()
            if len(parts) != 3:
                print("Invalid format. Use: add 5 4")
                continue

            op, num1, num2 = parts[0], parts[1], parts[2]

            if not (num1.isdigit() and num2.isdigit()):
                print("Both inputs must be numbers.")
                continue

            a = int(num1)
            b = int(num2)

            if op == 'add':
                print(f"Result: {self.add(a, b)}")
            elif op == 'sub':
                print(f"Result: {self.sub(a, b)}")
            elif op == 'mul':
                print(f"Result: {self.mul(a, b)}")
            elif op == 'div':
                print(f"Result: {self.div(a, b)}")
            else:
                print("Unknown command. Use add, sub, mul, div.")

Calculator().run()
