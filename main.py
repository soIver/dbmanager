import sys
from manager import DatabaseManager
from PyQt5.QtWidgets import QApplication

hostname = '5.183.188.132'
username = 'db_vgu_student'
password = 'thasrCt3pKYWAYcK'
database = 'db_vgu_test'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseManager(hostname, username, password, database)
    window.createConnection()
    window.show()
    sys.exit(app.exec_())