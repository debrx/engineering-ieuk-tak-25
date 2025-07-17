import re
from collections import Counter
import pandas as pd

# Sample log file path
LOG_FILE = "sample-log.log"

# Regular expression to parse the log format
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s-\s(?P<country>[A-Z]{2})\s-\s\[(?P<datetime>[^\]]+)\]\s'
    r'"(?P<method>GET|POST|PUT|DELETE|HEAD|OPTIONS) (?P<url>\S+) HTTP/\d\.\d"\s'
    r'(?P<status>\d{3})\s(?P<size>\d+)\s"(?P<referrer>[^"]*)"\s"(?P<user_agent>[^"]+)"\s(?P<response_time>\d+)'
)

# Parse log lines into a structured format
def parse_log(file_path):
    entries = []
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                entries.append(match.groupdict())
    return pd.DataFrame(entries)

# Analysis: most active IPs, user agents, and URLs
def analyze_logs(df):
    print("\nTop 10 IPs by number of requests:")
    print(df['ip'].value_counts().head(16))

    print("\nTop 10 User Agents:")
    print(df['user_agent'].value_counts().head(16))

    print("\nTop 10 URLs accessed:")
    print(df['url'].value_counts().head(16))

    # Optional: convert datetime to datetime format
    df['datetime'] = pd.to_datetime(df['datetime'], format='%d/%m/%Y:%H:%M:%S')
    return df

if __name__ == "__main__":
    df_logs = parse_log(LOG_FILE)
    if df_logs.empty:
        print("No valid log entries found.")
    else:
        df_logs = analyze_logs(df_logs)



