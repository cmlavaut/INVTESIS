import pandas as pd 

dbusers = '../database/users.csv'

def get_user(user_id):
    db = pd.read_csv(path)
    return db[db['username']==user_id].reset_index()

def user_put(user_data):
    db = pd.read_csv(path)
    user_ref = {
        'username' : [user_data.username],
        'password' : [user_data.password],
        'name' : [user_data.name],
        'email' : [user_data.email]
    }
    db = pd.concat([db, pd.DataFrame(user_ref)],ignore_index=True)
    db.to_csv(path, index=False)
