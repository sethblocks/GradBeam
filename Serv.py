import subprocess
import shutil
import gradio
import gradio.themes.glass
serv = subprocess.Popen(["C:\\Users\\seth2\\AppData\\Local\\Roblox\\Versions\\version-2cca5ed32b534b2a\\RobloxPlayerBeta.exe"])

def rServ():
    global serv
    serv.kill()
    serv = subprocess.Popen(["C:\\Users\\seth2\\AppData\\Local\\Roblox\\Versions\\version-2cca5ed32b534b2a\\RobloxPlayerBeta.exe"])
    return("Restarted Server!")
    

def dl(upl):
    for uploadint in range(len(upl)):
        upload = upl[uploadint]
        shutil.copyfile(upload, "C:\\Users\\seth2\\Desktop\\GradBeam\\beta\\" + upload.split("\\")[len(upload.split("\\"))-1])
        
        yield "uploaded " + str(uploadint+1) + " out of " + str(len(upl))
    return "Mods Uploaded! Restart Server To Apply!"
import json
map = "Click Show Map File to see current map"

def mshow():
    return json.JSONDecoder().decode(open("testing.json").read())["map"]

def setmap(map):
    conf = json.JSONDecoder().decode(open("testing.json").read())
    conf["map"] = map
    open("testing.json", "w").write(json.JSONEncoder().encode(conf))
    return "Map is now: " + map



# GRADIO




theme = gradio.themes.Glass(
    primary_hue="orange",
    secondary_hue="orange",
    neutral_hue="orange",
    text_size="lg",
    radius_size="lg",
    font=['Candara', 'Candara', 'Noto Sans', 'source-sans-pro'],
).set(
    body_background_fill='#2e1500',
    body_background_fill_dark='#2e1500',
    body_text_color='*neutral_100',
    background_fill_primary='*neutral_700',
    background_fill_secondary='*primary_800',
    border_color_accent='*neutral_600',
    border_color_primary='*primary_500',
    color_accent_soft='*neutral_700',
    shadow_drop='rgba(0,0,0,0.05) 0px 5px 5px 0px',
    block_background_fill='*primary_800',
    block_border_width='1px',
    block_label_background_fill='*primary_700',
    block_label_text_color='*neutral_200',
    block_title_text_color='*neutral_200',
    checkbox_background_color='*primary_600',
    checkbox_border_color='*neutral_700',
    checkbox_border_color_hover='*neutral_600',
    checkbox_label_border_width='*input_border_width',
    error_background_fill='*background_fill_primary',
    error_border_color='#ef4444',
    error_text_color='#fef2f2',
    error_icon_color='#ef4444',
    input_background_fill='*secondary_600',
    input_background_fill_focus='*secondary_600',
    input_border_color_focus='*primary_400',
    input_placeholder_color='*neutral_500',
    stat_background_fill='*primary_500',
    table_border_color='*neutral_700',
    table_even_background_fill_dark='*neutral_50',
    table_odd_background_fill='*neutral_700',
    button_border_width='*input_border_width',
    button_primary_background_fill='linear-gradient(180deg, *primary_400 0%, *primary_500 50%, *primary_600 50%, *primary_500 100%)',
    button_primary_background_fill_hover='linear-gradient(180deg, *primary_400 0%, *primary_500 50%, *primary_600 50%, *primary_500 100%)',
    button_primary_border_color='*primary_600'
)



with gradio.Blocks(theme=theme, title="BeamMP Server") as configPage:
    gradio.Markdown("# Configure BeamMP Server\nV0.2")
    with gradio.Row():
        upl= inputs=gradio.UploadButton("Click to upload mods", file_types=["zip"], file_count="multiple")
        out = gradio.Text("You have not made any changes yet")
        with gradio.Row():
            gradio.Markdown("# Danger!")
            rserv = gradio.Button("RESTART SERVER")
    with gradio.Row():
        with gradio.Row():
            gradio.Markdown("""Vanilla Maps: 
/levels/gridmap_v2/info.json
/levels/johnson_valley/info.json
/levels/automation_test_track/info.json
/levels/east_coast_usa/info.json
/levels/hirochi_raceway/info.json
/levels/italy/info.json
/levels/jungle_rock_island/info.json
/levels/industrial/info.json
/levels/small_island/info.json
/levels/smallgrid/info.json
/levels/utah/info.json
/levels/west_coast_usa/info.json
/levels/driver_training/info.json
/levels/derby/info.json""")
            mapsetter = gradio.Text(map)
            setm = gradio.Button("Set Map File")
            showm = gradio.Button("Show Current Map File")
    upl.upload(dl, upl, [out])
    rserv.click(rServ, None, [out])
    showm.click(mshow, None, [mapsetter])
    setm.click(setmap, mapsetter, [out])
configPage.launch(debug=True)