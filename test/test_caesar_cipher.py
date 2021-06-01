from caesar_cipher.caesar_cipher import encrypt,decrypt

def test_encrypt_one():
    actual = encrypt('Manchetser United',13)
    expected = 'znapurgfreahavgrq'
    assert actual == expected

def test_encrypt_two():
    actual = encrypt('Irbid is beautiful city',1)
    expected = 'jscjeojtocfbvujgvmodjuz'
    assert actual == expected

def test_decrypt_one():
    actual = decrypt('jscjeojtocfbvujgvmodjuz',1)
    expected = 'irbidnisnbeautifulncity'
    assert actual == expected

def test_decrypt_two():
    actual = decrypt('znapurgfreahavgrq',13)
    expected = 'manchetsernunited'
    assert actual == expected
