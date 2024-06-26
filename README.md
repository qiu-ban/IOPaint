## Development
安装[nodejs](https://nodejs.org/en)，然后安装前端相应依赖

```bash
git clone https://github.com/qiu-ban/IOPaint.git
cd IOPaint/web_app
npm install
npm run build
cp -r dist/ ../iopaint/web_app
```

`web-app`下新建`.env.local`文件，写入`VITE_BACKEND=http://127.0.0.1:9999`

运行前端
```bash
npm run dev
```

安装后端依赖，火山引擎的sdk已经集成在里面。这里会触发到github下载一次big-lama模型，最好科学上网一下。
```bash
pip install -r requirements.txt
python3 main.py start --model lama --port 9999 --model-dir=./models
```

`conf.json`文件中，填写火山引擎的ak和sk。注意，每次push时，把你的ak、sk删除，不要上传

以上操作完毕后，浏览器访问`http://localhost:5173/` ，在使用消除功能时，如果在控制台看到文案`**********魔改，使用火山引擎inpainting能力**********`，说明执行正确。

注意，目前对于太大的图片，会处理失败，这是因为火山引擎是以base64方式传输图片的，大小有限制，后续会找个图床中转一下
