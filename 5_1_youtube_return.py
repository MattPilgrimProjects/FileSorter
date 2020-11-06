import app
import library.file
import library.csv
import library.json
import library.cron
import library.url
import library.comment


            params = (
                ('q', artist+" "+track),
                ('part', 'snippet'),
                ('key', '')
            )
            library.cron.delay(1)
            content = library.url.youtube_web_api(params,app.settings["spotify"]["auth"])
            library.json.export_json(filename,content)

            library.comment.returnMessage("Added "+filename)



#             GET https://youtube.googleapis.com/youtube/v3/search?part=snippet&q=Slipknot%20Wait%20And%20Bleed&key=[YOUR_API_KEY] HTTP/1.1

# Authorization: Bearer [YOUR_ACCESS_TOKEN]
# Accept: application/json

# ?part=snippet&q=Slipknot%20Wait%20And%20Bleed&key=[YOUR_API_KEY]