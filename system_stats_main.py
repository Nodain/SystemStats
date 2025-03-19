from customtkinter import *; import os; import psutil, cpuinfo, platform, threading
import GPUtil

stats = CTk()
stats.title("System Monitor")

window_width = 700
window_height = 500

screen_width = stats.winfo_screenwidth()
screen_height = stats.winfo_screenheight()

x_axis = (screen_width / 2) - (window_width / 2)
y_axis = (screen_height / 2) - (window_height / 2)

stats.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_axis), int(y_axis)))

current_path = os.path.dirname(os.path.realpath(__file__))
stats.iconbitmap(current_path + "\images\icon\city.ico")

#Main Frame

tile_1 = CTkFrame(
    stats,
    width=665,
    height=200,
    border_color="#3df0cd",
    border_width=1,
    corner_radius=8,
    fg_color="#292929"
)

tile_1.place(relx=0.025, rely=0.05)

#Sub Frames

tile_2 = CTkFrame(
    #Left
    stats,
    width=250,
    height=225,
    border_color="#3df0cd",
    border_width=1,
    corner_radius=8,
    fg_color="#292929"
)

tile_2.place(relx=0.025, rely=0.5)

tile_3 = CTkFrame(
    #Right
    stats,
    width=250,
    height=225,
    border_color="#3df0cd",
    border_width=1,
    corner_radius=8,
    fg_color="#292929"
)

tile_3.place(relx=0.615, rely=0.5)

#CPU

cpu_perc_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

cpu_perc_preview.place(relx=0.02, rely=0.07)

cpu_freq_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

cpu_freq_preview.place(relx=0.02, rely=0.21)

phys_core_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

phys_core_preview.place(relx=0.02, rely=0.35)

log_core_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

log_core_preview.place(relx=0.02, rely=0.49)

cpu_times_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

cpu_times_preview.place(relx=0.02, rely=0.63)

cpu_model_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

cpu_model_preview.place(relx=0.02, rely=0.77)

cpu_arch_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

cpu_arch_preview.place(relx=0.51, rely=0.77)

# Memory

mem_usage_preview = CTkLabel(
    tile_3,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

mem_usage_preview.place(relx=0.05, rely=0.07)

mem_total_preview = CTkLabel(
    tile_3,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

mem_total_preview.place(relx=0.05, rely=0.21)

#PC Info

pc_os_preview = CTkLabel(
    tile_1,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

pc_os_preview.place(relx=0.51, rely=0.63)

#Gpu

gpu_model_preview = CTkLabel(
    tile_2,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

gpu_model_preview.place(relx=0.06, rely=0.07)

gpu_load_preview = CTkLabel(
    tile_2,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

gpu_load_preview.place(relx=0.06, rely=0.21)

gpu_freem_preview = CTkLabel(
    tile_2,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

gpu_freem_preview.place(relx=0.06, rely=0.35)

gpu_usedm_preview = CTkLabel(
    tile_2,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

gpu_usedm_preview.place(relx=0.06, rely=0.49)

gpu_totalm_preview = CTkLabel(
    tile_2,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

gpu_totalm_preview.place(relx=0.06, rely=0.63)

gpu_temperature_preview = CTkLabel(
    tile_2,
    width=20,
    height=20,
    corner_radius=8,
    fg_color="#353535",
    bg_color="transparent"
)

gpu_temperature_preview.place(relx=0.06, rely=0.77)

#Retrieve stats that dont need updates

cpu_model = cpuinfo.get_cpu_info()['brand_raw'] #cpu brand/model name
cpu_arch = cpuinfo.get_cpu_info()['arch'] #cpu architecture
phys_core = psutil.cpu_count(logical=False)
log_core = psutil.cpu_count(logical=TRUE) - phys_core #psutil.cpu_count(logical=False)
cpu_times = psutil.cpu_times().user / 60 // 60 # hours | aka uptime
pc_os = platform.platform() # operating system
mem_total = psutil.virtual_memory().total // 1_000_000_000 #retrieve total amount of ram in PC

#display the static stats

pc_os_preview.configure(text=f"OS: {pc_os}")
mem_total_preview.configure(text=f"RAM Available: {mem_total} GB")
phys_core_preview.configure(text=f"Physical Cores: {phys_core}")
log_core_preview.configure(text=f"Logical Cores: {log_core}")
cpu_model_preview.configure(text=f"Processor: {cpu_model}")
cpu_arch_preview.configure(text=f"Arch: {cpu_arch}")
cpu_times_preview.configure(text=f"PC Uptime: {cpu_times} Hours")

#Retrieve real time stats

def pull_stats():
    while True:
        cpu_percentage = psutil.cpu_percent()
        cpu_freq = cpuinfo.get_cpu_info()['hz_advertised_friendly']
        mem_usage = psutil.virtual_memory().percent

        # get gpu info
        gpu_model = GPUtil.getGPUs()

        for gpu in gpu_model:

            gpu_name = gpu.name
            gpu_load = f"{int(gpu.load*100)}%"
            gpu_free_memory = f"{gpu.memoryFree//1000}GB"
            gpu_used_memory = f"{gpu.memoryUsed//1000}GB"
            gpu_total_memory = f"{gpu.memoryTotal//1000}GB"
            gpu_temperature = f"{gpu.temperature} °C"
        
        stats.after(0, update_ui, cpu_percentage, cpu_freq, mem_usage, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature)

def update_ui(cpu_percentage, cpu_freq, mem_usage, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature):
        
        #Configure the new text
        cpu_perc_preview.configure(text=f"CPU Usage: {cpu_percentage}%")
        cpu_freq_preview.configure(text=f"CPU Freq: {cpu_freq}")
        mem_usage_preview.configure(text=f"RAM Usage: {mem_usage}%")

        gpu_model_preview.configure(text=f"{gpu_name}")
        gpu_load_preview.configure(text=f"Load: {gpu_load}")
        gpu_freem_preview.configure(text=f"Free Memory: {gpu_free_memory}")
        gpu_usedm_preview.configure(text=f"Used Memory: {gpu_used_memory}")
        gpu_totalm_preview.configure(text=f"Total Memory: {gpu_total_memory}")
        gpu_temperature_preview.configure(text=f"Temp: {gpu_temperature}")



stats_thread = threading.Thread(target=pull_stats, daemon=True)
stats_thread.start()

#cpu_btn = CTkButton(stats, 80, 30, 8, text="START", command=pull_stats(), fg_color="#292929", border_color="#3df0cd", border_width=1, hover_color="#222222")
#cpu_btn.place(relx=0.3, rely=.886)

stats.resizable(False,False)
stats.mainloop()