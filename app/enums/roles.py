from enum import Enum

#TODO: change the 'role' field in Role table to use this enum
class RoleEnum(str, Enum):
    ADMIN = 'ADMIN'
    CLIENT = 'CLIENT'
    OWNER = 'OWNER'
    AGENT = 'AGENT'
    INVESTOR = 'INVESTOR'