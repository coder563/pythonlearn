from models import User
from repository import UserRepository

def main():
    


    user_repository = UserRepository()

    user_id = user_repository.get_user_id()

    user = User()
    user.create_user(user_id,'Ajay',30)
    user.change_balance(20)
    user.change_balance(40)

    user_repository.save(user)

    print(f'{user.id=},{user.balance=},{user.username}')

    user2 = user_repository.get(user.id)

    print(f'{user2.id=},{user2.balance=},{user2.events}')







if __name__ == '__main__':
    main()

