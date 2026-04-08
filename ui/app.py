import customtkinter as ctk

from config import ALGORITHMS

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class CryptoApp(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("Crypto Algorithms")
        self.geometry("900x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.algorithm_menu = None
        self.input_text = None
        self.key_entry = None
        self.output_text = None

        self.algorithms = ALGORITHMS

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            main_frame,
            text="Classical Cryptography",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#2ecc71"
        )
        title.grid(row=0, column=0, pady=(10, 20))

        # Algorithm selection
        self.algorithm_menu = ctk.CTkOptionMenu(
            main_frame,
            values=["Caesar", "Mono-alphabetic", "Playfair", "Hill"]
        )
        self.algorithm_menu.grid(row=1, column=0, pady=10)

        # Input text field
        input_container = ctk.CTkFrame(main_frame, fg_color="transparent")
        input_container.grid(row=2, column=0, sticky="ew", padx=10)
        input_container.grid_columnconfigure(0, weight=1)

        input_label = ctk.CTkLabel(
            input_container,
            text="Input Text",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w",
            text_color="#2ecc71"
        )
        input_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.input_text = ctk.CTkTextbox(
            input_container,
            height=120,
            corner_radius=10,
            border_width=2
        )
        self.input_text.grid(row=1, column=0, sticky="ew")

        # Key field
        key_container = ctk.CTkFrame(main_frame, fg_color="transparent")
        key_container.grid(row=4, column=0, sticky="ew", padx=10, pady=(10, 5))
        key_container.grid_columnconfigure(0, weight=1)

        key_label = ctk.CTkLabel(
            key_container,
            text="Key",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w",
            text_color="#2ecc71"
        )
        key_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.key_entry = ctk.CTkEntry(
            key_container,
            placeholder_text="Enter the encryption key",
            corner_radius=10
        )
        self.key_entry.grid(row=1, column=0, sticky="ew")

        generate_btn = ctk.CTkButton(key_container, text="Generate Key", command=self.generate_key)
        generate_btn.grid(row=1, column=1, pady=10)

        # Buttons
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.grid(row=5, column=0, pady=10)

        encrypt_btn = ctk.CTkButton(button_frame, text="Encrypt", command=self.encrypt)
        encrypt_btn.grid(row=0, column=0, padx=10)

        decrypt_btn = ctk.CTkButton(button_frame, text="Decrypt", command=self.decrypt)
        decrypt_btn.grid(row=0, column=1, padx=10)

        swap_btn = ctk.CTkButton(button_frame, text="⇄", width=40, command=self.swap_text)
        swap_btn.grid(row=0, column=2, padx=5)

        # Output text field
        output_container = ctk.CTkFrame(main_frame, fg_color="transparent")
        output_container.grid(row=6, column=0, sticky="ew", padx=10, pady=(10, 0))
        output_container.grid_columnconfigure(0, weight=1)

        output_label = ctk.CTkLabel(
            output_container,
            text="Result",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w",
            text_color="#2ecc71"
        )
        output_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.output_text = ctk.CTkTextbox(
            output_container,
            height=120,
            state="disabled",
            corner_radius=10,
            border_width=2,
        )
        self.output_text.grid(row=1, column=0, sticky="ew")

    def set_output(self, text):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", str(text))
        self.output_text.configure(state="disabled")

    def set_key_entry(self, key):
        self.key_entry.delete(0, "end")
        self.key_entry.insert(0, str(key))

    def swap_text(self):
        output_text = self.output_text.get("1.0", "end").strip()

        self.input_text.delete("1.0", "end")
        self.input_text.insert("1.0", output_text)
        self.set_output("")

    def encrypt(self):
        text = self.input_text.get("1.0", "end").strip()
        key = self.key_entry.get()
        algorithm = self.algorithm_menu.get()
        algo = self.algorithms.get(algorithm)

        if algo is None:
            self.set_output("Algorithm not yet implemented")
            return

        try:
            result = algo["encrypt"](text, key)
            self.set_output(result)
        except Exception as e:
            self.set_output(f"Error: {str(e)}")

    def decrypt(self):
        text = self.input_text.get("1.0", "end").strip()
        key = self.key_entry.get()
        algorithm = self.algorithm_menu.get()
        algo = self.algorithms.get(algorithm)

        if algo is None:
            self.set_output("Algorithm not yet implemented")
            return

        try:
            result = algo["decrypt"](text, key)
            self.set_output(result)
        except Exception as e:
            self.set_output(f"Error: {str(e)}")

    def generate_key(self):
        algorithm = self.algorithm_menu.get()
        algo = self.algorithms.get(algorithm)

        if algo is None:
            self.set_output("Algorithm not yet implemented")
            return

        try:
            key = algo["generate"]()
            self.set_key_entry(key)
        except Exception as e:
            self.set_output(f"Error: {str(e)}")
