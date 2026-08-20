import json

class Database:

    def insert(self,name,email,password):
        with open('users_data.json','r') as af:
            users = json.load(af)

            if email in users:
                return 0
            else:
                users[email] = [name,password]

        with open('users_data.json','w') as wf:
            json.dump(users,wf)
            return 1

    def search(self,email,password):
        with open("users_data.json", 'r') as sf:
            users = json.load(sf)
            if email in users:
                if users[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0