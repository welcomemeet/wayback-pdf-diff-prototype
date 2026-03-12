import json
from pdfdiff import compare

result = compare(
    "samples/capture1.pdf",
    "samples/capture2.pdf"
)

print(json.dumps(result, indent=2))