import os

ROOT_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print ROOT_DIR

SETTINGS_DIR = os.path.join(ROOT_DIR, 'settings')
CORE_SETTINGS_DIR = os.path.join(SETTINGS_DIR, 'core')
HOSTAPD_INI = os.path.join(CORE_SETTINGS_DIR, 'hostapd.ini')
CORE_INI = os.path.join(CORE_SETTINGS_DIR, 'core.ini')

DB_DIR = os.path.join(ROOT_DIR, 'db')
EAP_USER_FILE = os.path.join(DB_DIR, 'hostapd.eap_user')

TMP_DIR = os.path.join(ROOT_DIR, 'tmp')
HOSTAPD_CONF = os.path.join(TMP_DIR, 'hostapd-wpe.conf')
CORE_CONF = os.path.join(TMP_DIR, 'core.conf')

CERTS_DIR = os.path.join(ROOT_DIR, 'certs')
CA_CNF = os.path.join(CERTS_DIR, 'ca.cnf')
SERVER_CNF = os.path.join(CERTS_DIR, 'server.cnf')
CLIENT_CNF = os.path.join(CERTS_DIR, 'client.cnf')
BOOTSTRAP_FILE = os.path.join(CERTS_DIR, 'bootstrap')
CA_PEM = os.path.join(CERTS_DIR, 'ca.pem')
SERVER_PEM = os.path.join(CERTS_DIR, 'server.pem')
PRIVATE_KEY = os.path.join(CERTS_DIR, 'server.pem')
DH_FILE = os.path.join(CERTS_DIR, 'dh')

HOSTAPD_EXEC_PATH = os.path.join(ROOT_DIR, 'hostapd-2.6/hostapd/hostapd-wpe')
HOSTAPD_LIB_PATH = os.path.join(ROOT_DIR,'hostapd-2.6/hostapd/libhostapd-eaphammer.so')
