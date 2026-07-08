import json
import re
from collections import Counter

paths = Counter()
ips = Counter()
total = 0

with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        total += 1
        ips[line.split()[0]] += 1

        match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if match:
            paths[match.group(1)] += 1

top_count = max(paths.values())
top_path = sorted(path for path, count in paths.items() if count == top_count)[0]

with open("/app/report.json", "w") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "requests_by_ip": dict(sorted(ips.items())),
            "requests_by_path": dict(sorted(paths.items())),
            "top_path": top_path,
        },
        out,
        indent=2,
        sort_keys=True,
    )
