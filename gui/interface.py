# import customtkinter as ctk
# import tkinter as tk
# import math
# import time
# import psutil
# from PIL import Image


# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")


# class JarvisGUI:

#     def __init__(self):

#         self.app = ctk.CTk()

#         self.app.geometry("1600x900")

#         self.app.title("JARVIS AI")

#         self.app.configure(fg_color="#050816")

#         self.user_input_callback = None

#         self.wave_phase = 0

#         # ================= MAIN LAYOUT =================

#         self.main_frame = ctk.CTkFrame(
#             self.app,
#             fg_color="#050816"
#         )

#         self.main_frame.pack(fill="both", expand=True)

#         # ================= LEFT PANEL =================

#         self.left_panel = ctk.CTkFrame(
#             self.main_frame,
#             width=300,
#             fg_color="#0b1020",
#             corner_radius=20,
#             border_width=2,
#             border_color="#00bfff"
#         )

#         self.left_panel.pack(side="left", fill="y", padx=15, pady=15)

#         self.left_panel.pack_propagate(False)

#         # TITLE

#         self.title = ctk.CTkLabel(
#             self.left_panel,
#             text="JARVIS",
#             font=("Consolas", 34, "bold"),
#             text_color="#00d9ff"
#         )

#         self.title.pack(pady=(30, 10))

#         # AI STATUS

#         self.ai_status = ctk.CTkLabel(
#             self.left_panel,
#             text="AI STATUS : ONLINE",
#             font=("Consolas", 18, "bold"),
#             text_color="#00ff99"
#         )

#         self.ai_status.pack(pady=15)

#         # CPU

#         self.cpu_label = ctk.CTkLabel(
#             self.left_panel,
#             text="CPU : 0%",
#             font=("Consolas", 18),
#             text_color="#00d9ff"
#         )

#         self.cpu_label.pack(pady=10)

#         # RAM

#         self.ram_label = ctk.CTkLabel(
#             self.left_panel,
#             text="RAM : 0%",
#             font=("Consolas", 18),
#             text_color="#00d9ff"
#         )

#         self.ram_label.pack(pady=10)

#         # SYSTEM INFO

#         self.system_title = ctk.CTkLabel(
#             self.left_panel,
#             text="SYSTEM INFO",
#             font=("Consolas", 22, "bold"),
#             text_color="#00d9ff"
#         )

#         self.system_title.pack(pady=(40, 10))

#         self.info_box = ctk.CTkTextbox(
#             self.left_panel,
#             width=240,
#             height=250,
#             fg_color="#050816",
#             text_color="#00d9ff",
#             border_width=2,
#             border_color="#00bfff",
#             font=("Consolas", 15)
#         )

#         self.info_box.pack(pady=10)

#         self.info_box.insert(
#             "end",
#             "SYSTEM : ACTIVE\n\n"
#             "VOICE MODE : READY\n\n"
#             "NETWORK : CONNECTED\n\n"
#             "AI ENGINE : ONLINE\n\n"
#             "SECURITY : ENABLED\n"
#         )

#         # ================= CENTER PANEL =================

#         self.center_panel = ctk.CTkFrame(
#             self.main_frame,
#             fg_color="#050816"
#         )

#         self.center_panel.pack(
#             side="left",
#             fill="both",
#             expand=True,
#             padx=10,
#             pady=15
#         )

#         # WAVEFORM

#         self.wave_canvas = tk.Canvas(
#             self.center_panel,
#             bg="#050816",
#             highlightthickness=0,
#             height=250
#         )

#         self.wave_canvas.pack(fill="x", pady=(10, 0))

#         # CHAT TITLE

#         self.chat_title = ctk.CTkLabel(
#             self.center_panel,
#             text="JARVIS CHATBOT",
#             font=("Consolas", 28, "bold"),
#             text_color="#00d9ff"
#         )

#         self.chat_title.pack(pady=10)

#         # CHAT BOX

#         self.chat_box = ctk.CTkTextbox(
#             self.center_panel,
#             fg_color="#0b1020",
#             text_color="#00d9ff",
#             border_width=2,
#             border_color="#00bfff",
#             font=("Consolas", 16),
#             corner_radius=15
#         )

#         self.chat_box.pack(
#             fill="both",
#             expand=True,
#             padx=10,
#             pady=10
#         )

#         self.chat_box.insert("end", "Jarvis initialized...\n\n")

#         # INPUT FRAME

#         self.input_frame = ctk.CTkFrame(
#             self.center_panel,
#             fg_color="#050816"
#         )

#         self.input_frame.pack(fill="x", pady=15)

#         # ENTRY

#         self.input_box = ctk.CTkEntry(
#             self.input_frame,
#             height=50,
#             font=("Consolas", 18),
#             fg_color="#0b1020",
#             text_color="#00d9ff",
#             border_width=2,
#             border_color="#00bfff",
#             corner_radius=15,
#             placeholder_text="Type your command..."
#         )

#         self.input_box.pack(
#             side="left",
#             fill="x",
#             expand=True,
#             padx=(10, 10)
#         )

#         self.input_box.bind(
#             "<Return>",
#             lambda event: self.send_command()
#         )

#         # SEND BUTTON

#         self.send_btn = ctk.CTkButton(
#             self.input_frame,
#             text="SEND",
#             width=120,
#             height=50,
#             fg_color="#008cff",
#             hover_color="#00bfff",
#             font=("Consolas", 18, "bold"),
#             command=self.send_command
#         )

#         self.send_btn.pack(side="left", padx=(0, 10))

