Parse the Apache-style access log at /app/access.log and write a JSON report to
/app/report.json.

Success criteria:

1. /app/report.json exists and contains valid JSON.
2. The JSON object has exactly these keys: total_requests, unique_ips,
   requests_by_ip, requests_by_path, and top_path.
3. total_requests is the number of non-empty log entries.
4. unique_ips is the number of distinct client IP addresses.
5. requests_by_ip maps each client IP address to its request count.
6. requests_by_path maps each requested path to its request count.
7. top_path is the path with the highest request count; if there is a tie, use
   the lexicographically smallest tied path.

You have 120 seconds to complete this task. Do not cheat by using online solutions
or hints specific to this task.
