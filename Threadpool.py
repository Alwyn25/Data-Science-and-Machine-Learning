import concurrent.futures
import random

def save_random_file(filename):
    random_number = random.randint(1, 100)
    with open(f"{filename}_{random_number}.txt", "w") as file:
        file.write(f"Random Numbers : {random_number}")
        
def main():
    filenames = [f"file_{i}" for i in range(1, 6)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(save_random_file, filenames)

if __name__ == "__main__":
    main()