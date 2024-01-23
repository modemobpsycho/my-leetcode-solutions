from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(email) -> str:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            return f"{local}@{domain}"

        return len(set(map(parse, emails)))
