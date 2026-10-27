# SSH Authentication Log Analyzer

A **Python-based cybersecurity tool** that analyzes SSH authentication logs to identify failed login attempts and flag IP addresses with repeated failures.

## Features

- Parses SSH authentication log entries using regular expressions.
- Counts failed login attempts by source IP address.
- Displays a summary of detected failed login attempts.
- Generates alerts when an IP address reaches a configurable failure threshold.

## Technologies Used

- **Python 3**
- **Regular Expressions** (`re`)
- **Counter** (`collections`)
- **Kali Linux**

## Testing and Dataset Attribution

The script was tested using SSH authentication log data obtained from a publicly available third-party repository. The dataset was used locally for testing and is not included in this repository.

**Original dataset source:** https://github.com/logpai/loghub/blob/master/OpenSSH/OpenSSH_2k.log



## How It Works

The script reads a log file named `sample_auth.log` and searches for failed SSH login entries. It counts the attempts associated with each source IP address and flags IP addresses that meet the configured threshold.

## Example Output

```text
=== AuthLog Analyzer ===
Total failed login attempts: 519

=== Results ===
192.168.1.100: 5 failed attempts
  [ALERT] Repeated login failures from 192.168.1.100
```

*Note: Example output only. The IP address and counts above are illustrative, not actual findings from the dataset.*

## How to Run

1. Install Python 3.
2. Place `authlog-analyzer.py` and `sample_auth.log` in the same directory.
3. Open a terminal in that directory.
4. Run the following command:

```bash
python3 authlog-analyzer.py
```

## Limitations

- Log entries must match the format expected by the script.
- Flags repeated attempts but does not automatically prove an attack.
- The current version focuses on failed SSH password authentication entries.

## Future Improvements

- Support more varieties of authentication log formats.
- Export findings to a report.
- Add timestamps to further prove an attack 
