import subprocess
import shutil
import gradio
serv = subprocess.Popen(["C:\\Users\\seth2\\AppData\\Local\\Roblox\\Versions\\version-2cca5ed32b534b2a\\RobloxPlayerBeta.exe"])

def rServ():
    global serv
    serv.kill()
    serv = subprocess.Popen(["C:\\Users\\seth2\\AppData\\Local\\Roblox\\Versions\\version-2cca5ed32b534b2a\\RobloxPlayerBeta.exe"])
    return("Restarted Server!")
    

def dl(upl):
    shutil.copyfile(upl, "C:\\Users\\seth2\\Desktop\\GradBeam\\beta\\" + upl.split("\\")[len(upl.split("\\"))-1])
    return "Mod Uploaded! Restart Server To Apply!"
        

with gradio.Blocks() as configPage:
    gradio.Markdown("# Configure BeamMP Server\nV0.1")
    with gradio.Row():
        upl= inputs=gradio.UploadButton("Click to upload mod", file_count="single")
        out = gradio.Text("You have not made any changes yet")
        with gradio.Column():
            gradio.Markdown("# Danger!")
            rserv = gradio.Button("RESTART SERVER")
    upl.upload(dl, upl, [out])
    rserv.click(rServ, None, [out])
configPage.launch()