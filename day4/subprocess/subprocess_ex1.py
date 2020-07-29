import subprocess
import re
from pprint import pprint


def subprocess_wrapper(cmd_list, raise_error=True):
    """Wrapper to execute subprocess including byte to UTF-8 conversion."""
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = proc.communicate()
    (std_out, std_err) = [x.decode("utf-8") for x in (std_out, std_err)]
    if raise_error and std_err:
        print(f"An error occurred:\n{std_err}")

    return (std_out, std_err, proc.returncode)


def process_disk_usage(df_output):
    """
    Extract the file-system and disk usage from 'df -h' output.

    Could also use same "pattern" and re.search (while looping over the lines, but
    re.find was a more elegant solution).
    """
    # Strip out the header line
    df_output = re.sub(r"^Filesystem.*Mounted on$", "", df_output, flags=re.M)
    pattern = r"^(\S+).*?(\d+%) .*"
    match = re.findall(pattern, df_output, flags=re.M)
    if not match:
        raise ValueError("Failed to parse 'df' output correctly")
    return match


if __name__ == "__main__":

    cmd_list = ["df", "-h"]
    std_out, _, _ = subprocess_wrapper(cmd_list)
    df_list = process_disk_usage(std_out)

    # Convert list over to final form and print it using a list comprehension
    disk_usage_list = [{"filesystem": fs, "usage": usage} for fs, usage in df_list]
    print()
    pprint(disk_usage_list)
    print()

    # Alternative solution using more standard for-loop
    disk_usage_list = []
    for fs, usage in df_list:
        disk_usage_list.append({"filesystem": fs, "usage": usage})
    print()
    pprint(disk_usage_list)
    print()
