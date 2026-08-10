from typing import List, Set

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized: Set[str] = set()

        def apply_dot_rule(email: str) -> str:
            new_email = ""
            after_at = False
            for c in email:
                if c == "@" or after_at:
                    after_at = True
                    new_email += c
                elif c != ".":
                    new_email += c
            return new_email

        def apply_plus_rule(email: str) -> str:
            new_email = ""
            after_at = False
            after_plus = False
            for c in email:
                if c == "@" or after_at:
                    after_at = True
                    new_email += c
                elif after_plus:
                    continue
                elif c == "+":
                    after_plus = True
                else:
                    new_email += c
            return new_email

        for email in emails:
            normalized.add(apply_dot_rule(apply_plus_rule(email)))

        return len(normalized)
