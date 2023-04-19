def time_conversion(s):
    # Write your code here
    if s[:2] == "12":
        if s[-2:] == "PM":
            return s[:-2]
        else:
            split_time = s[:-2].split(":")
            return f"00:{split_time[1]}:{split_time[2]}"

    if s[-2:] == "PM":
        split_time = s[:-2].split(":")
        return f"{int(split_time[0]) + 12}:{split_time[1]}:{split_time[2]}"
    else:
        return s[:-2]


if __name__ == '__main__':
    string_time = "07:05:45PM"
    result = time_conversion(string_time)
    print(result)
