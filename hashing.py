import bcrypt
#SALT = bcrypt.gensalt()
# print(bcrypt.gensalt())
SALT = b'$2b$12$JiG/F.oVp3CNdJBx6IWBou'


def hash_password(plain_password: str):
    """This function hashes the password."""
    password_bytes = bcrypt.hashpw(password=plain_password.encode("utf8"), salt=SALT)
    return password_bytes.decode("utf8")


def verify_password(plain_password: str, password_hash: str):
    """This function verify the hashed password."""
    return bcrypt.checkpw(plain_password.encode("utf8"), password_hash.encode("utf8"))


# print(hash_password("furqan"))

furqan_hash = "$2b$12$JiG/F.oVp3CNdJBx6IWBougLGCiUBCnG6yzimToop8ZuMgTvfAve2"

# print(verify_password("furqan", furqan_hash))
