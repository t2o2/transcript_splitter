mkdir -p samples

echo "Download sample videos"
youtube-dl -f 'bestvideo[ext=mp4][height<=480]+bestaudio/best[height<=480]' VMvdvP02f-Y -o samples/Kalanick_TechCocktail_VMvdvP02f-Y.mkv
youtube-dl -f 'bestvideo[ext=mp4][height<=480]+bestaudio/best[height<=480]' KopLe5NZBJc -o samples/Ballmer_DavidRubensteinShow_KopLe5NZBJc.mkv
youtube-dl -f 'bestvideo[ext=mp4][height<=480]+bestaudio/best[height<=480]' s5zXIjGlzDU -o samples/Kalanick_DisruptSF2014_s5zXIjGlzDU.mkv
youtube-dl -f 'bestvideo[ext=mp4][height<=480]+bestaudio/best[height<=480]' NUl-a3GZznQ -o samples/Nadella_DavidRubensteinShow_NUl-a3GZznQ.mkv

echo "Download subtitles"
youtube-dl https://www.youtube.com/watch?v=VMvdvP02f-Y --skip-download --write-sub --write-auto-sub --sub
 -lang en -o Kalanick_TechCocktail_VMvdvP02f-Y.vtt