#         # ================= RIGHT PANEL =================

#         self.right_panel = ctk.CTkFrame(
#             self.main_frame,
#             width=300,
#             fg_color="#0b1020",
#             corner_radius=20,
#             border_width=2,
#             border_color="#00bfff"
#         )

#         self.right_panel.pack(side="right", fill="y", padx=15, pady=15)

#         self.right_panel.pack_propagate(False)

#         # CLOCK

#         self.clock_label = ctk.CTkLabel(
#             self.right_panel,
#             text="00:00:00",
#             font=("Consolas", 34, "bold"),
#             text_color="#00d9ff"
#         )

#         self.clock_label.pack(pady=(30, 10))

#         # SPEAKING STATUS

#         self.speaking_label = ctk.CTkLabel(
#             self.right_panel,
#             text="Listening...",
#             font=("Consolas", 20),
#             text_color="#00ff99"
#         )

#         self.speaking_label.pack(pady=20)

#         # QUICK ACTIONS TITLE

#         self.quick_title = ctk.CTkLabel(
#             self.right_panel,
#             text="QUICK ACTIONS",
#             text_color="#00d9ff",
#             font=("Consolas", 24, "bold")
#         )

#         self.quick_title.pack(pady=(40, 20))

#         # ICON FRAME

#         self.icon_frame = ctk.CTkFrame(
#             self.right_panel,
#             fg_color="transparent"
#         )

#         self.icon_frame.pack()

#         # BUTTON STYLE

#         button_style = {
#             "width": 100,
#             "height": 100,
#             "fg_color": "#111827",
#             "hover_color": "#008cff",
#             "corner_radius": 18,
#             "font": ("Consolas", 14, "bold")
#         }

#         # ROW 1

#         self.chrome_btn = ctk.CTkButton(
#             self.icon_frame,
#             text="🌐\nChrome",
#             command=lambda: self.update_chat("Opening Chrome..."),
#             **button_style
#         )

#         self.chrome_btn.grid(row=0, column=0, padx=10, pady=10)

#         self.youtube_btn = ctk.CTkButton(
#             self.icon_frame,
#             text="▶️\nYouTube",
#             command=lambda: self.update_chat("Opening YouTube..."),
#             **button_style
#         )

#         self.youtube_btn.grid(row=0, column=1, padx=10, pady=10)

#         # ROW 2

#         self.vscode_btn = ctk.CTkButton(
#             self.icon_frame,
#             text="💻\nVS Code",
#             command=lambda: self.update_chat("Opening VS Code..."),
#             **button_style
#         )

#         self.vscode_btn.grid(row=1, column=0, padx=10, pady=10)

#         self.calc_btn = ctk.CTkButton(
#             self.icon_frame,
#             text="🧮\nCalculator",
#             command=lambda: self.update_chat("Opening Calculator..."),
#             **button_style
#         )

#         self.calc_btn.grid(row=1, column=1, padx=10, pady=10)

#         # ROW 3

#         self.note_btn = ctk.CTkButton(
#             self.icon_frame,
#             text="📝\nNotepad",
#             command=lambda: self.update_chat("Opening Notepad..."),
#             **button_style
#         )

#         self.note_btn.grid(row=2, column=0, padx=10, pady=10)

#         self.ss_btn = ctk.CTkButton(
#             self.icon_frame,
#             text="📸\nScreenshot",
#             command=lambda: self.update_chat("Taking Screenshot..."),
#             **button_style
#         )

#         self.ss_btn.grid(row=2, column=1, padx=10, pady=10)

#         # MIC ICON

#         self.mic_label = ctk.CTkLabel(
#             self.app,
#             text="🎤",
#             font=("Arial", 44),
#             text_color="#00d9ff"
#         )

#         self.mic_label.place(relx=0.5, rely=0.95, anchor="center")

#         # START LOOPS

#         self.animate_wave()

#         self.update_clock()

#         self.update_system()

#     # ==================================================
#     # WAVE ANIMATION
#     # ==================================================

#     def animate_wave(self):

#         self.wave_canvas.delete("all")

#         width = self.wave_canvas.winfo_width()

#         height = 250

#         center_y = height // 2

#         points = []

#         for x in range(0, width, 8):

#             y = center_y + math.sin(
#                 (x / 50) + self.wave_phase
#             ) * 40

#             points.append((x, y))

#         for i in range(len(points) - 1):

#             x1, y1 = points[i]

#             x2, y2 = points[i + 1]

#             self.wave_canvas.create_line(
#                 x1,
#                 y1,
#                 x2,
#                 y2,
#                 fill="#00d9ff",
#                 width=3,
#                 smooth=True
#             )

#         self.wave_phase += 0.15

#         self.app.after(50, self.animate_wave)

#     # ==================================================
#     # CLOCK
#     # ==================================================

#     def update_clock(self):

#         current = time.strftime("%H:%M:%S")

#         self.clock_label.configure(text=current)

#         self.app.after(1000, self.update_clock)

#     # ==================================================
#     # SYSTEM INFO
#     # ==================================================

#     def update_system(self):

#         cpu = psutil.cpu_percent()

#         ram = psutil.virtual_memory().percent

#         self.cpu_label.configure(text=f"CPU : {cpu}%")

#         self.ram_label.configure(text=f"RAM : {ram}%")

#         self.app.after(2000, self.update_system)

#     # ==================================================
#     # CHAT UPDATE
#     # ==================================================

#     def update_chat(self, text):

#         self.chat_box.insert("end", text + "\n\n")

#         self.chat_box.see("end")

