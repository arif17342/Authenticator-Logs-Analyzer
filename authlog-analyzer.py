import re
from collections import Counter

log_file = "sample_auth.log"
threshold = 3

failed_logins = Counter()

pattern = re.compile(
    r"Failed password for (?:invalid user )?(\S+) "
    r"from (\d{1,3}(?:\.\d{1,3}){3})"
)

with open(log_file, "r") as file:
    for line in file:
        match = pattern.search(line)

        if match:
            username, ip_address = match.groups()
            failed_logins[ip_address] += 1

print("\n=== AuthLog Analyzer ===")
print(f"Total failed login attempts: {sum(failed_logins.values())}")

print("\n=== Results ===")

if not failed_logins:
    print("No failed login attempts detected.")

for ip, count in failed_logins.most_common():
    print(f"{ip}: {count} failed attempts")

    if count >= threshold:
        print(f"  [ALERT] Repeated login failures from {ip}")