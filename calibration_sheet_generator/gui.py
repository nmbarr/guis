import customtkinter as ctk
from gui_classes.header_class import HeaderBox
from gui_classes.button_class import GUIButton

class CalibrationSheetGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the appearance mode and theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Set GUI window properties
        self.title("Calibration Sheet Generator")

        self.window_width = 1280
        self.window_height = 720
        self.geometry(f"{self.window_width}x{self.window_height}")

        self.center_window()
        self.resizable(False, False)

        # Setup GUI layout
        self.setup_layout()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int((screen_height / 2) - (self.window_height / 2))
        position_right = int((screen_width / 2) - (self.window_width / 2))

        self.geometry(f"{self.window_width}x{self.window_height}+{position_right}+{position_top}")
    
    def setup_layout(self):
        # Configure grid rows and columns
        self.grid_rowconfigure(0, weight=10, uniform="rows")  # More space for the content
        self.grid_rowconfigure(1, weight=1, uniform="rows")  # Less space for the Quit button
        self.grid_columnconfigure(0, weight=1, uniform="columns")
        self.grid_columnconfigure(1, weight=1, uniform="columns")

        self.create_gui_widgets()

    def create_frame(self, row, column, columnspan=1, rowspan=1):
        """Helper function to create a CTkFrame for a given grid row and column."""
        frame = ctk.CTkFrame(self)
        frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=10, pady=10, sticky="nsew")
        return frame

    def create_gui_widgets(self):
        # Directly place the "Generate Calibration Sheets" button in the grid layout
        generate_cal_sheets_button = GUIButton(self, text="GENERATE CALIBRATION SHEETS", fg_color="green", hover_color="darkgreen", border_color="black")
        generate_cal_sheets_button.generate_calibration_sheets()
        generate_cal_sheets_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")  # Span both columns

        # Create frame for row 0, column 0 (contains test buttons)
        button_frame_0_0 = self.create_frame(row=0, column=0)

        test_button_1 = GUIButton(button_frame_0_0, text="Test", border_color="black")
        test_button_1.pack(padx=5, pady=5)

        test_button_2 = GUIButton(button_frame_0_0, text="ABC", fg_color="purple", hover_color="violet", border_color="black")
        test_button_2.pack(padx=5, pady=5)

        test_button_3 = GUIButton(button_frame_0_0, text="XYZ", fg_color="green", hover_color="darkgreen", border_color="black")
        test_button_3.pack(padx=5, pady=5)
