import requests
import csv



def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    print(f"Status code : {response.status_code}")
    print(f"response: {response.text}")

    if response.status_code == 200:
        users = response.json()
        print(f"Total Users fetched: {len(users)}")

        with open("reports/users.csv", "w", newline = "") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "email", "phone", "website"])
            writer.writeheader()
            for user in users:
                writer.writerow({
                    "id": user["id"],
                    "name": user["name"],
                    "email": user["email"],
                    "phone": user["phone"],
                    "website": user["website"]
                })
        
        print(f"Saved {len(users)} users to CSV")
    
    else: 
        print(f"Failed. Status code: {response.status_code}")
    
if __name__ == "__main__":
        fetch_users()




