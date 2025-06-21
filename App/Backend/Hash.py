class Hash:

    def genHash_sha256(data):
        
        import hashlib
        try:
            try:
                text=data.strip()
                byte_data = text.encode('utf-8')
            except:
                byte_data = data.strip()

            sha256_hash = hashlib.sha256(byte_data).hexdigest()
        except Exception as e:
            print(e)
            return("Error : E02 - Hashing Failed")

        return sha256_hash

