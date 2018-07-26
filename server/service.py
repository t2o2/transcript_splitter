import os
from aiohttp import web
from converters.vtt2txt import convert_vtt2txt


async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name
    return web.Response(text=text)

async def download_cc(request):
    vid = request.match_info.get('vid')
    if vid is None:
        return web.Response(text='')
    vtt_file = '/tmp/transcript_{vid}'.format(vid=vid)
    txt_file = '/tmp/transcript_{vid}.en.txt'.format(vid=vid)
    os.system('youtube-dl https://www.youtube.com/watch?v={vid} --skip-download --write-sub --write-auto-sub --sub-lang en -o "{vtt}"'.format(vid=vid, vtt=vtt_file))
    vtt_file += '.en.vtt'
    print('vtt: {}'.format(vtt_file))
    print('txt: {}'.format(txt_file))
    convert_vtt2txt(vtt_file, txt_file)
    out = ''
    with open(txt_file, 'r') as f:
        out = f.read()
    return web.Response(text=out)


app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle),
    web.get('/dl_cc/{vid}', download_cc)
    ])

web.run_app(app)
