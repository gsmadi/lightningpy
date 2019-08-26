import codecs

def encode_macaroon(macaroon):
    encoded_macaroon = codecs.encode(macaroon, 'hex')

    return encoded_macaroon

def read_file(file_path):
    opened_file = open(file_path, 'rb').read()

    return opened_file