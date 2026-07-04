"""
Dictionary Attack Password Cracker - Advanced Version
Educational tool to understand password security vulnerabilities
Features: OOP design, multiple algorithms, performance metrics
Author: Chiku
GitHub: github.com/jim0624/password-cracker
"""

import hashlib
import time
from typing import Tuple, Optional


class PasswordCracker:
    """
    Crack password hashes using dictionary attack methodology.
    Supports MD5, SHA-1, SHA-256 algorithms.
    """

    SUPPORTED_ALGORITHMS = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
    }

    def __init__(self, hash_value: str, algorithm: str = 'md5'):
        """
        Initialize the cracker.
        
        Args:
            hash_value: The hash to crack (hexadecimal string)
            algorithm: Hash algorithm used ('md5', 'sha1', 'sha256')
        """
        self.target_hash = hash_value.lower()
        self.algorithm = algorithm.lower()
        self.passwords_tried = 0
        self.start_time = None
        self.elapsed_time = 0

        if self.algorithm not in self.SUPPORTED_ALGORITHMS:
            raise ValueError(f"Algorithm '{algorithm}' not supported. Use: {list(self.SUPPORTED_ALGORITHMS.keys())}")

    def _hash_password(self, password: str) -> str:
        """Hash a password using the specified algorithm."""
        hash_func = self.SUPPORTED_ALGORITHMS[self.algorithm]
        return hash_func(password.encode()).hexdigest()

    def crack_with_common_passwords(self) -> Optional[Tuple[str, float]]:
        """
        Attempt to crack the password using common passwords.
        
        Returns:
            Tuple of (password, time_taken) if found, None otherwise
        """
        self.start_time = time.time()
        self.passwords_tried = 0

        common_passwords = [
            'password', '123456', 'admin', 'letmein', 'welcome',
            'monkey', 'dragon', 'master', 'sunshine', 'princess',
            'qwerty', 'abc123', '1234567', 'password1', '12345678',
            'test', 'guest', 'user', 'root', 'toor',
        ]

        for password in common_passwords:
            password_hash = self._hash_password(password)
            self.passwords_tried += 1

            if password_hash == self.target_hash:
                self.elapsed_time = time.time() - self.start_time
                return (password, self.elapsed_time)

        self.elapsed_time = time.time() - self.start_time
        return None

    def print_statistics(self):
        """Display cracking statistics."""
        if self.elapsed_time > 0:
            passwords_per_second = self.passwords_tried / self.elapsed_time
            print(f"\n{'='*50}")
            print(f"Cracking Statistics:")
            print(f"{'='*50}")
            print(f"Passwords tried:      {self.passwords_tried:,}")
            print(f"Time elapsed:         {self.elapsed_time:.2f} seconds")
            print(f"Speed:                {passwords_per_second:,.0f} passwords/second")
            print(f"Algorithm:            {self.algorithm.upper()}")
            print(f"{'='*50}\n")


def main():
    """Main function demonstrating the password cracker."""
    print("\n" + "="*50)
    print("  PASSWORD CRACKER - Advanced Version")
    print("  Dictionary Attack with OOP Design")
    print("="*50 + "\n")

    # Test hash (password: 'password123')
    test_hash = "482c811da5d5b4bc6d497ffa98491e38"
    test_password = "password123"

    print(f"Target hash: {test_hash}")
    print(f"Algorithm: MD5")
    print(f"Expected password: {test_password}\n")

    print("Starting crack with common passwords...")
    cracker = PasswordCracker(test_hash, algorithm='md5')
    result = cracker.crack_with_common_passwords()

    if result:
        found_password, time_taken = result
        print(f"\n✓ PASSWORD FOUND: '{found_password}'")
        cracker.print_statistics()
    else:
        print("\n✗ Password not found in common passwords list")
        cracker.print_statistics()
    
    print("--- Educational Purpose Only ---")
    print("This advanced version demonstrates:")
    print("- Object-Oriented Programming (OOP)")
    print("- Multiple hash algorithm support")
    print("- Performance metrics and statistics")
    print("- Professional Python practices\n")


if __name__ == "__main__":
    main()
