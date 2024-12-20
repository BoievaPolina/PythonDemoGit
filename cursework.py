def parse_logs(file_path):
    file_path = "test_logs.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()

    logs = []
    for line in lines:
        parts = line.strip().split(', ')
        log_entry = {
            'username': parts[0].split(': ')[1],
            'email': parts[1].split(': ')[1],
            'date_connected': parts[2].split(': ')[1],
            'ip': parts[3].split(': ')[1],
            'connection_duration': parts[4].split(': ')[1],
        }
        logs.append(log_entry)

    return logs

# Завдання 1
def get_date_range(logs):
    dates = [entry['date_connected'].split()[0] for entry in logs]
    return [min(dates), max(dates)]

# Завдання 2
def count_unique_users(logs):
    usernames = {entry['username'] for entry in logs}
    return len(usernames)

# Завдання 3
def count_connections_per_user(logs):
    connection_counts = {}
    for entry in logs:
        username = entry['username']
        connection_counts[username] = connection_counts.get(username, 0) + 1
    return connection_counts

# Завдання 4
def get_unique_ips_per_user(logs):
    user_ips = {}
    for entry in logs:
        username = entry['username']
        ip = entry['ip']
        if username not in user_ips:
            user_ips[username] = set()
        user_ips[username].add(ip)
    return {username: list(ips) for username, ips in user_ips.items()}

# Завдання 5
def count_unique_ips_per_user(logs):
    unique_ips = get_unique_ips_per_user(logs)
    return {username: len(ips) for username, ips in unique_ips.items()}

# Завдання 6
# Власна функція для підрахунку часу у секундах
def duration_to_seconds(duration):
    hours, minutes, seconds = map(int, duration.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def total_connection_time_per_user(logs):
    user_durations = {}
    for entry in logs:
        username = entry['username']
        duration = duration_to_seconds(entry['connection_duration'])
        user_durations[username] = user_durations.get(username, 0) + duration
    return user_durations

# Основний виклик функцій
if __name__ == "__main__":
    file_path = "test_logs.txt"
    logs = parse_logs(file_path)

    # Виконання завдань
    date_range = get_date_range(logs)
    unique_users_count = count_unique_users(logs)
    connections_per_user = count_connections_per_user(logs)
    unique_ips_per_user = get_unique_ips_per_user(logs)
    unique_ip_counts = count_unique_ips_per_user(logs)
    total_connection_times = total_connection_time_per_user(logs)

    # Результати друк для перевірки
    # print("Date range:", date_range)
    # print("Unique users count:", unique_users_count)
    # print("Connections per user:", connections_per_user)
    # print("Unique IPs per user:", unique_ips_per_user)
    # print("Unique IP counts:", unique_ip_counts)
    # print("Total connection times:", total_connection_times)