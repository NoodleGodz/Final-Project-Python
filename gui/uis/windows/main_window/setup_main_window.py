# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from cProfile import label
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

import sys

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
        self.userLineEdit.returnPressed.connect(lambda: username_released(self, self.userLineEdit.text(), self.passwordLineEdit.text(), self.ui.load_pages.label_welcome, self.ui.load_pages.label_status))

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
        self.passwordLineEdit.returnPressed.connect(lambda: username_released(self, self.userLineEdit.text(), self.passwordLineEdit.text(), self.ui.load_pages.label_welcome, self.ui.load_pages.label_status))

        self.login_btn = PyPushButton(
            "Login",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )

        self.login_btn.setMinimumHeight(36)

        def username_released(self, username, password, changed_label: QLabel, status_label: QLabel, datetime_label: QLabel):
            if username and password:
                builtins.is_logged = True
                MainFunctions.get_left_menu_btn(self, "btn_login").set_icon(Functions.set_svg_icon("icon_user.svg"))

                MainFunctions.set_page(self, self.ui.load_pages.page_0)
                changed_label.setText("Welcome back, " + username + "!")
                status_label.setText("Last login: " + QDateTime.currentDateTime().toString())
                datetime_label.setText("Today is: " + str(builtins.mm.Today.strftime("%A, %d %B, %Y")))
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Login Panel")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Authentication Failure: The user credentials does not match any accounts on record.")
                msgBox.exec()

        # NO!
        self.login_btn.clicked.connect(lambda: username_released(
            self, 
            self.userLineEdit.text(), 
            self.passwordLineEdit.text(), 
            self.ui.load_pages.label_welcome, 
            self.ui.load_pages.label_status,
            self.ui.load_pages.label_datetime
        ))

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

        self.btn_change_stat.released.connect(lambda: change_stat_panel(self))

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

        self.btn_change_manage.released.connect(lambda: change_manage_panel(self))

        self.btn_new_day = PyPushButton(
            "New day",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_new_day = QIcon(Functions.set_svg_icon("icon_newday.svg"))
        self.btn_new_day.setMinimumHeight(160)
        self.btn_new_day.setIcon(self.icon_new_day)
        self.btn_new_day.setIconSize(QSize(40, 40))
        self.btn_new_day.setFont(QFont("Ubuntu", 30))

        def change_new_day(self, datetime_label: QLabel, chart_layout: QLayout, chart_from_to: QLabel):
            builtins.mm.New_day()

            def stat_chartview():
                stat_series = QBarSeries()

                sample = QBarSet("Energy Usage")
                sample.setColor(QColor(255, 206, 0, 255))
                sum_of_day,date = builtins.mm.Stat_L.Ploting_Usage_Of_All_Clients()
                for i in sum_of_day:
                    sample.append(i)
                stat_series.append(sample)

                chart = QChart()
                chart.addSeries(stat_series)
                chart.setBackgroundBrush(QBrush(QColor(44, 49, 60, 255)))
                chart.setTitleBrush(QBrush(QColor(133, 148, 170, 255)))
                chart.setAnimationOptions(QChart.SeriesAnimations)

                categories = []
                a=0
                for i in date:
                    a+=1
                    categories.append(a)

                axisX = QBarCategoryAxis()
                axisX.append(categories)
                axisX.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
                chart.addAxis(axisX, Qt.AlignBottom)
                stat_series.attachAxis(axisX)
            
                axisY = QValueAxis()
                maxy=(max(sum_of_day)//100 + 2)*100
                axisY.setRange(0, maxy)
                axisY.setTickCount(6)
                axisY.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
                chart.addAxis(axisY, Qt.AlignLeft)
                stat_series.attachAxis(axisY)

                chart.legend().setVisible(True)
                chart.legend().setAlignment(Qt.AlignBottom)
                chart.legend().setLabelBrush(QBrush(QColor(133, 148, 170, 255)))

                chartView = QChartView(chart);
                chartView.setRenderHint(QPainter.Antialiasing)
                return chartView
            
            
            chart_from_to.setText(
                "From" + 
                builtins.mm.Stat_L.Start_Point.strftime(" %d %B, %Y ") + 
                "To" + 
                builtins.mm.Stat_L.End_Point.strftime(" %d %B, %Y ")
            )
            old_chart = chart_layout.takeAt(0).widget()
            chart_layout.removeWidget(old_chart)
            old_chart.deleteLater()
            chart_layout.addWidget(stat_chartview())
            datetime_label.setText("Today is: " + str(builtins.mm.Today.strftime("%A, %d %B, %Y")))


        self.btn_new_day.released.connect(lambda: change_new_day(
            self, 
            self.ui.load_pages.label_datetime, 
            self.ui.load_pages.layout_linechart,
            self.ui.load_pages.label_from_to
        ))

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

        self.btn_change_logout.released.connect(lambda: change_logout_panel(self, passwdbox=self.passwordLineEdit))

        self.ui.load_pages.layout_frame_btn_stat.addWidget(self.btn_change_stat)
        self.ui.load_pages.layout_frame_btn_manage.addWidget(self.btn_change_manage)
        self.ui.load_pages.layout_frame_btn_newday.addWidget(self.btn_new_day)
        self.ui.load_pages.layout_frame_btn_logout.addWidget(self.btn_change_logout)

        # SET STAT PANEL
        # ///////////////////////////////////////////////////////////////
        #

        self.ui.load_pages.label_from_to.setText(
            "From" + 
            builtins.mm.Stat_L.Start_Point.strftime(" %d %B, %Y ") + 
            "To" + 
            builtins.mm.Stat_L.End_Point.strftime(" %d %B, %Y ")
        )

        def stat_chartview():
            stat_series = QBarSeries()
            sample = QBarSet("Energy Usage")
            sample.setColor(QColor(255, 206, 0, 255))
            sum_of_day,date = builtins.mm.Stat_L.Ploting_Usage_Of_All_Clients()
            for i in sum_of_day:
                sample.append(i)
            stat_series.append(sample)

            chart = QChart()
            chart.addSeries(stat_series)
            chart.setBackgroundBrush(QBrush(QColor(44, 49, 60, 255)))
            chart.setTitleBrush(QBrush(QColor(133, 148, 170, 255)))
            chart.setAnimationOptions(QChart.SeriesAnimations)

            categories = []
            a=0
            for i in date:
                a+=1
                categories.append(a)

            axisX = QBarCategoryAxis()
            axisX.append(categories)
            axisX.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
            chart.addAxis(axisX, Qt.AlignBottom)
            stat_series.attachAxis(axisX)
            
            axisY = QValueAxis()
            maxy=(max(sum_of_day)//100 + 2)*100
            axisY.setRange(0, maxy)
            axisY.setTickCount(6)
            axisY.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
            chart.addAxis(axisY, Qt.AlignLeft)
            stat_series.attachAxis(axisY)

            chart.legend().setVisible(True)
            chart.legend().setAlignment(Qt.AlignBottom)
            chart.legend().setLabelBrush(QBrush(QColor(133, 148, 170, 255)))

            chartView = QChartView(chart);
            chartView.setRenderHint(QPainter.Antialiasing)
            return chartView
                
        self.ui.load_pages.layout_linechart.addWidget(stat_chartview())
        chart = self.ui.load_pages.layout_linechart.takeAt(0).widget()
        self.ui.load_pages.layout_linechart.removeWidget(chart)
        chart.deleteLater()
        self.ui.load_pages.layout_linechart.addWidget(stat_chartview())

        self.btn_export_price = PyPushButton(
            "Export Price",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_export_price = QIcon(Functions.set_svg_icon("icon_export_price.svg"))
        self.btn_export_price.setMinimumHeight(100)
        self.btn_export_price.setIcon(self.icon_export_price)
        self.btn_export_price.setIconSize(QSize(40, 40))
        self.btn_export_price.setFont(QFont("Ubuntu", 30))
        
        def change_export_price(self):
           
            path =  builtins.mm.Stat_L.Price_List_To_Excel()
            QMessageBox.information(self, "Export Price", "Success: Export Price saved to \n" + path, QMessageBox.Ok)

        self.btn_export_price.released.connect(lambda: change_export_price(self))

        self.btn_export_usage = PyPushButton(
            "Export Usage",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_export_usage = QIcon(Functions.set_svg_icon("icon_export_usage.svg"))
        self.btn_export_usage.setMinimumHeight(100)
        self.btn_export_usage.setIcon(self.icon_export_usage)
        self.btn_export_usage.setIconSize(QSize(40, 40))
        self.btn_export_usage.setFont(QFont("Ubuntu", 30))
        
        def change_export_usage(self):
            path = builtins.mm.Stat_L.Export_Elec_Usage_To_Excel()
            QMessageBox.information(self, "Export Usage", "Success: Export Usage saved to \n" + path, QMessageBox.Ok)

        self.btn_export_usage.released.connect(lambda: change_export_usage(self))

        self.btn_flush = PyPushButton(
            "Flush Data",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_flush = QIcon(Functions.set_svg_icon("icon_flush.svg"))
        self.btn_flush.setMinimumHeight(100)
        self.btn_flush.setIcon(self.icon_flush)
        self.btn_flush.setIconSize(QSize(40, 40))
        self.btn_flush.setFont(QFont("Ubuntu", 30))
        
        def change_flush(self,chart_layout: QLayout, chart_from_to: QLabel):
            reply = QMessageBox.warning(self, "Flush Data", "Are you sure to flush all data?\nThis action is irreversible!", QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                builtins.mm.Stat_L.Flush()
                def stat_chartview():
                    stat_series = QBarSeries()

                    sample = QBarSet("Energy Usage")
                    sample.setColor(QColor(255, 206, 0, 255))
                    sum_of_day,date = builtins.mm.Stat_L.Ploting_Usage_Of_All_Clients()
                    if len(sum_of_day)==0: sum_of_day.append(0)
                    if len(date)==0: date.append(0)

                    for i in sum_of_day:
                        sample.append(i)
                    stat_series.append(sample)

                    chart = QChart()
                    chart.addSeries(stat_series)
                    chart.setBackgroundBrush(QBrush(QColor(44, 49, 60, 255)))
                    chart.setTitleBrush(QBrush(QColor(133, 148, 170, 255)))
                    chart.setAnimationOptions(QChart.SeriesAnimations)

                    categories = []
                    a=0
                    for i in date:
                        a+=1
                        categories.append(a)

                    axisX = QBarCategoryAxis()
                    axisX.append(categories)
                    axisX.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
                    chart.addAxis(axisX, Qt.AlignBottom)
                    stat_series.attachAxis(axisX)

                    axisY = QValueAxis()
                    maxy=(max(sum_of_day)//100 + 2)*100
                    axisY.setRange(0, maxy)
                    axisY.setTickCount(6)
                    axisY.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
                    chart.addAxis(axisY, Qt.AlignLeft)
                    stat_series.attachAxis(axisY)

                    chart.legend().setVisible(True)
                    chart.legend().setAlignment(Qt.AlignBottom)
                    chart.legend().setLabelBrush(QBrush(QColor(133, 148, 170, 255)))

                    chartView = QChartView(chart);
                    chartView.setRenderHint(QPainter.Antialiasing)
                    return chartView


                chart_from_to.setText(
                    "Energy Data is empty"
                )
                old_chart = chart_layout.takeAt(0).widget()
                chart_layout.removeWidget(old_chart)
                old_chart.deleteLater()
                chart_layout.addWidget(stat_chartview())


        self.btn_flush.released.connect(lambda: change_flush(
            self, 
            self.ui.load_pages.layout_linechart,
            self.ui.load_pages.label_from_to
        ))

        self.btn_load_version = PyPushButton(
            "Load Version",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_load_version = QIcon(Functions.set_svg_icon("icon_load.svg"))
        self.btn_load_version.setMinimumHeight(100)
        self.btn_load_version.setIcon(self.icon_load_version)
        self.btn_load_version.setIconSize(QSize(40, 40))
        self.btn_load_version.setFont(QFont("Ubuntu", 30))
        
        def change_load_version(self,chart_layout: QLayout, chart_from_to: QLabel):
            load_dialog = QFileDialog()
            load_dialog.setFileMode(QFileDialog.AnyFile)
            load_dialog.setNameFilter("ECMP object file (*.obj)")
            load_dialog.setViewMode(QFileDialog.Detail)
            if load_dialog.exec():
                filename = load_dialog.selectedFiles()
                path = filename[0]
                print(path)
                builtins.mm.Stat_L.Save_SL()
                builtins.mm.Stat_L.Load_Previous_Version(path)
                def stat_chartview():
                        stat_series = QBarSeries()

                        sample = QBarSet("Energy Usage")
                        sample.setColor(QColor(255, 206, 0, 255))
                        sum_of_day,date = builtins.mm.Stat_L.Ploting_Usage_Of_All_Clients()
                        for i in sum_of_day:
                            sample.append(i)
                        stat_series.append(sample)

                        chart = QChart()
                        chart.addSeries(stat_series)
                        chart.setBackgroundBrush(QBrush(QColor(44, 49, 60, 255)))
                        chart.setTitleBrush(QBrush(QColor(133, 148, 170, 255)))
                        chart.setAnimationOptions(QChart.SeriesAnimations)

                        categories = []
                        a=0
                        for i in date:
                            a+=1
                            categories.append(a)

                        axisX = QBarCategoryAxis()
                        axisX.append(categories)
                        axisX.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
                        chart.addAxis(axisX, Qt.AlignBottom)
                        stat_series.attachAxis(axisX)
                    
                        axisY = QValueAxis()
                        maxy=(max(sum_of_day)//100 + 2)*100
                        axisY.setRange(0, maxy)
                        axisY.setTickCount(6)
                        axisY.setLabelsBrush(QBrush(QColor(133, 148, 170, 255)))
                        chart.addAxis(axisY, Qt.AlignLeft)
                        stat_series.attachAxis(axisY)

                        chart.legend().setVisible(True)
                        chart.legend().setAlignment(Qt.AlignBottom)
                        chart.legend().setLabelBrush(QBrush(QColor(133, 148, 170, 255)))

                        chartView = QChartView(chart);
                        chartView.setRenderHint(QPainter.Antialiasing)
                        return chartView
                
                chart_from_to.setText(
                    "From" + 
                    builtins.mm.Stat_L.Start_Point.strftime(" %d %B, %Y ") + 
                    "To" + 
                    builtins.mm.Stat_L.End_Point.strftime(" %d %B, %Y ")
                )
                old_chart = chart_layout.takeAt(0).widget()
                chart_layout.removeWidget(old_chart)
                old_chart.deleteLater()
                chart_layout.addWidget(stat_chartview())
                #builtins.mm.Stat_L.Load_SL()


        self.btn_load_version.released.connect(lambda: change_load_version(self, 
            self.ui.load_pages.layout_linechart,
            self.ui.load_pages.label_from_to
        ))

        self.ui.load_pages.layout_frame_btn_export_price.addWidget(self.btn_export_price)
        self.ui.load_pages.layout_frame_btn_export_usage.addWidget(self.btn_export_usage)
        self.ui.load_pages.layout_frame_btn_flush.addWidget(self.btn_flush)
        self.ui.load_pages.layout_frame_btn_load_version.addWidget(self.btn_load_version)

        # SET CUSTOMER MANAGE - 
        # ///////////////////////////////////////////////////////////////

        self.btn_add_cstmr = PyPushButton(
            " Add New Customer",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_add_cstmr = QIcon(Functions.set_svg_icon("icon_add_user.svg"))
        self.btn_add_cstmr.setMinimumHeight(128)
        self.btn_add_cstmr.setIcon(self.icon_add_cstmr)
        self.btn_add_cstmr.setIconSize(QSize(40, 40))
        self.btn_add_cstmr.setFont(QFont("Ubuntu", 30))

        def add_cstmr(self):
            c_id, ok1 = QInputDialog.getText(
                self,
                "Add New Customer",
                "Type ID of customer:",
            )

            if not ok1 or not c_id:
                return

            c_Name,ok2 = QInputDialog.getText(
                self,
                "Add New Customer",
                "Type Name of customer:",
            )
            if not ok2 or not c_Name:
                return

            c_Address,ok3 = QInputDialog.getText(
                self,
                "Add New Customer",
                "Type Address of customer:",
            )
            if not ok3 or not c_Address:
                return

            c_Info, ok4 = QInputDialog.getText(
                self,
                "Add New Customer",
                "Type Info of customer:",
            )
            if not ok4 or not c_Info:
                return

            mode_E=['0','1','2','3','4','5']
            c_EM, ok5 = QInputDialog.getItem(
                self,
                "Add New Customer",
                "Type Electric_Mode of customer:", 
                mode_E,
                0,
                False
            )
            if not ok5:
                return

            c_status=builtins.mm.Client_L.CreateNewClient(c_id,c_Name,c_Address,c_Info,c_EM)
            if c_status:
                QMessageBox.information(
                    self,
                    "Add New Customer",
                    "Success: " + str(c_id) + " - " + str(c_Name) + " has been added to the record."
                )
            else:
                QMessageBox.critical(
                    self,
                    "Add New Customer",
                    "Conflict: There is already a customer with ID " + str(c_id) + ", terminating"
                )
            
            change_listWidget(self, self.customer_lineedit.text(), self.ui.load_pages.listWidget_cstmr, self.ui.load_pages.label_match_text)

        self.btn_add_cstmr.clicked.connect(lambda: add_cstmr(self))
        self.ui.load_pages.layout_btn_add_cstmr.addWidget(self.btn_add_cstmr)

        self.customer_lineedit = PyLineEdit(
            "",
            "Type here to search...",
            8,
            2,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_four"],
            self.themes["app_color"]["bg_three"],
            self.themes["app_color"]["bg_one"],
            self.themes["app_color"]["context_color"]
        )

        def change_listWidget(self, query: str, lw: QListWidget, match_text: QLabel):

            lw.clear()
            query_match=builtins.mm.Client_L.FindClientsListbyInput(query)
            for i in query_match:
                labelname=i['id']+' / '+i['Client_Object'].Owner_Name

                item = QListWidgetItem()
                item.setText(labelname)

                lw.addItem(item)
            
            match_text.setText(str(len(query_match)) + " match(es) found, double-click to open Detailed View")
        
        self.customer_lineedit.setMinimumHeight(36)
        self.customer_lineedit.textChanged.connect(lambda: change_listWidget(self, self.customer_lineedit.text(), self.ui.load_pages.listWidget_cstmr, self.ui.load_pages.label_match_text))

        change_listWidget(self, "", self.ui.load_pages.listWidget_cstmr, self.ui.load_pages.label_match_text)

        self.ui.load_pages.layout_frame_labeledit_search.addWidget(self.customer_lineedit)

        def change_double_clicked(item):
            idchoose=item.text().split()[0]
            builtins.mm.Client_L.SelectClientbyid(idchoose)

        def change_cstmr_page(self):
            MainFunctions.set_page(self, self.ui.load_pages.page_4)

        self.ui.load_pages.listWidget_cstmr.itemDoubleClicked.connect(change_double_clicked)
        self.ui.load_pages.listWidget_cstmr.itemDoubleClicked.connect(lambda: change_cstmr_page(self))

        self.logo_cstmr = QSvgWidget(Functions.set_svg_icon("icon_user.svg"))
        self.logo_cstmr.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        self.ui.load_pages.layout_icon_template.addWidget(self.logo_cstmr, Qt.AlignCenter, Qt.AlignCenter)

        # SET CUSTOMER PAGE
        # ///////////////////////////////////////////////////////////

        self.btn_cstmr_back = PyPushButton(
            "Back",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_cstmr_back = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.btn_cstmr_back.setMinimumHeight(35)
        self.btn_cstmr_back.setIcon(self.icon_cstmr_back)
        self.btn_cstmr_back.setIconSize(QSize(20, 20))
        self.btn_cstmr_back.setFont(QFont("Ubuntu", 12))

        def change_cstmr_search(self):
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        self.btn_cstmr_back.clicked.connect(lambda: change_cstmr_search(self))

        self.ui.load_pages.layout_frame_cstmr_back.addWidget(self.btn_cstmr_back)

        self.btn_view_profile = PyPushButton(
            "Back",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.btn_view_profile.setMinimumHeight(30)
        self.btn_view_profile.setFont(QFont("Ubuntu", 12))

        def change_view_edit_profile(self, c_id, name, address, info, c_id_label : QLineEdit, name_label : QLineEdit, address_label : QLineEdit, info_label : QLineEdit):
            c_id_label.setText(c_id)
            name_label.setText(name)
            address_label.setText(address)
            info_label.setText(info_label)

            if not MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)

        self.btn_view_profile.clicked.connect(lambda: change_view_edit_profile(
            self,
            builtins.mm.Client_L.SelectedClient.Contract_ID,
            builtins.mm.Client_L.SelectedClient.Owner_Name,
            builtins.mm.Client_L.SelectedClient.Address,
            builtins.mm.Client_L.SelectedClient.Info,
            self.customer_info_id,
            self.customer_info_name,
            self.customer_info_address,
            self.customer_info_info,
        ))
        self.ui.load_pages.layout_frame_view_edit_profile.addWidget(self.btn_view_profile)

        # SET CUSTOMER INFO
        # ///////////////////////////////////////////////////////////////

        self.ui.right_column.layout_cstmr_image_right.addWidget(self.logo_cstmr, Qt.AlignCenter, Qt.AlignCenter)

        self.btn_right_back = PyPushButton(
            "Back",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.icon_right_back = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.btn_right_back.setMinimumHeight(35)
        self.btn_right_back.setIcon(self.icon_cstmr_back)
        self.btn_right_back.setIconSize(QSize(20, 20))
        self.btn_right_back.setFont(QFont("Ubuntu", 12))

        def change_right_back(self):
            MainFunctions.toggle_right_column(self)

        self.btn_right_back.clicked.connect(lambda: change_right_back(self))
        self.ui.right_column.layout_cstmr_back.addWidget(self.btn_right_back)

        self.customer_info_name = PyLineEdit(
            "",
            "Empty...",
            8,
            2,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_four"],
            self.themes["app_color"]["bg_three"],
            self.themes["app_color"]["bg_one"],
            self.themes["app_color"]["context_color"]
        )
        self.customer_info_name.setMinimumHeight(30)

        self.customer_info_id = PyLineEdit(
            "",
            "Empty...",
            8,
            2,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_four"],
            self.themes["app_color"]["bg_three"],
            self.themes["app_color"]["bg_one"],
            self.themes["app_color"]["context_color"]
        )
        self.customer_info_id.setMinimumHeight(30)

        self.customer_info_address = PyLineEdit(
            "",
            "Empty...",
            8,
            2,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_four"],
            self.themes["app_color"]["bg_three"],
            self.themes["app_color"]["bg_one"],
            self.themes["app_color"]["context_color"]
        )
        self.customer_info_address.setMinimumHeight(30)

        self.customer_info_info = PyLineEdit(
            "",
            "Empty...",
            8,
            2,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_four"],
            self.themes["app_color"]["bg_three"],
            self.themes["app_color"]["bg_one"],
            self.themes["app_color"]["context_color"]
        )
        self.customer_info_info.setMinimumHeight(30)

        self.ui.right_column.layout_cstmr_name_input.addWidget(self.customer_info_name)
        self.ui.right_column.layout_cstmr_id_input.addWidget(self.customer_info_id)
        self.ui.right_column.layout_cstmr_address_input.addWidget(self.customer_info_address)
        self.ui.right_column.layout_cstmr_info_input.addWidget(self.customer_info_info)

        self.btn_view_edit_profile = PyPushButton(
            "Edit...",
            8,
            self.themes["app_color"]["text_foreground"],
            self.themes["app_color"]["dark_one"],
            self.themes["app_color"]["dark_three"],
            self.themes["app_color"]["dark_four"]
        )
        self.btn_view_edit_profile.setMinimumHeight(36)
        self.btn_view_edit_profile.setFont(QFont("Ubuntu", 12))

        def change_edit_profile(self):
            pass

        self.btn_view_edit_profile.clicked.connect(lambda: change_edit_profile(self))

        self.ui.right_column.layout_cstmr_btn_edit.addWidget(self.btn_view_edit_profile)

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
