# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start
check_interval = 15
check_count=10
for check in range(1, check_count+1):
    print(f"Check {check}: {check * check_interval} minutes after shift start")

