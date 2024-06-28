import hashlib
import random
from passlib.hash import pbkdf2_sha256, phpass


def Hashing(hashtype, hash_value):
    hash_t = None
    if hashtype == "pbkdf2_sha256":
        pbhash = pbkdf2_sha256.hash(hash_value)
        return pbhash
    elif hashtype == "phpass":
        phpasshash = phpass.hash(hash_value)
        return phpasshash
    elif hashtype == "sha1":
        hash_t = hashlib.sha1()
    elif hashtype == "sha224":
        hash_t = hashlib.sha224()
    elif hashtype == "sha256":
        hash_t = hashlib.sha256()
    elif hashtype == "sha512":
        hash_t = hashlib.sha512()
    elif hashtype == "md5":
        hash_t = hashlib.md5()

    if hash_t:
        hash_t.update(hash_value.encode())
        hashed = hash_t.hexdigest()
        return hashed

    # else:
    #     hash_t = hashlib.new(hashtype)
    #     hash_t.update(hash_value.encode())
    #     hashed = hash_t.hexdigest()
    #     return hashed


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
    print(generated)
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
        elif pbkdf2_sha256.verify(line, Hashing("pbkdf2_sha256", hash_code)):
            return ["pbkdf2_sha256", line]
        elif phpass.verify(line, Hashing("phpass", hash_code)):
            return ["phpass", line]

    return ["Not found", "Not found"]