#
#
# class UniqueVisitor:
#
#     def __init__(self):
#         self.visitors = set()
#         self.counter = 0
#
#     def check_existence(self, key):
#         if not key in self.visitors:
#             return False
#         return True
#
#     def add_entry(self, val):
#         """
#         check existence
#         :return:
#         """
#         exists = self.check_existence(val)
#         if not exists:
#             self.visitors.add(val)
#             self.counter += 1
#             print(f"Added unique visitor:{val} and website: count is  {self.counter}")
#             return
#         print(f"Already exists - {val}")
#
#
#
# unique_visitor = UniqueVisitor()
# unique_visitor.add_entry("Ibrahim")
# unique_visitor.add_entry("RIZ")
# unique_visitor.add_entry("Ibrahim")
# unique_visitor.add_entry("KASIM")
# unique_visitor.add_entry("Anvari")
# unique_visitor.add_entry("Vignesh")

import hashlib
import math

class HyperLogLog:
    def __init__(self, b=4):
        """
        Initialize HyperLogLog.
        :param b: Number of bits to determine the number of registers (m = 2^b).
        """
        self.b = b
        self.m = 2 ** b  # Number of registers
        self.registers = [0] * self.m  # Initialize registers to 0
        self.alpha = self._calculate_alpha()

    def _calculate_alpha(self):
        """Calculate the alpha constant based on the number of registers (m)."""
        if self.m == 16:
            return 0.673
        elif self.m == 32:
            return 0.697
        elif self.m == 64:
            return 0.709
        else:
            return 0.7213 / (1 + 1.079 / self.m)

    def _hash(self, value):
        """Hash the input value using SHA-1 and return a 32-bit integer."""
        hash_hex = hashlib.sha1(str(value).encode('utf-8')).hexdigest()
        return int(hash_hex[:8], 16)  # Use the first 32 bits of the hash

    def _get_register_index_and_rank(self, hash_value):
        """Get the register index and the rank (number of leading zeros + 1)."""
        binary = format(hash_value, '032b')  # Convert hash to 32-bit binary string
        register_index = int(binary[:self.b], 2)  # First b bits for register index
        rank = len(binary[self.b:]) - len(binary[self.b:].lstrip('0')) + 1  # Count leading zeros
        return register_index, rank

    def add(self, value):
        """Add a value to the HyperLogLog."""
        hash_value = self._hash(value)
        register_index, rank = self._get_register_index_and_rank(hash_value)
        self.registers[register_index] = max(self.registers[register_index], rank)

    def count(self):
        """Estimate the cardinality of the dataset."""
        harmonic_mean = sum(2 ** -register for register in self.registers)
        raw_estimate = self.alpha * (self.m ** 2) / harmonic_mean

        # Apply small range correction
        if raw_estimate <= 2.5 * self.m:
            zeros = self.registers.count(0)
            if zeros != 0:
                return self.m * math.log(self.m / zeros)
        return raw_estimate

# Example usage
hll = HyperLogLog(b=4)  # Use 16 registers (2^4)
data = ["apple", "banana", "apple", "orange", "banana", "grape"]

for item in data:
    hll.add(item)

print("Estimated unique elements:", hll.count())