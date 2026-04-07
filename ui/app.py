import customtkinter as ctk

from algorithms.caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class CryptoApp(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("Crypto Algorithms")
        self.geometry("900x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()

        self.algorithms = {
            "Caesar": {
                "encrypt": caesar_encrypt,
                "decrypt": caesar_decrypt
            },
            "Mono-alphabetic": None,
            "Playfair": None,
            "Hill": None,
        }

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
        ctk.CTkLabel(main_frame, text="Input text").grid(row=2, column=0, pady=10)
        self.input_text = ctk.CTkTextbox(main_frame, height=120)
        self.input_text.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Key field
        self.key_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter the key")
        self.key_entry.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        # Buttons
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.grid(row=5, column=0, pady=10)

        encrypt_btn = ctk.CTkButton(button_frame, text="Encrypt", command=self.encrypt)
        encrypt_btn.grid(row=0, column=0, padx=10)

        decrypt_btn = ctk.CTkButton(button_frame, text="Decrypt", command=self.decrypt)
        decrypt_btn.grid(row=0, column=1, padx=10)

        swap_btn = ctk.CTkButton(button_frame, text="⇄", width=40, command=self.swap_text)
        swap_btn.grid(row=0, column=2, padx=5)

        # Output text field
        ctk.CTkLabel(main_frame, text="Result").grid(row=6, column=0, pady=10)
        self.output_text = ctk.CTkTextbox(main_frame, height=120, state="disabled")
        self.output_text.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

    def set_output(self, text):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", text)
        self.output_text.configure(state="disabled")

    def swap_text(self):
        input_text = self.input_text.get("1.0", "end").strip()
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
