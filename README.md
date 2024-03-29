# TDDiffusionAPI (TDA)
<a href="https://discord.com/invite/wNW8xkEjrf"><img src="https://discord.com/api/guilds/838923088997122100/widget.png?style=shield" alt="Discord Shield"/></a>

TouchDesigner interface for [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) API

![image](https://user-images.githubusercontent.com/11017531/230521603-730908a4-097a-495c-8473-82e123109d70.png)

## Version 2.1.1
### Features:
* **Easy install (no additional libraries & scripts).** Start A1111 with api flag, drag & drop .tox to your project and you ready to go!
* **img2img mode.** Connect any TOP to TDA and start generating images.
* **Stream mode**. Enable toggle to start auto-generation (live mode).
* [**Multi-Controlnet.**](https://github.com/Mikubill/sd-webui-controlnet) Multiple ControlNet inputs for a single generation. Connect any TOP to TDA controlNet TOP input.
* **Inpainting.** Connect mask to "inpaintMask" input. Only for img2img.
* **Scripts & Extensions.** Partial support, not all scripts can be run in TD.
* **Aditional tools.** Support for Hires Fix, Refiner.
* **Checkpoints.** You can select any checkpoint (from A1111) straight in TDA.
* **Upscale.** connect any TOP to TDA extras TOP input and upscale images.
* **Clip interrogator.** Connect any TOP to TDA and interrogate CLIP to get describing prompt.
* **Annotation.** Most parameter now have help info. Hold ALT + rollover mouse on parameter.
* **Save images.** Now you can set to save images in folder or keep (only last) image in TOP out.
* **OSX support.**
* **Optimization.** Stable FPS and generation speed improvements.
	
## Installation
1. Install [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui#installation-and-running)
2. Set "--api" flag in web-user.bat 
3. Download latest [TDA component](https://github.com/olegchomp/TDDiffusionAPI/releases)
4. Add TDDiffusionAPI.tox to TouchDesigner project.
5. Run "Refresh" in "Dependencies" of TDA settings.
