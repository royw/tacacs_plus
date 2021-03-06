# versioning
TAC_PLUS_MAJOR_VER = 0xc
TAC_PLUS_MINOR_VER = 0x0
TAC_PLUS_MINOR_VER_ONE = 0x1

# types + actions
TAC_PLUS_AUTHEN = 0x01
TAC_PLUS_AUTHOR = 0x02
TAC_PLUS_AUTHEN_LOGIN = 0x01
TAC_PLUS_ACCT = 0x03

# services
TAC_PLUS_AUTHEN_SVC_NONE = 0x00
TAC_PLUS_AUTHEN_SVC_LOGIN = 0x01

# authentication types
TAC_PLUS_AUTHEN_TYPE_NOT_SET = 0x00
TAC_PLUS_AUTHEN_TYPE_ASCII = 0x01
TAC_PLUS_AUTHEN_TYPE_PAP = 0x02
TAC_PLUS_AUTHEN_TYPE_CHAP = 0x03
TAC_PLUS_AUTHEN_TYPES = {
    'ascii': TAC_PLUS_AUTHEN_TYPE_ASCII,
    'pap': TAC_PLUS_AUTHEN_TYPE_PAP,
    'chap': TAC_PLUS_AUTHEN_TYPE_CHAP,
}

# authentication flags
TAC_PLUS_CONTINUE_FLAG_ABORT = 0x01

# authentication statuses
TAC_PLUS_AUTHEN_STATUS_PASS = 0x01
TAC_PLUS_AUTHEN_STATUS_FAIL = 0x02
TAC_PLUS_AUTHEN_STATUS_GETDATA = 0x03
TAC_PLUS_AUTHEN_STATUS_GETUSER = 0x04
TAC_PLUS_AUTHEN_STATUS_GETPASS = 0x05
TAC_PLUS_AUTHEN_STATUS_RESTART = 0x06
TAC_PLUS_AUTHEN_STATUS_ERROR = 0x07
TAC_PLUS_AUTHEN_STATUS_FOLLOW = 0x21

# priveleges
TAC_PLUS_PRIV_LVL_MIN = 0x00
TAC_PLUS_PRIV_LVL_MAX = 0x0F

# authorization statuses
TAC_PLUS_AUTHOR_STATUS_PASS_ADD = 0x01
TAC_PLUS_AUTHOR_STATUS_PASS_REPL = 0x02
TAC_PLUS_AUTHOR_STATUS_FAIL = 0x10
TAC_PLUS_AUTHOR_STATUS_ERROR = 0x11
TAC_PLUS_AUTHOR_STATUS_FOLLOW = 0x21

# authentication methods
TAC_PLUS_AUTHEN_METH_NOT_SET = 0x00
TAC_PLUS_AUTHEN_METH_NONE = 0x01
TAC_PLUS_AUTHEN_METH_KRB5 = 0x02
TAC_PLUS_AUTHEN_METH_LINE = 0x03
TAC_PLUS_AUTHEN_METH_ENABLE = 0x04
TAC_PLUS_AUTHEN_METH_LOCAL = 0x05
TAC_PLUS_AUTHEN_METH_TACACSPLUS = 0x06
TAC_PLUS_AUTHEN_METH_GUEST = 0x08
TAC_PLUS_AUTHEN_METH_RADIUS = 0x10
TAC_PLUS_AUTHEN_METH_KRB4 = 0x11
TAC_PLUS_AUTHEN_METH_RCMD = 0x20

# accounting methods
TAC_PLUS_ACCT_FLAG_START = 0x02
TAC_PLUS_ACCT_FLAG_STOP = 0x04
TAC_PLUS_ACCT_FLAG_WATCHDOG = 0x08
TAC_PLUS_ACCT_FLAGS = {
    'start': TAC_PLUS_ACCT_FLAG_START,
    'stop': TAC_PLUS_ACCT_FLAG_STOP,
    'update': TAC_PLUS_ACCT_FLAG_WATCHDOG
}

# accounting statuses
TAC_PLUS_ACCT_STATUS_SUCCESS = 0x01
TAC_PLUS_ACCT_STATUS_ERROR = 0x02
TAC_PLUS_ACCT_STATUS_FOLLOW = 0x21

# port and rem_addr, useful inside tac_plus accounting logs
TAC_PLUS_VIRTUAL_PORT = "python_tty0"
TAC_PLUS_VIRTUAL_REM_ADDR = "python_device"
