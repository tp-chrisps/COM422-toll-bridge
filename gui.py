from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QListWidget, QComboBox, \
    QVBoxLayout, QHBoxLayout, QWidget
import sys
import traceback

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bridge = None
        self.setMinimumSize(600, 600)
        self.setWindowTitle("Toll Bridge")

        self.titleLabel = QLabel("Toll Bridge")

        self.sizeLabel = QLabel("Toll Bridge Max Size")
        self.sizeLineEdit = QLineEdit()
        self.size = QVBoxLayout()
        self.size.addWidget(self.sizeLabel)
        self.size.addWidget(self.sizeLineEdit)

        self.createBridgeButton = QPushButton("Create Bridge")
        self.destroyBridgeButton = QPushButton("Destroy Bridge")

        self.BridgeList = QListWidget()

        self.vehicle_type = QComboBox()
        self.vehicle_type.addItems(["Car", "Motorbike", "Lorry"])

        self.vehicle_regLabel = QLabel("Vehicle Reg")
        self.vehicle_regLineEdit = QLineEdit()
        self.vehicle_reg = QVBoxLayout()
        self.vehicle_reg.addWidget(self.vehicle_regLabel)
        self.vehicle_reg.addWidget(self.vehicle_regLineEdit)
        self.vehicle_weightLabel = QLabel("Vehicle Weight")
        self.vehicle_weightLineEdit = QLineEdit()
        self.vehicle_weight = QVBoxLayout()
        self.vehicle_weight.addWidget(self.vehicle_weightLabel)
        self.vehicle_weight.addWidget(self.vehicle_weightLineEdit)


        self.addVehicleButton = QPushButton("Add Vehicle")
        self.removeVehicleButton = QPushButton("Remove Vehicle")

        self.removeCarReg = QLineEdit()
        self.removeCarReg.setPlaceholderText("Reg")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.titleLabel)
        self.verticalLayout.addWidget(self.BridgeList)
        self.bridgeLayout = QHBoxLayout()
        self.bridgeLayout.addLayout(self.size)
        self.bridgeLayout.addWidget(self.createBridgeButton)
        self.bridgeLayout.addWidget(self.destroyBridgeButton)
        self.vehicleLayout = QHBoxLayout()
        self.vehicleLayout.addWidget(self.vehicle_type)
        self.vehicleLayout.addLayout(self.vehicle_reg)
        self.vehicleLayout.addLayout(self.vehicle_weight)
        self.verticalLayout.addLayout(self.bridgeLayout)
        self.verticalLayout.addLayout(self.vehicleLayout)
        self.buttonlayout = QHBoxLayout()
        self.buttonlayout.addWidget(self.removeCarReg)
        self.buttonlayout.addWidget(self.addVehicleButton)
        self.buttonlayout.addWidget(self.removeVehicleButton)
        self.verticalLayout.addLayout(self.buttonlayout)

        self.widget = QWidget()
        self.widget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.widget)

        self.createBridgeButton.clicked.connect(self.createBridge)
        self.destroyBridgeButton.clicked.connect(self.destroyBridge)
        self.addVehicleButton.clicked.connect(self.addVehicle)



    def createBridge(self):
        from bridge import Bridge
        if self.bridge is None:
            size = int(self.sizeLineEdit.text())
            self.bridge = Bridge(size)
            self.sizeLineEdit.clear()

    def destroyBridge(self):
        self.bridge = None

    def addVehicle(self):
        if self.bridge is None:
            return
        vehicle_type = self.vehicle_type.currentText()
        weight = int(self.vehicle_weightLineEdit.text())
        reg = self.vehicle_regLineEdit.text()
        if vehicle_type == "Car":
            from cars import Cars
            car = Cars(reg, weight)
            self.bridge.addVehicle(car)
        elif vehicle_type == "Motorbike":
            from motorbikes import Motorbike
            motorbike = Motorbike(reg, weight)
            self.bridge.addVehicle(motorbike)
        else:
            from lorry import Lorry
            lorry = Lorry(reg, weight)
            self.bridge.addVehicle(lorry)
        self.updateBridge()

    def removeVehicle(self):
        if self.bridge is None:
            return
        reg = self.removeVehicleButton.text()
        self.bridge.removeVehicle(reg)
        self.updateBridge()

    def updateBridge(self):
        if self.bridge is None:
            return
        self.BridgeList.clear()
        for vehicle in self.bridge.vehicle_list:
            self.BridgeList.addItem(f"vehicle type: {vehicle.__class__.__name__} reg: {vehicle.reg} weight: {vehicle.weight}")

def run_gui() -> None:
    def exception_hook(exc_type, exc_value, exc_tb):
        traceback.print_exception(exc_type, exc_value, exc_tb)
        sys.exit(1)

    sys.excepthook = exception_hook
    main_window = MainWindow()
    main_window.show()
    app.exec()

run_gui()