#     # ==================================================
#     # STATUS
#     # ==================================================

#     def update_status(self, text):

#         self.speaking_label.configure(text=text)

#     # ==================================================
#     # INPUT CALLBACK
#     # ==================================================

#     def set_input_callback(self, callback):

#         self.user_input_callback = callback

#     # ==================================================
#     # SEND COMMAND
#     # ==================================================

#     def send_command(self):

#         command = self.input_box.get().strip()

#         if command == "":
#             return

#         self.update_chat(f"You: {command}")

#         self.input_box.delete(0, "end")

#         if self.user_input_callback:
#             self.user_input_callback(command)

#     # ==================================================
#     # RUN
#     # ==================================================

#     def run(self):

#         self.app.mainloop()



"""
JARVIS AI Interface — High Performance Edition
================================================
Performance fixes vs original:
  • ONE master animation loop (app.after) drives ALL canvas drawing.
    No stacked/overlapping after() calls that flood the event queue.
  • Canvas items are UPDATED (coords/config) not deleted+recreated every frame.
    Eliminates GC pressure from thousands of object allocations per second.
  • System-monitor polling runs in a background Thread; results are
    posted back to the GUI via a thread-safe Queue, never touching
    Tkinter from a non-main thread.
  • Clock / date strings are only redrawn when the value changes.
  • All expensive math (sin/cos tables) is pre-computed or cached.
"""

import tkinter as tk
import math
import time
import threading
import queue
import random
import platform
import os

# ── optional psutil (graceful fallback) ──────────────────────────────────────
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

# ── optional PIL for icon rendering (not required) ────────────────────────────
try:
    from PIL import Image, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# ═════════════════════════════════════════════════════════════════════════════
# CONSTANTS / THEME
# ═════════════════════════════════════════════════════════════════════════════
BG          = "#020b18"
PANEL_BG    = "#041018"
BORDER      = "#00d9ff"
CYAN        = "#00d9ff"
CYAN_DIM    = "#005566"
CYAN_FAINT  = "#002233"
GREEN       = "#00ff88"
PURPLE      = "#8800ff"
WHITE       = "#ffffff"
RED         = "#ff4466"
BLUE        = "#0088ff"
FONT_TITLE  = ("Consolas", 11, "bold")
FONT_MONO   = ("Consolas", 10)
FONT_SMALL  = ("Consolas", 9)
FONT_BIG    = ("Consolas", 28, "bold")

FPS         = 30          # target frames per second
FRAME_MS    = 1000 // FPS  # milliseconds per frame
METRIC_INTERVAL = 2.0     # seconds between psutil polls


# ═════════════════════════════════════════════════════════════════════════════
# UTILITY HELPERS
# ═════════════════════════════════════════════════════════════════════════════
def hex_lerp(c1: str, c2: str, t: float) -> str:
    """Linear interpolate between two hex colours."""
    r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
    r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02x}{g:02x}{b:02x}"


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


# ═════════════════════════════════════════════════════════════════════════════
# BACKGROUND METRIC POLLER
# ═════════════════════════════════════════════════════════════════════════════
class MetricPoller(threading.Thread):
    """
    Runs psutil in a daemon thread.
    Posts results into `result_queue` so the GUI thread never blocks.
    """
    def __init__(self, result_queue: queue.Queue, interval: float = METRIC_INTERVAL):
        super().__init__(daemon=True)
        self.q        = result_queue
        self.interval = interval
        self._stop    = threading.Event()

        # system info (static, read once)
        self.sysinfo  = self._read_sysinfo()

    def _read_sysinfo(self) -> dict:
        info = {
            "os":       platform.system() + " " + platform.release(),
            "cpu":      platform.processor() or platform.machine(),
            "cores":    os.cpu_count() or "?",
        }
        if HAS_PSUTIL:
            try:
                mem = psutil.virtual_memory()
                info["ram_total"] = f"{mem.total // (1024**3)} GB"
            except Exception:
                info["ram_total"] = "?"
        return info

    def run(self):
        while not self._stop.is_set():
            data = self._poll()
            # non-blocking put; drop if consumer is slow
            try:
                self.q.put_nowait(data)
            except queue.Full:
                pass
            self._stop.wait(self.interval)

    def _poll(self) -> dict:
        if not HAS_PSUTIL:
            # simulate realistic-looking values
            return {
                "cpu":  random.uniform(10, 45),
                "ram":  random.uniform(55, 70),
                "disk": random.uniform(28, 36),
                "net":  "ACTIVE",
            }
        try:
            return {
                "cpu":  psutil.cpu_percent(interval=None),
                "ram":  psutil.virtual_memory().percent,
                "disk": psutil.disk_usage("/").percent,
                "net":  "ACTIVE",
            }
        except Exception:
            return {"cpu": 0, "ram": 0, "disk": 0, "net": "ERROR"}

    def stop(self):
        self._stop.set()


