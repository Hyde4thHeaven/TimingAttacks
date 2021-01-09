import time
from hmac import compare_digest


def check_authorized_unsecured(password):
    if password == 'HYDEHEAVEN'*50:
        return True
    else:
        return False
  
def check_authorized_secured(password):
    if compare_digest(password, 'HYDEHEAVEN'*50):
        return True
    else:
        return False

print('=========================')

password = 'HYPEHEAVEN'
start = time.time()
print(check_authorized_unsecured(password))
end = time.time()
print('Time for HYPEHEAVEN (== operation:)', end - start)

password = 'HYDEHAEVEN'*50
start = time.time()
print(check_authorized_unsecured(password))
end = time.time()
print('Time for HYDEHAEVEN (== operation:)', end - start)

password = 'HYDEHEAVEN'*50 + 'T'
start = time.time()
print(check_authorized_unsecured(password))
end = time.time()
print('Time for HYDEHEAVENNNNT (== operation:)', end - start)

password = 'HYDEHEAVEN'*50
start = time.time()
print(check_authorized_unsecured(password))
end = time.time()
print('Time for HYDEHEAVEN (== operation:)', end - start)

print('=========================')
