from cryptography.fernet import Fernet

# 鍵の生成
key = Fernet.generate_key()

# 鍵を使用してFernetオブジェクトを作成
fernet = Fernet(key)

# メッセージの暗号化
message = b"Hello, World!"
encrypted_message = fernet.encrypt(message)

# 暗号化されたメッセージの表示
print("暗号化されたメッセージ:", encrypted_message)

# メッセージの復号化
decrypted_message = fernet.decrypt(encrypted_message)

# 復号化されたメッセージの表示
print("復号化されたメッセージ:", decrypted_message)