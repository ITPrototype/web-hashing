import hashlib
import random
from passlib.hash import pbkdf2_sha256, phpass


def Hashing(hashtype, hash_value):
    if hashtype == "pbkdf2_sha256":
        pbhash = pbkdf2_sha256.hash(hash_value)
        return pbhash
    elif hashtype == "phpass":
        phpasshash = phpass.hash(hash_value)
        return phpasshash
    else:
        hash_t = hashlib.new(hashtype)
        hash_t.update(hash_value.encode())
        hashed = hash_t.hexdigest()
        return hashed


def generate(words):
    def random_generator(size, words):
        return "".join(random.choice(words) for _ in range(size))

    lower_words = [word.lower() for word in words]
    upper_words = [word.upper() for word in words]
    capitalized_words = [word.capitalize() for word in words]
    random_words = []

    for _ in range(20):
        random_words.append(random_generator(size=2, words=words))
        random_words.append(random_generator(size=2, words=lower_words))
        random_words.append(random_generator(size=2, words=upper_words))
        random_words.append(random_generator(size=2, words=capitalized_words))

    united_words = lower_words + upper_words + capitalized_words + random_words + words
    return united_words


def deHashUPH(wlist, hash_code):
    generated = generate(wlist)
    for line in generated:
        if Hashing("sha1", line) == hash_code:
            return ["sha1", line]
        elif Hashing("sha224", line) == hash_code:
            return ["sha224", line]
        elif Hashing("sha256", line) == hash_code:
            return ["sha256", line]
        elif Hashing("sha512", line) == hash_code:
            return ["sha512", line]
        elif Hashing("md5", line) == hash_code:
            return ["md5", line]
        elif pbkdf2_sha256.verify(line, Hashing("pbkdf2_sha256", line)):
            return ["pbkdf2_sha256", line]
        elif phpass.verify(line, Hashing("phpass",line)):
            return ["phpass", line]

    return ["Not found", "Not found"]
