from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit
from mysql.connector import connect

class DatabaseManager(QWidget):
    def __init__(self, hostname, username, password, database):
        super().__init__()
        self.initUI()
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.err_msg = 'Не удалось осуществить запрос. Проверьте корректность ввода.'

    def initUI(self):
        self.setWindowTitle("Database Manager")
        self.setGeometry(300, 300, 1000, 800)
        layout = QVBoxLayout()

        self.createTableButton = QPushButton("Создать таблицу")
        self.createTableButton.clicked.connect(self.createTable)
        layout.addWidget(self.createTableButton)

        self.insertDataButton = QPushButton("Добавить запись")
        self.insertDataButton.clicked.connect(self.insertData)
        layout.addWidget(self.insertDataButton)

        self.readDataButton = QPushButton("Считать таблицу")
        self.readDataButton.clicked.connect(self.readData)
        layout.addWidget(self.readDataButton)

        self.updateDataButton = QPushButton("Обновить запись")
        self.updateDataButton.clicked.connect(self.updateData)
        layout.addWidget(self.updateDataButton)

        self.deleteDataButton = QPushButton("Удалить запись")
        self.deleteDataButton.clicked.connect(self.deleteData)
        layout.addWidget(self.deleteDataButton)

        self.setStyleSheet('''
                           QPushButton::hover {background-color: #FFC857; color: #ffffff; font-family: "Calibri"; font-size: 20pt; border-radius: 10px}
                           QPushButton {background-color: #465362; color: #ffffff; font-family: "Calibri"; font-size: 20pt; border-radius: 10px}
                           QPlainTextEdit {border-radius: 10px; font-family: "Calibri"; font-size: 20pt;}
                           ''') 

        self.outputTextEdit = QPlainTextEdit()
        self.outputTextEdit.setReadOnly(True)
        self.outputTextEdit.setPlaceholderText('Поле вывода')
        layout.addWidget(self.outputTextEdit)

        self.inputTextEdit = QPlainTextEdit()
        self.inputTextEdit.setPlaceholderText('Поле ввода')
        layout.addWidget(self.inputTextEdit)

        self.setLayout(layout)

    def createConnection(self):
        try:
            self.connection = connect(
                host=self.hostname,
                user=self.username,
                password=self.password,
                database=self.database
            )
        except:
            pass

    def createTable(self):
        try:
            data = self.inputTextEdit.toPlainText()
            data = data.split(':')
            tablename = data[0].strip()
            columns = data[1].strip()
            cursor = self.connection.cursor()
            query = f"CREATE TABLE IF NOT EXISTS {tablename} ({columns})"
            cursor.execute(query)
            self.connection.commit()
            self.outputTextEdit.setPlainText(f"Таблица {tablename} успешно создана.")
        except:
            self.outputTextEdit.setPlainText(self.err_msg)

    def insertData(self):
        try:
            data = self.inputTextEdit.toPlainText()
            data = data.split(':')
            tablename = data[0].strip()
            data = data[1].split(',')
            processed_data = list()
            for item in data:
                item = item.strip()
                if item.startswith('"') and item.endswith('"'):
                    processed_data.append(item[1:-1])
                else:
                    processed_data.append(int(item))
            data = processed_data
            cursor = self.connection.cursor()
            query = f"INSERT INTO {tablename} VALUES ({', '.join(['%s'] * len(data))})"
            cursor.execute(query, data)
            self.connection.commit()
            self.outputTextEdit.setPlainText(f"Запись успешно добавлена в таблицу {tablename}.")
        except:
            self.outputTextEdit.setPlainText(self.err_msg)

    def readData(self):
        try:
            tablename = self.inputTextEdit.toPlainText()
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {tablename}"
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                self.outputTextEdit.setPlainText(str(row))
        except:
            self.outputTextEdit.setPlainText(self.err_msg)

    def updateData(self):
        try:
            data = self.inputTextEdit.toPlainText()
            data = data.split(':')
            tablename = data[0].strip()
            data = data[1].split(';')
            condition = data[1].strip()
            data = data[0]
            cursor = self.connection.cursor()
            query = f"UPDATE {tablename} SET {data} WHERE {condition}"
            cursor.execute(query)
            self.connection.commit()
            self.outputTextEdit.setPlainText(f"Запись {condition} в таблице {tablename} успешно обновлена.")
        except:
            self.outputTextEdit.setPlainText(self.err_msg)

    def deleteData(self):
        try:
            data = self.inputTextEdit.toPlainText()
            data = data.split(':')
            tablename = data[0].strip()
            condition = data[1].strip()
            data = data[0]
            cursor = self.connection.cursor()
            query = f"DELETE FROM {tablename} WHERE {condition}"
            cursor.execute(query)
            self.connection.commit()
            self.outputTextEdit.setPlainText(f"Запись {condition} успешно удалена из таблицы {tablename}.")
        except:
            self.outputTextEdit.setPlainText(self.err_msg)