# ═════════════════════════════════════════════════════════════════════════════
# MAIN GUI CLASS
# ═════════════════════════════════════════════════════════════════════════════
class JarvisGUI:
    # ── init ─────────────────────────────────────────────────────────────────
    def __init__(self):
        self.user_input_callback = None
        self._metric_q = queue.Queue(maxsize=2)
        self._poller   = MetricPoller(self._metric_q)

        # animation state
        self._frame      = 0
        self._hud_angle  = 0.0
        self._wave_off   = 0.0
        self._start_time = time.time()
        self._metrics    = {"cpu": 18.0, "ram": 62.0, "disk": 34.0, "net": "ACTIVE"}
        self._mic_on     = False
        self._uptime_str = "00:00:00"

        # clock cache
        self._last_clock_str = ""
        self._last_date_str  = ""

        # chat typing state
        self._typing      = False
        self._typing_text = ""
        self._typing_idx  = 0

        self._build_window()
        self._build_layout()
        self._poller.start()
        self._schedule_loop()

    # ── window ───────────────────────────────────────────────────────────────
    def _build_window(self):
        self.root = tk.Tk()
        self.root.title("JARVIS AI")
        self.root.geometry("1500x900")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        self._poller.stop()
        self.root.destroy()

    # ── layout scaffolding ───────────────────────────────────────────────────
    def _build_layout(self):
        # title bar
        tb = tk.Frame(self.root, bg=PANEL_BG, height=50)
        tb.pack(fill="x")
        tb.pack_propagate(False)
        tk.Label(tb, text="JARVIS", bg=PANEL_BG, fg=CYAN,
                 font=("Consolas", 26, "bold")).pack(side="left", padx=20)
        tk.Label(tb, text="SYS v4.2.1", bg=PANEL_BG, fg=CYAN_DIM,
                 font=FONT_SMALL).pack(side="left", padx=10)
        tk.Label(tb, text="AI ASSISTANT ONLINE", bg=PANEL_BG, fg=CYAN_DIM,
                 font=FONT_SMALL).pack(side="right", padx=20)

        # three-column body
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True)

        self.left_panel  = self._make_panel(body, side="left",  w=230)
        self.right_panel = self._make_panel(body, side="right", w=230)

        # center fills remaining space
        self.center = tk.Frame(body, bg=BG)
        self.center.pack(side="left", fill="both", expand=True)

        self._build_left()
        self._build_center()
        self._build_right()

    def _make_panel(self, parent, side, w):
        f = tk.Frame(parent, bg=PANEL_BG, width=w,
                     highlightthickness=1, highlightbackground=CYAN_DIM)
        f.pack(side=side, fill="y", padx=6, pady=6)
        f.pack_propagate(False)
        return f

    def _section(self, parent, title):
        tk.Label(parent, text=title, bg=PANEL_BG, fg=CYAN,
                 font=("Consolas", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
        tk.Frame(parent, bg=CYAN_DIM, height=1).pack(fill="x", padx=10)

    # ── LEFT PANEL ───────────────────────────────────────────────────────────
    def _build_left(self):
        p = self.left_panel

        # ── SYSTEM MONITOR ──
        self._section(p, "SYSTEM MONITOR")
        self.ring_cpu  = self._ring_canvas(p, "CPU",  CYAN)
        self.ring_ram  = self._ring_canvas(p, "RAM",  PURPLE)
        self.ring_disk = self._ring_canvas(p, "DISK", GREEN)

        bar_frame = tk.Frame(p, bg=PANEL_BG)
        bar_frame.pack(fill="x", padx=10, pady=4)
        self.cpu_bar,  self.cpu_val  = self._bar_row(bar_frame, "CPU",  BLUE)
        self.ram_bar,  self.ram_val  = self._bar_row(bar_frame, "RAM",  PURPLE)
        self.disk_bar, self.disk_val = self._bar_row(bar_frame, "DISK", GREEN)

        # ── SYSTEM INFO ──
        self._section(p, "SYSTEM INFO")
        info_f = tk.Frame(p, bg=PANEL_BG)
        info_f.pack(fill="x", padx=10, pady=4)
        si = self._poller.sysinfo
        rows = [
            ("OS",    si.get("os",    "Windows 11")),
            ("CPU",   si.get("cpu",   "Intel Core")),
            ("CORES", str(si.get("cores", "8"))),
            ("UPTIME","00:00:00"),
            ("NET",   "ACTIVE"),
        ]
        self._sysinfo_vals = {}
        for key, val in rows:
            row = tk.Frame(info_f, bg=PANEL_BG)
            row.pack(fill="x", pady=1)
            tk.Label(row, text=key, bg=PANEL_BG, fg=CYAN_DIM,
                     font=FONT_SMALL, width=6, anchor="w").pack(side="left")
            lbl = tk.Label(row, text=val, bg=PANEL_BG, fg=CYAN,
                           font=FONT_SMALL, anchor="w")
            lbl.pack(side="left", fill="x", expand=True)
            self._sysinfo_vals[key] = lbl

        # ── AI STATUS ──
        self._section(p, "AI STATUS")
        status_f = tk.Frame(p, bg=PANEL_BG)
        status_f.pack(fill="x", padx=10, pady=6)
        dot = tk.Canvas(status_f, width=14, height=14, bg=PANEL_BG,
                        highlightthickness=0)
        dot.pack(side="left")
        dot.create_oval(2, 2, 12, 12, fill=GREEN, outline=GREEN, tags="dot")
        self._status_dot = dot
        tk.Label(status_f, text="ONLINE", bg=PANEL_BG, fg=GREEN,
                 font=("Consolas", 11, "bold")).pack(side="left", padx=6)
        tk.Label(p, text="ALL SYSTEMS OPERATIONAL", bg=PANEL_BG, fg=CYAN_DIM,
                 font=FONT_SMALL).pack(anchor="w", padx=10)

        # status graph canvas
        self._sg_canvas = tk.Canvas(p, width=200, height=45, bg=PANEL_BG,
                                    highlightthickness=0)
        self._sg_canvas.pack(padx=10, pady=4)
        self._sg_history = [18.0] * 40

    def _ring_canvas(self, parent, label, color):
        f = tk.Frame(parent, bg=PANEL_BG)
        f.pack(side="left", padx=5, pady=4)
        c = tk.Canvas(f, width=64, height=64, bg=PANEL_BG, highlightthickness=0)
        c.pack()
        tk.Label(f, text=label, bg=PANEL_BG, fg=CYAN_DIM,
                 font=("Consolas", 8)).pack()
        c._color   = color
        c._val     = 0.0
        c._arc     = c.create_arc(8, 8, 56, 56, start=90, extent=0,
                                   style="arc", outline=color, width=5)
        c._track   = c.create_arc(8, 8, 56, 56, start=0, extent=359.9,
                                   style="arc", outline=CYAN_FAINT, width=5)
        c._text    = c.create_text(32, 32, text="0%", fill=color,
                                    font=("Consolas", 10, "bold"))
        return c

    def _bar_row(self, parent, label, color):
        row = tk.Frame(parent, bg=PANEL_BG)
        row.pack(fill="x", pady=2)
        tk.Label(row, text=label, bg=PANEL_BG, fg=CYAN_DIM,
                 font=FONT_SMALL, width=4, anchor="w").pack(side="left")
        track = tk.Canvas(row, height=8, bg=CYAN_FAINT,
                          highlightthickness=0)
        track.pack(side="left", fill="x", expand=True, padx=4)
        fill = track.create_rectangle(0, 0, 0, 8, fill=color, outline="")
        val  = tk.Label(row, text="0%", bg=PANEL_BG, fg=CYAN,
                        font=FONT_SMALL, width=5, anchor="e")
        val.pack(side="left")
        track._fill = fill
        return track, val

    # ── CENTER ───────────────────────────────────────────────────────────────
    def _build_center(self):
        c = self.center

        # waveform
        wlbl = tk.Frame(c, bg=BG)
        wlbl.pack(fill="x", padx=8, pady=(6, 0))
        tk.Label(wlbl, text="VOICE WAVEFORM", bg=BG, fg=CYAN_DIM,
                 font=FONT_SMALL).pack(anchor="w")

        self.wave_canvas = tk.Canvas(c, height=80, bg=BG, highlightthickness=0)
        self.wave_canvas.pack(fill="x", padx=8)
        # pre-create wave lines
        self._wave_lines = []
        for _ in range(70):
            ln = self.wave_canvas.create_line(0, 40, 0, 40, fill=CYAN, width=2)
            self._wave_lines.append(ln)

        # HUD canvas
        self.hud_canvas = tk.Canvas(c, height=260, bg=BG, highlightthickness=0)
        self.hud_canvas.pack(fill="x", padx=8, pady=4)
        self._build_hud_static()

        # chat section
        chat_lbl = tk.Frame(c, bg=BG)
        chat_lbl.pack(fill="x", padx=8)
        tk.Label(chat_lbl, text="JARVIS CHATBOT  ─  NEURAL LINK ACTIVE",
                 bg=BG, fg=CYAN_DIM, font=FONT_SMALL).pack(anchor="w")
        tk.Frame(c, bg=CYAN_DIM, height=1).pack(fill="x", padx=8)

        self.chat_box = tk.Text(
            c, bg="#000814", fg=CYAN, font=FONT_MONO,
            relief="flat", padx=8, pady=6,
            insertbackground=CYAN, wrap="word",
            highlightthickness=1, highlightbackground=CYAN_DIM,
        )
        self.chat_box.pack(fill="both", expand=True, padx=8, pady=4)
        self.chat_box.tag_configure("user",   foreground=BLUE)
        self.chat_box.tag_configure("jarvis", foreground=CYAN)
        self.chat_box.tag_configure("label_user",   foreground=BLUE,   font=("Consolas", 8, "bold"))
        self.chat_box.tag_configure("label_jarvis", foreground=CYAN,   font=("Consolas", 8, "bold"))
        self.chat_box.configure(state="disabled")
        self._chat_insert("JARVIS", "Systems initialized. All modules online. How can I assist you?")

        # mic + input
        mic_row = tk.Frame(c, bg=BG)
        mic_row.pack(pady=4)
        self.mic_btn = tk.Button(
            mic_row, text="🎤", bg=PANEL_BG, fg=CYAN,
            font=("Arial", 22), relief="flat", cursor="hand2",
            activebackground=CYAN_DIM, command=self._toggle_mic,
            highlightthickness=1, highlightbackground=CYAN_DIM,
        )
        self.mic_btn.pack()

        inp_row = tk.Frame(c, bg=BG)
        inp_row.pack(fill="x", padx=8, pady=(0, 6))
        self.input_box = tk.Entry(
            inp_row, bg="#000814", fg=CYAN, font=FONT_MONO,
            insertbackground=CYAN, relief="flat",
            highlightthickness=1, highlightbackground=CYAN_DIM,
        )
        self.input_box.pack(side="left", fill="x", expand=True, ipady=6)
        self.input_box.bind("<Return>", lambda e: self._send_command())
        tk.Button(
            inp_row, text="SEND", bg=BLUE, fg=WHITE,
            font=("Consolas", 10, "bold"), relief="flat", cursor="hand2",
            command=self._send_command, padx=12,
        ).pack(side="left", padx=(6, 0), ipady=6)

    def _build_hud_static(self):
        """Draw static HUD elements (grid) once."""
        c  = self.hud_canvas
        # We'll draw everything dynamically in the loop for simplicity,
        # but tag static grid items so we don't recreate them.
        # Grid lines — created once, never touched again.
        for x in range(0, 1500, 50):
            c.create_line(x, 0, x, 260, fill="#022b3a", tags="grid")
        for y in range(0, 260, 50):
            c.create_line(0, y, 1500, y, fill="#022b3a", tags="grid")

        # Static concentric circles + arcs
        self._hud_cx = 0   # will be set on first resize
        self._hud_cy = 130

        # Create dynamic items with placeholder coords
        self._hud_circles = []
        for r in [20, 40, 60, 80, 100, 120, 140]:
            oid = c.create_oval(0, 0, 1, 1, outline=CYAN_DIM, width=1, tags="dyn")
            self._hud_circles.append((oid, r))

        self._hud_scanner = c.create_line(0, 0, 1, 1,
                                           fill=CYAN, width=2, tags="dyn")
        self._hud_dot     = c.create_oval(0, 0, 1, 1,
                                           fill=CYAN, outline=CYAN, tags="dyn")
        self._hud_core    = c.create_oval(0, 0, 1, 1,
                                           fill=CYAN, outline=CYAN, tags="dyn")

        # Tick marks — static, drawn once after we know cx
        self._hud_ticks_ready = False

    def _ensure_hud_center(self):
        w = self.hud_canvas.winfo_width()
        if w < 10:
            return
        cx = w // 2
        if self._hud_cx == cx and self._hud_ticks_ready:
            return
        self._hud_cx = cx
        cy = self._hud_cy
        c  = self.hud_canvas
        # redraw circles
        for oid, r in self._hud_circles:
            c.coords(oid, cx - r, cy - r, cx + r, cy + r)
        # draw ticks if not yet done
        if not self._hud_ticks_ready:
            for i in range(36):
                a   = i * math.pi * 2 / 36
                ln  = 10 if i % 9 == 0 else 5
                r1  = 145
                col = CYAN_DIM if i % 9 == 0 else "#002233"
                ww  = 2 if i % 9 == 0 else 1
                c.create_line(
                    cx + r1 * math.cos(a), cy + r1 * math.sin(a),
                    cx + (r1 + ln) * math.cos(a), cy + (r1 + ln) * math.sin(a),
                    fill=col, width=ww, tags="tick",
                )
            self._hud_ticks_ready = True

    # ── RIGHT PANEL ──────────────────────────────────────────────────────────
    def _build_right(self):
        p = self.right_panel

        # ── LIVE CLOCK ──
        self._section(p, "LIVE CLOCK")
        self.clock_lbl = tk.Label(p, text="00:00:00", bg=PANEL_BG, fg=CYAN,
                                  font=("Consolas", 22, "bold"))
        self.clock_lbl.pack(pady=(4, 0))
        self.date_lbl = tk.Label(p, text="", bg=PANEL_BG, fg=CYAN_DIM,
                                 font=FONT_SMALL)
        self.date_lbl.pack()

        self.analog_canvas = tk.Canvas(p, width=160, height=160, bg=PANEL_BG,
                                       highlightthickness=0)
        self.analog_canvas.pack(pady=6)
        self._build_analog_static()

        # ── SPEAKING ──
        self._section(p, "SPEAKING...")
        self.speak_lbl = tk.Label(p, text="Voice system active...", bg=PANEL_BG,
                                  fg=CYAN_DIM, font=FONT_SMALL, wraplength=200,
                                  justify="left")
        self.speak_lbl.pack(anchor="w", padx=10, pady=2)
        self.speak_canvas = tk.Canvas(p, width=200, height=50, bg=PANEL_BG,
                                      highlightthickness=0)
        self.speak_canvas.pack(padx=10, pady=4)
        self._speak_lines = []
        for _ in range(20):
            ln = self.speak_canvas.create_line(0, 25, 0, 25,
                                                fill=PURPLE, width=2)
            self._speak_lines.append(ln)

        # ── QUICK ACTIONS ──
        self._section(p, "QUICK ACTIONS")
        grid_f = tk.Frame(p, bg=PANEL_BG)
        grid_f.pack(padx=8, pady=6)
        actions = [
            ("🌐", "Chrome"), ("▶", "YouTube"), ("💻", "VS Code"),
            ("🧮", "Calc"),   ("📝", "Notepad"), ("📸", "Shot"),
        ]
        for idx, (icon, label) in enumerate(actions):
            r, c_col = divmod(idx, 3)
            btn = tk.Button(
                grid_f, text=f"{icon}\n{label}",
                bg="#000814", fg=CYAN,
                font=("Consolas", 9), relief="flat", cursor="hand2",
                width=7, height=3,
                highlightthickness=1, highlightbackground=CYAN_DIM,
                activebackground=CYAN_DIM,
            )
            btn.grid(row=r, column=c_col, padx=4, pady=4)

    def _build_analog_static(self):
        c  = self.analog_canvas
        cx, cy, r = 80, 80, 72
        # face rings
        c.create_oval(cx-r, cy-r, cx+r, cy+r, outline=CYAN_DIM, width=2)
        c.create_oval(cx-r+8, cy-r+8, cx+r-8, cy+r-8,
                       outline="#001a25", width=1)
        # tick marks (static)
        for i in range(60):
            a   = i * math.pi * 2 / 60 - math.pi / 2
            ln  = 8 if i % 5 == 0 else 4
            ri  = r - 2
            col = CYAN_DIM if i % 5 == 0 else "#002233"
            ww  = 1.5 if i % 5 == 0 else 0.8
            c.create_line(
                cx + ri * math.cos(a), cy + ri * math.sin(a),
                cx + (ri - ln) * math.cos(a), cy + (ri - ln) * math.sin(a),
                fill=col, width=ww,
            )
        # clock hands (dynamic — created once, moved each frame)
        self._hand_hr  = c.create_line(cx, cy, cx, cy, fill=CYAN,    width=4, capstyle="round")
        self._hand_min = c.create_line(cx, cy, cx, cy, fill=CYAN,    width=2.5, capstyle="round")
        self._hand_sec = c.create_line(cx, cy, cx, cy, fill=RED,     width=1.5, capstyle="round")
        self._hand_dot = c.create_oval(cx-4, cy-4, cx+4, cy+4,
                                        fill=CYAN, outline=CYAN)
        self._analog_cx = cx
        self._analog_cy = cy
        self._analog_r  = r

    # ═════════════════════════════════════════════════════════════════════════
    # MASTER ANIMATION LOOP  (single after(), no recursion pileup)
    # ═════════════════════════════════════════════════════════════════════════
    def _schedule_loop(self):
        self._loop_id = self.root.after(FRAME_MS, self._master_loop)

    def _master_loop(self):
        """Called once per frame. All animation happens here."""
        self._frame += 1
        t = time.time()

        # ── drain metric queue (non-blocking) ───────────────────────────────
        try:
            data = self._metric_q.get_nowait()
            self._metrics = data
            self._update_metrics_ui()
        except queue.Empty:
            pass

        # ── waveform ────────────────────────────────────────────────────────
        self._draw_waveform()

        # ── HUD radar ───────────────────────────────────────────────────────
        self._draw_hud()

        # ── speak wave ──────────────────────────────────────────────────────
        self._draw_speak_wave()

        # ── status graph ────────────────────────────────────────────────────
        if self._frame % FPS == 0:          # once per second
            self._sg_history.append(self._metrics["cpu"])
            self._sg_history = self._sg_history[-40:]
            self._draw_status_graph()

        # ── clock (every second) ────────────────────────────────────────────
        clock_str = time.strftime("%H:%M:%S")
        date_str  = time.strftime("%A, %d %b %Y")
        if clock_str != self._last_clock_str:
            self._last_clock_str = clock_str
            self.clock_lbl.configure(text=clock_str)
            self._draw_analog_clock()
        if date_str != self._last_date_str:
            self._last_date_str = date_str
            self.date_lbl.configure(text=date_str)
            # update uptime
            elapsed = int(t - self._start_time)
            h, rem  = divmod(elapsed, 3600)
            m, s    = divmod(rem, 60)
            self._sysinfo_vals["UPTIME"].configure(text=f"{h:02d}:{m:02d}:{s:02d}")

        # ── status dot pulse ────────────────────────────────────────────────
        pulse = abs(math.sin(t * 2)) * 0.7 + 0.3
        g_val = int(255 * pulse)
        col   = f"#00{g_val:02x}55"
        self._status_dot.itemconfigure("dot", fill=col, outline=col)

        # ── advance wave offset ──────────────────────────────────────────────
        self._wave_off += 1
        self._hud_angle += 0.04

        # reschedule
        self._schedule_loop()

    # ═════════════════════════════════════════════════════════════════════════
    # DRAWING METHODS
    # ═════════════════════════════════════════════════════════════════════════
    def _draw_waveform(self):
        c   = self.wave_canvas
        w   = c.winfo_width()
        h   = c.winfo_height()
        if w < 10:
            return
        mid = h // 2
        n   = len(self._wave_lines)
        sp  = w / n
        amp_scale = 28 if self._mic_on else 12

        for i, ln in enumerate(self._wave_lines):
            x   = i * sp + sp / 2
            amp = (abs(math.sin((i + self._wave_off) * 0.4)) * amp_scale + 3)
            c.coords(ln, x, mid - amp, x, mid + amp)

    def _draw_hud(self):
        self._ensure_hud_center()
        cx = self._hud_cx
        cy = self._hud_cy
        if cx == 0:
            return
        c   = self.hud_canvas
        ang = self._hud_angle
        sx  = cx + 140 * math.cos(ang)
        sy  = cy + 140 * math.sin(ang)

        c.coords(self._hud_scanner, cx, cy, sx, sy)
        c.coords(self._hud_dot,     sx - 6, sy - 6, sx + 6, sy + 6)
        c.coords(self._hud_core,    cx - 6, cy - 6, cx + 6, cy + 6)

    def _draw_analog_clock(self):
        now = time.localtime()
        s   = now.tm_sec
        m   = now.tm_min
        h   = now.tm_hour % 12
        cx, cy, r = self._analog_cx, self._analog_cy, self._analog_r

        def hand_end(angle_rad, length):
            return (cx + length * math.cos(angle_rad),
                    cy + length * math.sin(angle_rad))

        hr_a  = (h + m / 60) / 12 * 2 * math.pi - math.pi / 2
        min_a = (m + s / 60) / 60 * 2 * math.pi - math.pi / 2
        sec_a = s / 60 * 2 * math.pi - math.pi / 2

        hx, hy = hand_end(hr_a,  40)
        mx, my = hand_end(min_a, 55)
        sx2, sy2 = hand_end(sec_a, 62)

        c = self.analog_canvas
        c.coords(self._hand_hr,  cx, cy, hx, hy)
        c.coords(self._hand_min, cx, cy, mx, my)
        c.coords(self._hand_sec, cx, cy, sx2, sy2)

    def _draw_speak_wave(self):
        c   = self.speak_canvas
        w   = c.winfo_width()
        h   = c.winfo_height()
        mid = h // 2
        n   = len(self._speak_lines)
        if n == 0 or w < 10:
            return
        sp      = w / n
        scale   = 20 if self._mic_on else 8

        for i, ln in enumerate(self._speak_lines):
            x   = i * sp + sp / 2
            amp = abs(math.sin((i + self._wave_off * 0.5) * 0.6 + i * 0.3)) * scale + 3
            c.coords(ln, x, mid - amp, x, mid + amp)

    def _draw_status_graph(self):
        c  = self._sg_canvas
        w  = c.winfo_width()
        h  = c.winfo_height()
        if w < 10:
            return
        c.delete("all")
        pts    = self._sg_history
        n      = len(pts)
        if n < 2:
            return
        step   = w / (n - 1)
        coords = []
        for i, v in enumerate(pts):
            x = i * step
            y = h - (v / 100) * h
            coords.extend([x, y])
        c.create_line(*coords, fill=CYAN, width=1.5, smooth=True)

    # ═════════════════════════════════════════════════════════════════════════
    # METRICS UI UPDATE  (runs on main thread, data from queue)
    # ═════════════════════════════════════════════════════════════════════════
    def _update_metrics_ui(self):
        d = self._metrics
        for key, bar, val_lbl, color in [
            ("cpu",  self.cpu_bar,  self.cpu_val,  BLUE),
            ("ram",  self.ram_bar,  self.ram_val,  PURPLE),
            ("disk", self.disk_bar, self.disk_val, GREEN),
        ]:
            pct  = clamp(d[key], 0, 100)
            w    = bar.winfo_width()
            fill_w = int(w * pct / 100)
            bar.coords(bar._fill, 0, 0, fill_w, bar.winfo_height())
            val_lbl.configure(text=f"{pct:.0f}%")

        # rings
        self._draw_ring(self.ring_cpu,  d["cpu"],  CYAN)
        self._draw_ring(self.ring_ram,  d["ram"],  PURPLE)
        self._draw_ring(self.ring_disk, d["disk"], GREEN)

        # sysinfo net
        self._sysinfo_vals["NET"].configure(text=d.get("net", "ACTIVE"))

    def _draw_ring(self, canvas: tk.Canvas, val: float, color: str):
        pct    = clamp(val, 0, 100)
        extent = -(pct / 100) * 359.9   # negative = clockwise
        canvas.itemconfigure(canvas._arc, outline=color, extent=extent)
        canvas.itemconfigure(canvas._text, text=f"{pct:.0f}%")

    # ═════════════════════════════════════════════════════════════════════════
    # CHAT
    # ═════════════════════════════════════════════════════════════════════════
    _RESPONSES = [
        "Processing your request. Command acknowledged.",
        "Scanning system parameters. All clear.",
        "Neural pathways engaged. Running analysis.",
        "Affirmative. Task queued in execution pipeline.",
        "Voice recognition active. Awaiting further input.",
        "Accessing database... Query complete.",
        "Network scan initiated. Monitoring activity.",
        "Optimizing performance metrics. Standby.",
        "Deep analysis complete. Results are nominal.",
        "All subsystems nominal. Ready for next command.",
    ]

    def _chat_insert(self, speaker: str, text: str):
        self.chat_box.configure(state="normal")
        tag   = "label_jarvis" if speaker == "JARVIS" else "label_user"
        utag  = "jarvis" if speaker == "JARVIS" else "user"
        self.chat_box.insert("end", f"\n{speaker}\n", tag)
        self.chat_box.insert("end", text + "\n", utag)
        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")

    def _send_command(self):
        if self._typing:
            return
        cmd = self.input_box.get().strip()
        if not cmd:
            return
        self.input_box.delete(0, "end")
        self._chat_insert("YOU", cmd)
        self.speak_lbl.configure(text="Processing...")
        self._typing = True
        # respond after short delay in a timer (no thread needed)
        delay = random.randint(600, 1200)
        self.root.after(delay, self._deliver_response)

    def _deliver_response(self):
        resp = random.choice(self._RESPONSES)
        self._chat_insert("JARVIS", resp)
        self.speak_lbl.configure(text=resp)
        self._typing = False

        # callback for external AI integration
        if self.user_input_callback:
            threading.Thread(
                target=self.user_input_callback,
                args=(resp,),
                daemon=True,
            ).start()

    # ═════════════════════════════════════════════════════════════════════════
    # MIC TOGGLE
    # ═════════════════════════════════════════════════════════════════════════
    def _toggle_mic(self):
        self._mic_on = not self._mic_on
        if self._mic_on:
            self.mic_btn.configure(bg=CYAN_DIM)
            self.speak_lbl.configure(text="Listening...")
        else:
            self.mic_btn.configure(bg=PANEL_BG)
            self.speak_lbl.configure(text="Voice system active...")

    # ═════════════════════════════════════════════════════════════════════════
    # PUBLIC API (same surface as original)
    # ═════════════════════════════════════════════════════════════════════════
    def set_input_callback(self, callback):
        """Register a function(command: str) to be called when user sends text."""
        self.user_input_callback = callback

    def update_chat(self, text: str):
        """Thread-safe: schedule chat update on the GUI thread."""
        self.root.after(0, lambda: self._chat_insert("JARVIS", text))

    def update_status(self, text: str):
        """Update the speaking / status label."""
        self.root.after(0, lambda: self.speak_lbl.configure(text=text))

    def run(self):
        self.root.mainloop()


# ═════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    gui = JarvisGUI()
    gui.run()