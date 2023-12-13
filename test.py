from pyrogram import Client
import os
import pandas

API_ID = os.environ.get("ID")
API_HASH = os.environ.get("HASH")



app = Client("my_account2", api_id=API_ID, api_hash=API_HASH)
# nest_asyncio.apply()
async def main():

    # df = pd.DataFrame(columns=['id', 'date', 'content', 'user', 'photo_w', 'photo_h','video', 'voice', 'video_note'])
    dff = pandas.read_excel('teleanal_bd.xlsx', usecols='B:J')
    last_id = list(dff.id.tail(1))[0]
    print(last_id)
    async with app:

        async for message in app.get_chat_history(chat_id=323893921, offset_id = last_id+1, reverse=True):

            id = message.id
            date = str(message.date)
            text = message.text
            name = message.from_user.first_name

            try:
                photo_w = message.photo.width
            except:
                photo_w = 'net'

            try:
                photo_h = message.photo.height
            except:
                photo_h = 'net'

            try:
                video = message.video.file_unique_id
            except:
                video = 'net'

            try:
                voice = message.voice.duration
            except:
                voice = 'net'

            try:
                video_note = message.video_note.duration
            except:
                video_note = 'net'

            new_row = [id, date, text, name, photo_w,photo_h, video, voice, video_note]
            print(new_row)

            dff.loc[len(dff)] = new_row


    dff.to_excel(f'teleanal_bd.xlsx')


    df['text_l'] = df['content'].str.len()
    df['date'] = pandas.to_datetime(df['date'])

app.run(main())