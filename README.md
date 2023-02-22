# TDDiffusionAPI (TDA)
Stable Diffusion image generator in TouchDesigner with [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) API


![TDDiffusion](https://user-images.githubusercontent.com/11017531/209246887-78790ddd-2629-4ec9-b512-2b89112df7ad.png)

## Version 2.0.0
### Features:
* Easy install (no additional libraries & scripts). Start A1111 with api flag, drag & drop .tox to your project and you ready to go!
* img2img mode. Connect any TOP to TDA and start generating images.
* Checkpoints. You can select any checkpoint (from A1111) straight in TDA.
* Sampling methods. Also you can select samplers in TDA.
* Clip interrogator. Connect any TOP to TDA and interrogate CLIP to get describing prompt.
* Annotation. Every parameter now have help info. Hold ALT + rollover mouse on parameter.
* Save images. Now you can set to save images in folder or keep (only last) image in TOP out.
* OSX support.
* Optimization. Stable FPS and generation speed improvements.
	
## Installation
1. Install [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui#installation-and-running)
2. Set "--api" flag in web-user.bat 
3. Download latest [TDA component](https://github.com/olegchomp/TDDiffusionAPI/releases)
4. Add TDDiffusionAPI.tox to TouchDesigner project.
5. Set "Working folder" in TDA settings.
6. Run "Check" in "Dependencies" of TDA settings.
	
## Roadmap 
Use pull request or discord server to suggest tasks 

- [ ] Seed travel
- [ ] Save sampling steps
- [ ] ControlNet
- [x] txt2img
- [x] Lexica API
- [x] img2img
- [x] Model select
- [x] Check updates
- [x] Samplers
- [x] In App anotation
- [x] CLIP interrogator
