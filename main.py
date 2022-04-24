# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from pyclbr import Function
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# RANDOMNESS
import random

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# os.environ["QT_SCALE_FACTOR"] = "0.5"

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # POST-SETUP
        if not builtins.is_logged:
            MainFunctions.get_left_menu_btn(self, "btn_login").set_icon(Functions.set_svg_icon("icon_lock.svg"))

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////


        # top_btn_setting = MainFunctions.get_title_bar_btn(self, "btn_top_settings")

        if btn.objectName() == "btn_login":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        if btn.objectName() == "btn_stat":
            if not builtins.is_logged:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Statistics Dashboard")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Access denied. Please login.")
                msgBox.exec()
            else:
                self.ui.left_menu.select_only_one(btn.objectName())
                MainFunctions.set_page(self, self.ui.load_pages.page_2)

        if btn.objectName() == "btn_manage":
            if not builtins.is_logged:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Customers Management")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Access denied. Please login.")
                msgBox.exec()
            else:
                self.ui.left_menu.select_only_one(btn.objectName())
                MainFunctions.set_page(self, self.ui.load_pages.page_3)

        if btn.objectName() == "btn_info" or btn.objectName() == "btn_close_left_column":
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()

                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu = self.ui.left_column.menus.menu_2,
                    title = "About",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )

        if btn.objectName() == "btn_setting" or btn.objectName() == "btn_close_left_column":
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()

                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )
        
        if btn.objectName() == "btn_rate":
            text, ok = QInputDialog().getMultiLineText(
                self, 
                "Feedback",
                "What do you think about this client?", 
                "",
            )

            if ok:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Feedback")
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Thank you for sending! Your opinion will be sent to /dev/null for everyone!")
                msgBox.exec()

        if btn.objectName() == "btn_motd":
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Message of the Day")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(
                random.choice(builtins.motds)
            )
            msgBox.exec()

        # # SETTINGS TITLE BAR
        # if btn.objectName() == "btn_top_settings":
        #     # Toogle Active
        #     if not MainFunctions.right_column_is_visible(self):
        #         btn.set_active(True)

        #         # Show / Hide
        #         MainFunctions.toggle_right_column(self)
        #     else:
        #         btn.set_active(False)

        #         # Show / Hide
        #         MainFunctions.toggle_right_column(self)

        #     # Get Left Menu Btn            
        #     top_settings = MainFunctions.get_left_menu_btn(self, "btn_info")
        #     top_settings.set_active_tab(False)   

        #     # Get Left Menu Btn            
        #     top_settings = MainFunctions.get_left_menu_btn(self, "btn_setting")
        #     top_settings.set_active_tab(False)           

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())