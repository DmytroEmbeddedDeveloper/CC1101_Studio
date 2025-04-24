import sys, time, serial, re
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from MainWindow import Ui_MainWindow
from PySide6.QtCore import QTimer
from PySide6.QtGui import QTextCursor
import serial.tools.list_ports

cc1101StateMachine = {
    0x00: "SLEEP",
    0x01: "IDLE",
    0x02: "XOFF",
    0x03: "VCOON_MC",
    0x04: "REGON_MC",
    0x05: "MANCAL",
    0x06: "VCOON",
    0x07: "REGON",
    0x08: "STARTCAL",
    0x09: "BWBOOST",
    0x0A: "FS_LOCK",
    0x0B: "IFADCON",
    0x0C: "ENDCAL",
    0x0D: "RX", 
    0x0E: "RX_END",
    0x0f: "RX_RST", 
    0x10: "TXRX_SWITCH",
    0x11: "RXFIFO_OVERFLOW", 
    0x12: "FSTXON",
    0x13: "TX",
    0x14: "TX_END",
    0x15: "RXTX_SWITCH",
    0x16: "TXFIFO_UNDERFLOW"
}





class MainWindow(QMainWindow):
    def sendCommand(self, command, sizeResponse=0):
        if not self.serial_conn or not self.serial_conn.is_open:
            self.closeSerial()
            return None
        try:
            if isinstance(command, int):  
                command = [command]
            elif isinstance(command, bytes):
                command = list(command)
            sizeCommand = len(command)
            packet = bytes([sizeCommand, sizeResponse] + command)
            self.serial_conn.write(packet)
            if sizeResponse > 0:
                response = self.serial_conn.read(sizeResponse)
                return list(response) if response else None
            return None 
        except:
            self.closeSerial()
            return None
    
    def updateListPort(self):
        new_ports = [port.device for port in serial.tools.list_ports.comports()]
        if new_ports == self.last_ports:
            return
        self.ui.cListPort.clear()
        if new_ports:
            self.ui.cListPort.addItems(new_ports)
            self.ui.bConnectDisconnect.setEnabled(True)
        else:
            self.ui.cListPort.addItem("Немає доступних портів")
            self.ui.bConnectDisconnect.setEnabled(False)
        self.last_ports = new_ports

    def openSerial(self):
        selected_port = self.ui.cListPort.currentText()
        if "Немає доступних портів" in selected_port:
            return
        try:
            self.serial_conn = serial.Serial(selected_port, 9600, timeout=10)
            responce = self.sendCommand([0xF1], sizeResponse = 1)
            if responce[0] != 0x14:
                self.serial_conn.close()
                return None
            self.ui.bConnectDisconnect.setText("Відключити")
            self.ui.bConnectDisconnect.clicked.disconnect(self.openSerial)
            self.ui.bConnectDisconnect.clicked.connect(self.closeSerial)
            self.ui.cListPort.setEnabled(False)
            self.timerUpdateListPort.stop()
            self.timerStateMaschine.start()
            self.timerUpdateConfigurationsRegister.start()
            self.timerUpdateStateRegister.start()
        except serial.SerialException as e:
            self.log.append(f"[Помилка] Не вдалося відкрити {selected_port}: {e}")

    def closeSerial(self):
        self.serial_conn.close()
        self.ui.bConnectDisconnect.setText("Підключити")
        self.ui.bConnectDisconnect.clicked.disconnect(self.closeSerial)
        self.ui.bConnectDisconnect.clicked.connect(self.openSerial)
        self.ui.cListPort.setEnabled(True)
        self.timerUpdateListPort.start()
        self.timerStateMaschine.stop()
        self.timerUpdateConfigurationsRegister.stop()
        self.timerUpdateStateRegister.stop()
        self.ui.LStateMachine.setText("Not connected")
    
    def update_state_machine_event(self):
        response = self.sendCommand([0xF5], sizeResponse = 1)
        self.ui.LStateMachine.setText(cc1101StateMachine.get(response[0], "Unknown"))
    
    def updateConfigurationsRegister(self):
        for row in range(self.ui.tConfigurationsRegister.rowCount()):
            item = self.ui.tConfigurationsRegister.item(row, 0)
            if item:
                hex_value = item.text().strip()
                try:
                    dec_value = int(hex_value, 16)
                    response = self.sendCommand([dec_value+0x80], sizeResponse = 1)[0]
                    self.ui.tConfigurationsRegister.setItem(row, 2, QTableWidgetItem(f"{response:#04x}"))
                except ValueError:
                    self.ui.tConfigurationsRegister.setItem(row, 2, QTableWidgetItem("Помилка"))

    def updateStateRegister(self):
        for row in range(self.ui.tStatusRegister.rowCount()):
            item = self.ui.tStatusRegister.item(row, 0)
            if item:
                hex_value = item.text().strip()
                try:
                    dec_value = int(hex_value, 16)
                    response = self.sendCommand([dec_value], sizeResponse = 1)[0]
                    self.ui.tStatusRegister.setItem(row, 2, QTableWidgetItem(f"{response:#04x}"))
                except ValueError:
                    self.ui.tStatusRegister.setItem(row, 2, QTableWidgetItem("Помилка"))

    def writeConfigurationsRegister(self):
        for row in range(self.ui.tConfigurationsRegister.rowCount()):
            itemAddress = self.ui.tConfigurationsRegister.item(row, 0)
            itemValue = self.ui.tConfigurationsRegister.item(row, 3)
            if itemAddress and itemValue:
                address = itemAddress.text()
                value = itemValue.text()
                self.sendCommand([int(address, 16), int(value, 16)])
                   

    def readFIFO(self):
        pass

    def writeFIFO(self):
        hexText = self.ui.plainFIFO.toPlainText()
        hexText = hexText.replace(" ", "").upper()
        if not all(c in "0123456789ABCDEF" for c in hexText.upper()):
            print("Невірний формат шістнадцяткових чисел!")
            return
        
        # Перетворюємо текст в байти
        byteArray = bytearray.fromhex(hexText)
        byteArray.insert(0, 0x7F)
        self.sendCommand(list(byteArray))

    def SRES(self):
        self.sendCommand([0x30])

    def SFSTXON(self):
        self.sendCommand([0x31])

    def SXOFF(self):
        self.sendCommand([0x32])

    def SCAL(self):
        self.sendCommand([0x33])

    def SRX(self):
        self.sendCommand([0x34])

    def STX(self):
        self.sendCommand([0x35])

    def SIDLE(self):
        self.sendCommand([0x36])

    def SWOR(self):
        self.sendCommand([0x38])

    def SPWD(self):
        self.sendCommand([0x39])

    def SFRX(self):
        self.sendCommand([0x3A])

    def SFTX(self):
        self.sendCommand([0x3B])

    def SWORRST(self):
        self.sendCommand([0x3C])

    def SNOP(self):
        self.sendCommand([0x3D])
    
    def plainFIFOTextChanged(self):
        self.ui.plainFIFO.textChanged.disconnect(self.plainFIFOTextChanged)
        hexText = self.ui.plainFIFO.toPlainText().replace(" ", "")
        hexText = re.sub(r'[^0-9A-Fa-f]', '', hexText)
        formattedText = ' '.join([hexText[i:i+2] for i in range(0, len(hexText), 2)])
        self.ui.plainFIFO.setPlainText(formattedText)
        cursor = QTextCursor(self.ui.plainFIFO.document())
        cursor.movePosition(QTextCursor.End)
        self.ui.plainFIFO.setTextCursor(cursor)
        self.ui.plainFIFO.textChanged.connect(self.plainFIFOTextChanged)
    
    def load_from_txt(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Відкрити файл", "", "Текстові файли (*.txt);;Усі файли (*)")
        if not filename:
            return

        with open(filename, "r") as file:
            lines = file.readlines()
        
        config_data = {}
        
        for line in lines:
            address, value = line.strip().split(": ")  # Розділяємо адресу і значення
            config_data[address] = value

        for row in range(self.ui.tConfigurationsRegister.rowCount()):
            item = self.ui.tConfigurationsRegister.item(row, 0)
            if item:
                value = item.text()
                hex_value = config_data.get(value, "")
                self.ui.tConfigurationsRegister.setItem(row, 3, QTableWidgetItem(hex_value))
                



    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #list port
        self.last_ports = list()
        self.updateListPort()
        #FIFO Validator
        self.ui.plainFIFO.textChanged.connect(self.plainFIFOTextChanged)


        #timers
            #listPort
        self.timerUpdateListPort = QTimer(self)
        self.timerUpdateListPort.setInterval(2000)
        self.timerUpdateListPort.timeout.connect(self.updateListPort)
        self.timerUpdateListPort.start()
            #state Machine
        self.timerStateMaschine = QTimer(self)
        self.timerStateMaschine.setInterval(500)
        self.timerStateMaschine.timeout.connect(self.update_state_machine_event)
            #configuration register
        self.timerUpdateConfigurationsRegister = QTimer(self)
        self.timerUpdateConfigurationsRegister.setInterval(2000)
        self.timerUpdateConfigurationsRegister.timeout.connect(self.updateConfigurationsRegister)
            #state register
        self.timerUpdateStateRegister = QTimer(self)
        self.timerUpdateStateRegister.setInterval(500)
        self.timerUpdateStateRegister.timeout.connect(self.updateStateRegister)

        #button listener
        self.ui.bConnectDisconnect.clicked.connect(self.openSerial)
        self.ui.bWriteConfigurationsRegister.clicked.connect(self.writeConfigurationsRegister)
        self.ui.bReadFIFO.clicked.connect(self.readFIFO)
        self.ui.bWriteFIFO.clicked.connect(self.writeFIFO)
        self.ui.bSRES.clicked.connect(self.SRES)
        self.ui.bSFSTXON.clicked.connect(self.SFSTXON)
        self.ui.bSXOFF.clicked.connect(self.SXOFF)
        self.ui.bSCAL.clicked.connect(self.SCAL)
        self.ui.bSRX.clicked.connect(self.SRX)
        self.ui.bSTX.clicked.connect(self.STX)
        self.ui.bSIDLE.clicked.connect(self.SIDLE)
        self.ui.bSWOR.clicked.connect(self.SWOR)
        self.ui.bSPWD.clicked.connect(self.SPWD)
        self.ui.bSFRX.clicked.connect(self.SFRX)
        self.ui.bSFTX.clicked.connect(self.SFTX)
        self.ui.bSWORRST.clicked.connect(self.SWORRST)
        self.ui.bSNOP.clicked.connect(self.SNOP)
        self.ui.bLoadFile.clicked.connect(self.load_from_txt)
        







        
        

        
        
    def open_serial(self):
        """ Відкриття COM-порту """
        selected_port = self.ui.comboBox.currentText()
        if "Немає доступних портів" in selected_port:
            return

        try:
            self.serial_conn = serial.Serial(selected_port, 9600, timeout=10)
            self.ui.pushButton.setText("Зупинити")
            self.ui.pushButton.clicked.connect(self.close_serial)
            
            
            self.timerStateMaschine.start()
            self.timerUpdateConfigRegister.start()
        except serial.SerialException as e:
            self.log.append(f"[Помилка] Не вдалося відкрити {selected_port}: {e}")


    def close_serial(self):
        pass
    
    def update_configuration_register(self):
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item:
                hex_value = item.text().strip()
                try:
                    dec_value = int(hex_value, 16)
                    self.serial_conn.write(bytes([dec_value+0x80]))
                    response = ord(self.serial_conn.read(1))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"{response:#04x}"))
                except ValueError:
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem("Помилка"))
    def perform_task_3(self):
        print("Start 3")
        time.sleep(3)
        print("Stop 3")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
