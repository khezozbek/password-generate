import random
import string


def generate_username(existing_usernames):
    while True:
        username = ''.join(random.choices(string.ascii_lowercase, k=8))
        if username not in existing_usernames:
            return username


def generate_password(existing_passwords):
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        if password not in existing_passwords:
            return password


def generate_data(num_samples):
    usernames = set()
    passwords = set()
    data = []

    for _ in range(num_samples):
        username = generate_username(usernames)
        password = generate_password(passwords)
        label = random.choice([True, False])  # Randomly assign correct or incorrect label

        usernames.add(username)
        passwords.add(password)

        data.append((username, password, label))

    return data


def save_data_to_file(data, filename):
    with open(filename, 'w') as f:
        for username, password, label in data:
            line = f"{username},{password}\n"
            f.write(line)


# Generate and save synthetic data
num_samples = 10012122 # Adjust the number of samples as per your requirement
data = generate_data(num_samples)
save_data_to_file(data, 'dataset.csv')
