# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_user.svg",
            "btn_id" : "btn_login",
            "btn_text" : "Login Page",
            "btn_tooltip" : "Login Page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_insights.svg",
            "btn_id" : "btn_stat",
            "btn_text" : "Statistics Dashboard",
            "btn_tooltip" : "Statistics Dashboard",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_business.svg",
            "btn_id" : "btn_manage",
            "btn_text" : "Customers Management",
            "btn_tooltip" : "Customers Management",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "About",
            "btn_tooltip" : "About",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_setting",
            "btn_text" : "Settings",
            "btn_tooltip" : "Settings",
            "show_top" : False,
            "is_active" : False
        },
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_star_rate.svg",
            "btn_id" : "btn_rate",
            "btn_tooltip" : "User Feedback",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_motd.svg",
            "btn_id" : "btn_motd",
            "btn_tooltip" : "Message of the Day",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # SET LOGIN PANEL
        # ///////////////////////////////////////////////////////////////
        
        self.logo = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.logo.renderer().setAspectRatioMode(Qt.KeepAspectRatio)
        self.ui.load_pages.frame_logo.addWidget(self.logo, Qt.AlignCenter, Qt.AlignBottom)

        self.userLineEdit = PyLineEdit(
            "",
            "Username",
            8,
            2,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_four"],
            self.themes["app_color"]["bg_three"],
            self.themes["app_color"]["bg_one"],
            self.themes["app_color"]["context_color"]
        )

        self.userLineEdit.setMinimumHeight(36)
        self.userLineEdit.returnPressed.connect(lambda: username_clicked(self, self.userLineEdit.text(), self.passwordLineEdit.text(), self.ui.load_pages.label_welcome, self.ui.load_pages.label_status))

        self.passwordLineEdit = PyLineEdit(
            "",
            "Password",
            8,
            2,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_four"],
            self.themes["app_color"]["bg_three"],
            self.themes["app_color"]["bg_one"],
            self.themes["app_color"]["context_color"]
        )

        self.passwordLineEdit.setMinimumHeight(36)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setInputMethodHints(Qt.ImhHiddenText | Qt.ImhNoPredictiveText | Qt.ImhNoAutoUppercase);
        self.passwordLineEdit.returnPressed.connect(lambda: username_clicked(self, self.userLineEdit.text(), self.passwordLineEdit.text(), self.ui.load_pages.label_welcome, self.ui.load_pages.label_status))

        self.login_btn = PyPushButton(
            "Login",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )

        self.login_btn.setMinimumHeight(36)

        def username_clicked(self, username, password, changed_label: QLabel, status_label: QLabel):
            if username and password:
                builtins.is_logged = True
                MainFunctions.get_left_menu_btn(self, "btn_login").set_icon(Functions.set_svg_icon("icon_user.svg"))

                MainFunctions.set_page(self, self.ui.load_pages.page_0)
                changed_label.setText("Welcome back, " + username + "!")
                status_label.setText("Last login: " + QDateTime.currentDateTime().toString())
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Login Panel")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Authentication Failure: The user credentials does not match any accounts on record.")
                msgBox.exec()

        # NO!
        self.login_btn.clicked.connect(lambda: username_clicked(self, self.userLineEdit.text(), self.passwordLineEdit.text(), self.ui.load_pages.label_welcome, self.ui.load_pages.label_status))

        self.ui.load_pages.layout_username.addWidget(self.userLineEdit)
        self.ui.load_pages.layout_password.addWidget(self.passwordLineEdit)
        self.ui.load_pages.layout_login.addWidget(self.login_btn)

        # SET LOGGED PANEL
        # ///////////////////////////////////////////////////////////////

        self.btn_change_stat = PyPushButton(
            "Statistic Dashboard",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_stat = QIcon(Functions.set_svg_icon("icon_insights.svg"))
        self.btn_change_stat.setMinimumHeight(160)
        self.btn_change_stat.setIcon(self.icon_stat)
        self.btn_change_stat.setIconSize(QSize(40, 40))
        self.btn_change_stat.setFont(QFont("Ubuntu", 30))

        def change_stat_panel(self):
            self.ui.left_menu.select_only_one("btn_stat")
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        self.btn_change_stat.clicked.connect(lambda: change_stat_panel(self))

        self.btn_change_manage = PyPushButton(
            "Customers Management",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_manage = QIcon(Functions.set_svg_icon("icon_business.svg"))
        self.btn_change_manage.setMinimumHeight(160)
        self.btn_change_manage.setIcon(self.icon_manage)
        self.btn_change_manage.setIconSize(QSize(40, 40))
        self.btn_change_manage.setFont(QFont("Ubuntu", 30))

        def change_manage_panel(self):
            self.ui.left_menu.select_only_one("btn_manage")
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        self.btn_change_manage.clicked.connect(lambda: change_manage_panel(self))

        self.btn_change_logout = PyPushButton(
            "Logout",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_logout = QIcon(Functions.set_svg_icon("icon_logout.svg"))
        self.btn_change_logout.setMinimumHeight(160)
        self.btn_change_logout.setIcon(self.icon_logout)
        self.btn_change_logout.setIconSize(QSize(40, 40))
        self.btn_change_logout.setFont(QFont("Ubuntu", 30))

        def change_logout_panel(self, passwdbox: QLineEdit = None):
            reply = QMessageBox.question(self, "Logout", "Are you sure you want to logout?", QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                builtins.is_logged = False
                passwdbox.clear()
                passwdbox.setFocus()
                MainFunctions.get_left_menu_btn(self, "btn_login").set_icon(Functions.set_svg_icon("icon_lock.svg"))
                self.ui.left_menu.select_only_one("btn_login")
                MainFunctions.set_page(self, self.ui.load_pages.page_1)

        self.btn_change_logout.clicked.connect(lambda: change_logout_panel(self, passwdbox=self.passwordLineEdit))

        self.ui.load_pages.layout_frame_btn_stat.addWidget(self.btn_change_stat)
        self.ui.load_pages.layout_frame_btn_manage.addWidget(self.btn_change_manage)
        self.ui.load_pages.layout_frame_btn_logout.addWidget(self.btn_change_logout)

        # SET STAT PANEL
        # ///////////////////////////////////////////////////////////////

        # SET CUSTOMER MANAGE
        # ///////////////////////////////////////////////////////////////

        # SET CUSTOMER INFO
        # ///////////////////////////////////////////////////////////////

        # SET SETTINGS MENU
        # ///////////////////////////////////////////////////////////////

        self.lable_motd = QLabel("Show MOTD at startup", self)

        self.toggle_motd = PyToggle(
            50,
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["icon_color"],
            self.themes["app_color"]["context_color"],
        )

        self.ui.left_column.menus.layout_motd.addWidget(self.lable_motd, Qt.AlignCenter, Qt.AlignCenter)
        self.ui.left_column.menus.layout_motd.addStretch(9)
        self.ui.left_column.menus.layout_motd.addWidget(self.toggle_motd, Qt.AlignCenter, Qt.AlignCenter)
        self.ui.left_column.menus.layout_motd.addStretch(1)

        # SET SETTINGS MENU
        # //////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    # BEGIN OF EVENTS HANDLING FOR CUSTOM WIDGETS
    # This is the place for main pages to handle data (MainFunctions included)
    # ////////////////////////////////////////////////////////////////
