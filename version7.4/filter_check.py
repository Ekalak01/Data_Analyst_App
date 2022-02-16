import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class HeaderView(QtWidgets.QHeaderView):
    checked = QtCore.pyqtSignal(bool)

    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self._checkable_column = -1
        self._state = False
        self._column_down = -1

    @property
    def checkable_column(self):
        return self._checkable_column

    @checkable_column.setter
    def checkable_column(self, c):
        self._checkable_column = c

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, c):
        if self.checkable_column == -1:
            return
        self._state = c
        self.checked.emit(c)
        self.updateSection(self.checkable_column)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super().paintSection(painter, rect, logicalIndex)
        painter.restore()
        if logicalIndex != self.checkable_column:
            return

        opt = QtWidgets.QStyleOptionButton()

        checkbox_rect = self.style().subElementRect(
            QtWidgets.QStyle.SE_CheckBoxIndicator, opt, None
        )
        checkbox_rect.moveCenter(rect.center())
        opt.rect = checkbox_rect
        opt.state = QtWidgets.QStyle.State_Enabled | QtWidgets.QStyle.State_Active
        if logicalIndex == self._column_down:
            opt.state |= QtWidgets.QStyle.State_Sunken
        opt.state |= (
            QtWidgets.QStyle.State_On if self.state else QtWidgets.QStyle.State_Off
        )
        self.style().drawPrimitive(QtWidgets.QStyle.PE_IndicatorCheckBox, opt, painter)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        li = self.logicalIndexAt(event.pos())
        self._column_down = li
        self.updateSection(li)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        li = self.logicalIndexAt(event.pos())
        self._column_down = -1
        if li == self.checkable_column:
            self.state = not self.state

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.model = QtGui.QStandardItemModel(0, 2, self)

        self.model.setHorizontalHeaderLabels(["", "First Name"])

        for state, firstname  in (
            (True, "Larry"),
            (True, "Steve"),
            (True, "Steve"),
            (True, "Bill"),
        ):
            it_state = QtGui.QStandardItem()
            it_state.setEditable(False)
            it_state.setCheckable(True)
            it_state.setCheckState(QtCore.Qt.Checked if state else QtCore.Qt.UnChecked)
            it_firstname = QtGui.QStandardItem(firstname)
            self.model.appendRow([it_state, it_firstname,])

        self.view = QtWidgets.QTableView(
            showGrid=False, selectionBehavior=QtWidgets.QAbstractItemView.SelectRows
        )
        self.view.setModel(self.model)
        headerview = HeaderView(QtCore.Qt.Horizontal, self.view)
        headerview.checkable_column = 0
        headerview.checked.connect(self.change_state_of_model)
        self.view.setHorizontalHeader(headerview)

        self.view.verticalHeader().hide()

        self.view.horizontalHeader().setMinimumSectionSize(0)
        self.view.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents
        )
        self.view.horizontalHeader().setStretchLastSection(True)

        self.box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok
            | QtWidgets.QDialogButtonBox.Cancel
            | QtWidgets.QDialogButtonBox.NoButton
            | QtWidgets.QDialogButtonBox.Help,
            QtCore.Qt.Vertical,
        )

        hlay = QtWidgets.QHBoxLayout(self)
        hlay.addWidget(self.view)
        hlay.addWidget(self.box)

        self.box.accepted.connect(self.accept)
        self.box.rejected.connect(self.reject)
        self.box.helpRequested.connect(self.on_helpRequested)

        self.resize(300, 140)

    @QtCore.pyqtSlot()
    def on_helpRequested(self):
        QtWidgets.QMessageBox.aboutQt(self)

    @QtCore.pyqtSlot(bool)
    def change_state_of_model(self, state):
        for i in range(self.model.rowCount()):
            it = self.model.item(i)
            if it is not None:
                it.setCheckState(QtCore.Qt.Checked if state else QtCore.Qt.Unchecked)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = Dialog()
    w.show()

    sys.exit(app.exec_())